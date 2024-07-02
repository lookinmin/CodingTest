var summaryRanges = function(nums) {
    if(nums.length === 0){
        return [];
    }
    const cvt = (a, b) => {
        if(a === b){
            return a.toString();
        }
        return `${a}->${b}`;
    }

    var now = nums[0];
    var res = new Array();
    var tmp = new Array();

    nums.forEach((num => {
        if(num === now){
            tmp.push(num)
            now += 1
        } else {
            res.push(cvt(tmp[0], tmp[tmp.length - 1]));
            tmp = [num];
            now = num + 1;
        }
    }));
    res.push(cvt(tmp[0], tmp[tmp.length - 1]));
    return res;
};