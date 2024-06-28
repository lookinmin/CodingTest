// var lst = new Array(10);
// for(let i = 1; i <= 10; i ++){
//     lst[i-1] = i;
// }

// console.log(lst);

// console.log(lst.find((e) => e === 3));
// console.log(lst.findIndex((e) => e === 3));

var arr = new Array();
num = 10;
for(let i = 0; i < 10; i++){
    arr.push([i + 1, num]);
    num++;
}

// console.log(arr);
// console.log(arr.find(([x, y]) => x === 2 && y === 10));
// console.log(arr.findIndex(([x, y]) => x === 1 && y === 10));

var filteredArr = arr.filter(([x, y]) => y % 2 === 0);
console.log(filteredArr)