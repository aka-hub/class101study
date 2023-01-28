const todoinput = document.querySelector("#todo-input");
const check = document.querySelector("#checked");
const weeklist = document.querySelector(".weeklist");

todoinput.addEventListener("keypress", function(e){
    if(e.keyCode===13){
        generatetodo(todoinput.value);
    }
})



function pressplus(){
    generatetodo(todoinput.value);
}

const generatetodo = (todo) =>{
    const li = document.createElement("li"); 

    const checkedspan = generatechecked();
    const textspan = generatetext(todo);
    const datespan = generatedate();

    li.appendChild(checkedspan);
    li.appendChild(textspan);
    li.appendChild(datespan);
    
    weeklist.appendChild(li);


}



const generatechecked = ()=>{
    const span = document.createElement("span");
    span.classList.add("todo-checked");
    const icon = document.createElement("i");
    icon.innerHTML='<i class="fa-regular fa-square"></i>';
    span.appendChild(icon);
    icon.addEventListener("click",() =>{
        if(icon.innerHTML=='<i class="fa-regular fa-square"></i>'){
            icon.innerHTML='<i class="fa-regular fa-square-check"></i>';
        }
        else if(icon.innerHTML=='<i class="fa-regular fa-square-check"></i>'){
            icon.innerHTML='<i class="fa-regular fa-square"></i>';
            
        }
    })
    console.log(span);
    return span;
}

const generatetext = (todo) =>{
    const span = document.createElement("span");
    span.classList.add("todo-item");
    span.innerText=todo;
    return span;
}


const generatedate = ()=>{
    const span = document.createElement("span");
    span.classList.add("todo-date");
    const icon = document.createElement("i");
    icon.innerHTML='<i class="fa-solid fa-calendar-days"></i>';
    span.appendChild(icon);
    console.log(span);
    return span;
}

