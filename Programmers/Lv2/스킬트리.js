function solution(skill, skill_trees) {
    var answer = 0;
    
    for(tree of skill_trees){
        var stack = [];
        for(w of tree){
            if(skill.includes(w)){
                stack.push(w)
            }
        }
        var flag = true;
        for(let i = 0 ; i < stack.length; i++){
            if(stack[i] !== skill[i]){
                flag = false;
                break;
            }
        }
        if(flag){
            answer += 1;
        }
    
    }
    return answer;
}