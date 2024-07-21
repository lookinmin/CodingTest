var isUgly = function(n) {
    if(n <= 0) return false;
    if(n === 1) return true;
    var nums = [2, 3, 5];
    for(let num of nums){
        while(n % num === 0){
            n /= num;
        }
    }
    return n === 1;
};