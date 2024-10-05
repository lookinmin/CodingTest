function solution(word) {
  var vowel = ['A', 'E', 'I', 'O', 'U'];
  var tmp = new Set();

  const dfs = (out) => {
    if (out.length > 5) {
      return;
    }
    tmp.add(out);
    for (let i = 0; i < 5; i++) {
      dfs(out + vowel[i]);
    }
  };

  dfs('');
  var cvt = Array.from(tmp).sort();
  // var cvt = Array(...tmp).sort();

  for (let i = 0; i < cvt.length; i++) {
    if (cvt[i] === word) {
      return i;
    }
  }
}
