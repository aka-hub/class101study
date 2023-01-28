
#%%

import PySimpleGUI as sg
import pandas as pd
import numpy as np
import PyInstaller
from datetime import datetime

sg.theme("BrownBlue")

#%%
list1=['회사이름_설비이름']

list=['INPUT_DATE']
list.extend('ITEM00' + str(i) for i in range(1,10))
list.extend('ITEM0' + str(i) for i in range(10,61))


#%%

#App layout 설계
layout = [
    [sg.T("",background_color='steelblue')],
    [sg.Text("Input Raw file: ",background_color='steelblue'),
    sg.Input(key="-IN-"),
    sg.FileBrowse(file_types=(("ALL CSV Files", "*.csv"), ("ALL Files", "*.*"), )),
    sg.Text('            ',background_color='steelblue'),
    sg.Button("Run the program", button_color = ('black','orange'))],
    [sg.Text('',background_color='steelblue')],
    [sg.Text("설비 수",background_color='steelblue'),
    sg.Output(key="-OUT1-", size=(15)),
    sg.Text('         ',background_color='steelblue'),
    sg.Text("전력 데이터 수",background_color='steelblue'),
    sg.Output(key="-OUT2-", size=(15)),
    sg.Text('         ',background_color='steelblue'),
    sg.Text('날짜 조회',background_color='steelblue'),
    sg.InputText(key="-startdate-", size=(15)), 
    sg.Text(' - ',background_color='steelblue'),
    sg.InputText(key="-enddate-",size=(15)),
    sg.Button('datecheck')],

    [sg.Text('',background_color='steelblue')],
    [sg.Table(key='Table0',values=[],
                headings=['수요기업 이름'],
                auto_size_columns=False,
                col_widths=[10],
                num_rows=30,
                display_row_numbers=True,
                justification='center',
                vertical_scroll_only=False,
                background_color="#FFFFFF",
                text_color="black",),
    sg.Table(key='Table1',values=[],
                headings=['데이터 종류','단위'],
                auto_size_columns=False,
                col_widths=[10],
                num_rows=30,
                display_row_numbers=True,
                justification='center',
                vertical_scroll_only=False,
                background_color="#FFFFFF",
                text_color="black",),
    sg.Table(key='Table2',values=[],
                headings=list1,
                auto_size_columns=False,
                col_widths=[20],
                num_rows=30,
                display_row_numbers=True,
                vertical_scroll_only=False,
                justification='center',
                background_color="#FFFFFF",
                text_color="black",),
    sg.Table(key='Table3',values=[],
                headings=list,
                auto_size_columns=False,
                col_widths=[10],
                num_rows=30,
                vertical_scroll_only=False,
                justification='center',
                display_row_numbers=True,
                background_color="#FFFFFF",
                text_color="black",
                expand_x=True)],
    [sg.Text('                                                                                                     ',background_color='steelblue'),
     sg.Input(key='-FILE1-',size=(17)),sg.Button('Save As',key='SaveAs1'),sg.Button('Save',key='Save1'),
     sg.Text('                                 ',background_color='steelblue'),
     sg.Input(key='-FILE2-',size=(60)),sg.Button('Save As',key='SaveAs2'),sg.Button('Save',key='Save2')]
]



