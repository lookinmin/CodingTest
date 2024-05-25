function solution(topping) {
    var answer = 0;
    
    var me = {};
    var unique = 0;
    var bro = new Set();
    
    for(top of topping){
        if(!me[top]){
            me[top] = 1;
            unique += 1;
        } else {
            me[top] += 1;
        }
    }
    
    for(top of topping){
        me[top] -= 1;
        bro.add(top);
        
        if(me[top] == 0){
            unique -= 1;
            delete me[top];
        }

        if(unique === bro.size){
            answer += 1;
        } 
    }
    return answer;
}