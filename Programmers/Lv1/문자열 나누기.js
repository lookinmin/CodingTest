function solution(s) {
    var res = [];

    var now = 0;
    var val = 0;
    var otherVal = 0;
    
    flag = false;
    for(let i = 0; i<s.length;i++){
        if(s[now] == s[i]){
            val += 1;        
        } else {
            otherVal += 1;
        }
        
        if (val == otherVal){
            flag = true;
            if (flag){
                res.push(s.slice(now, i + 1));
                now = i + 1;
                flag = false;
                val = 0;
                otherVal = 0;
            }
        }
    }
    
    if(now < s.length && val !== otherVal){
        res.push(s.slice(now))
    }
    
    
    return res.length;
}