#Open app window
window = sg.Window('Company data processing', layout, size=(1500,750), icon='Images/BIGAI_icon.ico',background_color='steelblue')
filename = ""
while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Run the program":
            filename = values['-IN-']

            df00=pd.read_csv(filename)
            data_type=df00.drop_duplicates(subset='prmtTy', keep="last").reset_index(drop=True)
            data_type=data_type.loc[:,['prmtTy','unitCd']]


            data3 = data_type[0:].values.tolist()
            window.Element('Table1').update(values=data3)


            df1 = pd.read_csv(filename)
            mask = np.column_stack([df1['unitCd'].astype(str).eq("KW") for col in df1])
            df1=df1.loc[mask.any(axis=1)].reset_index(drop=True)

            df_comp=df1.drop_duplicates(subset='siteNm', keep="last").reset_index(drop=True)
            df_comp=df_comp.loc[:,['siteNm']]
            df_comp.columns=['수요기업']

            data0 = df_comp[0:].values.tolist()
            window.Element('Table0').update(values=data0)


            company=df_comp['수요기업'].values[0]
            df0=df1.drop_duplicates(subset='prmtNm', keep="last").reset_index(drop=True)
            df2=df0.loc[:,['prmtNm']]
            df2.columns=[company]
            df2[company]=df2[company].str.rstrip('_유효전력')
            df2=df2[df2[company].str.contains(company)==False]

            data1 = df2[0:].values.tolist()
            window.Element('Table2').update(values=data1)


            df_out=pd.DataFrame()
            k=1
            for u in df1['prmtNm'].unique():
                #file_name = '설비들\{0}.xlsx'.format(u) 
                df00=df1[df1['prmtNm'] == u].sort_index(ascending=False).reset_index(drop=True)
                if k==1:
                    df00.rename(columns={'actTm':'INPUT_DATE','value':'ITEM00%s' %k}, inplace=True)
                    df01=pd.DataFrame(df00['INPUT_DATE'])
                    df01['INPUT_DATE'] = pd.to_datetime(df01['INPUT_DATE']).dt.date
                    df02=pd.DataFrame(df00['ITEM00%s' %k])
                    df_out=pd.concat([df_out,df01,df02], axis=1)
                if k>1 and k<10:
                    df00.rename(columns={'value':'ITEM00%s' %k}, inplace=True)
                    df00=pd.DataFrame(df00['ITEM00%s' %k])
                    df_out=pd.concat([df_out,df00], axis=1)
                if k>=10:
                    df00.rename(columns={'value':'ITEM0%s' %k}, inplace=True)
                    df00=pd.DataFrame(df00['ITEM0%s' %k])
                    df_out=pd.concat([df_out,df00], axis=1)
                k=k+1


            data2 = df_out[0:].values.tolist()
            window.Element('Table3').update(values=data2)
            

            window.Element('-OUT1-').update(value=len(df2))

            window.Element('-OUT2-').update(value=len(df_out)*(len(df_out.columns)-1))
        
        elif event == "datecheck":
            startdate = '2022-09-01'
            enddate = '2022-09-02'
            mask = startdate
            
            sg.popup("test")        

           
        elif event == "SaveAs1":
            filename = values['-FILE1-']
            filename = sg.popup_get_file("Save As", default_extension='.csv', default_path=filename, save_as=True, file_types=(("All CSV Files", "*.csv"),), no_window=True)
            if filename:
                window['-FILE1-'].update(filename)

        elif event == 'Save1':
            filename = values['-FILE1-']
            if filename:
                try:
                    with open(filename, 'wt') as f:
                        f.write('\n'.join([','.join(item) for item in [list1]+data1]))
                    sg.popup(f"File {repr(filename)} Saved !!!")
                    continue
                except PermissionError:
                    pass
            sg.popup(f"Cannot open file {repr(filename)} !!!")
        elif event == "SaveAs2":
            filename = values['-FILE2-']
            filename = sg.popup_get_file("Save As", default_extension='.csv', default_path=filename, save_as=True, file_types=(("All CSV Files", "*.csv"),), no_window=True)
            if filename:
                window['-FILE2-'].update(filename)

        elif event == 'Save2':
            filename = values['-FILE2-']
            if filename:
                try:
                    with open(filename, 'wt') as f:
                        f.write('\n'.join([','.join(map(str,item)) for item in [list]+data2]))
                    sg.popup(f"File {repr(filename)} Saved !!!")
                    continue
                except PermissionError:
                    pass
            sg.popup(f"Cannot open file {repr(filename)} !!!")

                 
window.close()

#%%

