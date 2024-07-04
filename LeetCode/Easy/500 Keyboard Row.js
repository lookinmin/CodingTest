var findWords = function(words) {
    var first = "qwertyuiop";
    var second = "asdfghjkl";
    var last = "zxcvbnm";

    var res = new Array();

    words.forEach((word) => {
        var tmp = new Set();
        word.toLowerCase().split('').forEach((e) => {
            if(first.includes(e)){
                tmp.add(1);
            } else if(second.includes(e)){
                tmp.add(2);
            } else{
                tmp.add(3);
            }
        });
        if(tmp.size === 1){
            res.push(word);
        }
    });
    return res;
};