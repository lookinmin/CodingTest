// 둘만의 암호, Lv1, JS 풀이

function solution(s, skip, index) {
    var answer = '';
    let arr = s.split('');

    arr.map((word) => {
        let tmp = word.charCodeAt();
        for(let i = 0; i < index; i++){
            tmp++;

            if(tmp > 122)
                tmp = 97;

            while(skip.includes(String.fromCodePoint(tmp))){
                tmp++;
                if(tmp > 122)
                    tmp = 97;

            }
        }

        answer = answer + String.fromCodePoint(tmp);

    });


    return answer;
}