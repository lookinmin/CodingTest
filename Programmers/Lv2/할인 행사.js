const check = (dic, arr) => {
    for(let val of arr){
        if([...dic.keys()].includes(val) && dic.get(val) > 0){
            dic.set(val, dic.get(val) - 1);
        }
    }
    if([...dic.values()].reduce((a, b) => a + b ,0) == 0){
        return true;
    }
    return false;
}

function solution(want, number, discount) {
    var answer = 0;
    var dic = new Map();
    for(let i = 0; i<want.length;i++){
        dic.set(want[i], number[i]);
    }
    
    for(let i = 0; i<= discount.length - 10; i++){
        let tmp = discount.slice(i, i + 10);
        let dicCopy = new Map(dic);
        if (check(dicCopy, tmp)){
            answer += 1;
        }
    }
    
    return answer;
}