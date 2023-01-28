// function song(){
//     const title = "window";
//     const singer =  "kyul";
// }


//construction function
function song(title, singer){
    this.title = title;
    this.singer = singer;
    TouchList.getinfo = function(){ 
        return `이 곡의 제목은 ${this.title}고 가수는 ${this.singer}입니다.`;
    } // 함수도 가능, 구조체인듯

}

const song1 = new song("window", "kyul"); //new 키워드 사용해야함
//구조체같은 느,끼밍ㄴ듯 해요 근데 객체지향이 있는(oop)
//c++이랑 비슷ㅅ한듯

//prototype 사용법

song.prototype.getyear = function(){
    //프로토타입안에 숨는다? 출력했을떄?찾ㅇ봐야할듯

}

//클래스의 경우;

class Song{
    constructor(title, singer, year){
        this.title = title;
        this.singer = singer;
        this.year = year;

    }
    getinfo(){
        return `어쩌구`;
    }
}