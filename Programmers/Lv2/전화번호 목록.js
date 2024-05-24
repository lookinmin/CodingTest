function solution(phone_book) {
  var answer = true;
  phone_book.sort();

  for (let i = 0; i < phone_book.length - 1; i++) {
    var k = phone_book[i].length;
    if (phone_book[i] === phone_book[i + 1].substring(0, k)) {
      return false;
    }
  }
  return answer;
}
