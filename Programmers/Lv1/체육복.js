function solution(n, lost, reserve) {
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a- b);
    
    for(num of reserve){
        if(lost.includes(num)){
            lost = lost.filter((e) => e !== num);
            reserve = reserve.filter((e) => e !== num);
        }
    }
    
    for(num of reserve){
        if(lost.includes(num - 1)){
            lost = lost.filter((e) => e !== num - 1)            
        } else if (lost.includes(num + 1)){
            lost = lost.filter((e) => e !== num + 1)      
        }
    }
    
    return n - lost.length;
}