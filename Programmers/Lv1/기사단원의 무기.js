function solution(number, limit, power) {
    var answer = 0;
    for (let num = 1; num <=number; num ++ ){
        let cnt = 0
        for(let i = 1; i<=Math.sqrt(num);i++){
            if (num % i == 0){
                cnt += 1;
                if (num / i !== i){
                    cnt += 1;
                }
            }
            
        }
        if(cnt > limit){
            answer += power;
        } else {
            answer += cnt;
        }
    }
    
    return answer;
}

// 약수 구하기

var arr = [];
for(let idx = 1; idx <= Math.sqrt(num); idx ++){
    if(num % idx == 0){
        arr.push(idx);
        if(num / idx !== idx){
            arr.push(num / idx);
        }
    }
}

arr.sort((a, b) => a - b);