
const solve = (arr) => {
    let map = new Map();

    for(num of arr){
        map.set(num, (map.get(num) || 0) + 1)
    }

    tmp = [...map].sort((a, b) => b[1] - a[1]);
    console.log(tmp);

    return tmp.length === 1 || tmp[0][1] > tmp[1][1] ? tmp[0][0] : -1;
}

console.log(solve([1, 3, 5, 9, 2, 4, 10, 3, 5]));

