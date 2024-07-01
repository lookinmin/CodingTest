var isAnagram = function(s, t) {
    var tmp = new Map();
    for(let w of s){
        tmp.set(w, (tmp.get(w) || 0) + 1);
    }
    
    for(let w of t){
        if(!tmp.has(w) || tmp.get(w) === 0){
            return false;
        } else {
            tmp.set(w, tmp.get(w) - 1);
        }
    }

    var cnt = 0;
    // [...tmp.values()].forEach((e) => {
    //     cnt += e;
    // });
    cnt = [...tmp.values()].reduce((a, b) => a + b, 0);
    if(cnt === 0){
        return true;
    } else {
        return false;
    }
};