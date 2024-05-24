function solution(k, tangerine) {
    var answer = new Array();
    var dic = new Map();
    for(num of tangerine){
        dic.set(num, (dic.get(num) || 0) + 1)
    }
    let tmp = [...dic].sort((a, b) => b[1] - a[1]);
    
    while(k > 0){
        let now = tmp[0][1];
        answer.push(tmp[0][0]);
        k -= now;
        tmp.shift()
    }
    return answer.length;
}