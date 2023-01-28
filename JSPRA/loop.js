// const animals = [
//     {name : "monkey", size: "medium", isAggresive: false, weight:15},
//     {name : "tiger", size: "big", isAggresive: true, weight:60},
//     {name : "cat", size: "small", isAggresive: true, weight:8},
//     {name : "gecko", size: "small", isAggresive: false, weight:1},
// ]

// for(let i = 0; i < animals.length; i++){

// }
// // 밑과 위가 같음
// for(let animal of animals){

// }
// //c언어랑 비슷한듯 해용 
// let i  = 0;
// while(i < 10){
//     i++;
// }
// // forEach map reduce filter



// animals.forEach(function(animal, index){

// }) // 같은 반복문-찾아볼것

// const mappedAnimal = animals.map(function (animal){
//     //애로우로 넘기면 animals.map(animals=>{}으로 생략 가능

//     return animal.name //반환형식 저장
//  //맵은 재정의
// })

// //filter는 조건 부합하는 경우만 넘김

// const filteredAnimal =animals.filter(animal=>{
//     return animal.weight >= 10
// })

// //출려근 console.log(~~)로 했음

// //reduce 맵, 필터 둘 다 가능하나 합구하는 걸 자주 씀

// const reduceAnimal = animals.reduce((acc, cur)=>{ //합해지는 값, 현재값)
//     return acc + cur.weight
// }, 0) //초기값 지정을 0으로 둠


