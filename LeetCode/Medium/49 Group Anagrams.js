var groupAnagrams = function(strs) {
    var res = [];

    var solid = new Map();
    strs.forEach((s) => {
        let tmp = s.split('').sort().join('');
        if(solid.has(tmp)){ 
            res[solid.get(tmp)].push(s);
        } else {
            solid.set(tmp, res.length);
            res.push([s]);
        }
    });
    return res;
};