function solution(s) {
  if (s.length == 4 || s.length == 6) {
    var check = /^\d+$/;
    if (check.test(s)) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}
