var reverseVowels = function (s) {
  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

  var normal = []; //큐
  var vow = []; //스택
  var turn = [];
  for (let w of s) {
    if (vowels.includes(w)) {
      turn.push(1);
      vow.push(w);
    } else {
      turn.push(0);
      normal.push(w);
    }
  }

  var res = '';
  for (let num of turn) {
    if (num === 1) {
      res += vow.pop();
    } else {
      res += normal.shift();
    }
  }
  return res;
};
