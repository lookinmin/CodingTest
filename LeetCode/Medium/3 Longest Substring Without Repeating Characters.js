var lengthOfLongestSubstring = function(s) {
    if (s === "") {
        return 0;
    }

    var res = new Array();
    var tmp = new Array();

    for (let i = 0; i < s.length; i++) {
        if (!tmp.includes(s[i])) {
            tmp.push(s[i]);
        } else {
            res.push(tmp.length); // 중복 발생 시 현재 부분 문자열의 길이를 기록
            tmp = tmp.slice(tmp.indexOf(s[i]) + 1); // 중복된 문자 이후로 자르고 새 부분 문자열 시작
            tmp.push(s[i]); // 현재 문자를 추가
        }
    }

    res.push(tmp.length); // 마지막 부분 문자열의 길이도 기록

    return Math.max(...res); // 가장 큰 부분 문자열 길이를 반환
};