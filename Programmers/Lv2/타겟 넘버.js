function solution(numbers, target) {
    var answer = 0;
    
    const dfs = (nums, idx, cur) => {
        if(idx == nums.length && cur == target){
            answer += 1;
            return
        } else if (idx == nums.length && cur !== target){
            return;
        }
        
        dfs(numbers, idx + 1, cur - numbers[idx]);
        dfs(numbers, idx + 1, cur + numbers[idx]);
    }
    
    dfs(numbers, 0, 0)
    
    return answer;
}