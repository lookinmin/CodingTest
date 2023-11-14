function solution(t, p) {
    var answer = 0;
    var k = p.length;
    for(let i = 0; i < t.length - k + 1; i++){
        let tmp = t.slice(i, i + k);
        let cvt = "";
        // tmp.map((item) => {
        //     cvt += item;
        // });
        for(let i = 0; i < tmp.length; i++){
            cvt += tmp[i];
        }

        let num = parseInt(cvt, 10);
        if(num <= parseInt(p, 10)) {
            answer += 1;
        }
    }
    return answer;
}

// map이 왜 안되는지 모르겠다.... tmp가 array가 아닌가