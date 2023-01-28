// // 조건문, function arrow

// if(x==10){
//     console.log("~");
// }
// // x===10 이런식으로 =을 3개쓰면 자료형과 값 둘 다 비교 가능
// //else나 else if는 c랑 비슷

// //삼항연산자도 존재
// // 조건 ? 참일경우 : 아닐경우 ;

// x > 20 ? group = "senior" : group = "junior"; 
// //x가  20 초과일 경우 senior 그룹, 아닐시 junior 그룹 

// //switch문도 존재

// switch(animal){
//     case 'lion':
//         console.log("big");
//         break;
//     case 'tiger':
//         console.log("big");

//     default:
//         console.log("big");

// }

// //자바스크립트에서 함수를사용하는 방법

// function add(a=0, b=0){ // 초기값 설정을 0으로 해둔것
//     return a +b;

// } //일케 작성하면 윈도우에 담겨서 안정적이지 않음

// const sum1 = function(a, b) {return a+b} // 익명 함수, 변수에 함수 담는 것


// const sum2 = (a,b)=>{return a+b}
// //이처럼 하는 게 바람직함 ㅇ애로우 펑션 사용하세ㅣㅂ쇼
