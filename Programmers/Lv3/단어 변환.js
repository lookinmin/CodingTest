function solution(begin, target, words) {
  var answer = Infinity;
  if (!words.includes(target)) {
    return 0;
  }

  const visited = new Set();

  const dfs = (s, cnt) => {
    if (s === target) {
      answer = Math.min(cnt, answer);
    }

    for (let word of words) {
      if (!visited.has(word) && cvt(s, word)) {
        visited.add(word);
        dfs(word, cnt + 1);
        visited.delete(word);
      }
    }
  };

  const cvt = (s1, s2) => {
    let diff = 0;
    for (let i = 0; i < s1.length; i++) {
      if (s1[i] !== s2[i]) {
        diff++;
      }
    }

    if (diff === 1) {
      return true;
    } else if (diff > 1) {
      return false;
    }
  };

  dfs(begin, 0);
  return answer;
}
