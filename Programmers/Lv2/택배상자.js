function solution(order) {
  var answer = 0;
  var stack = []; // 보조 컨테이너
  // var items = Array.from({length : order.length}, (_, i) => i + 1);
  // var items = [...Array(order.length).keys()].map(i => i + 1);
  let idx = 0;
  for (let i = 0; i <= order.length; i++) {
    if (order[idx] !== i) {
      stack.push(i);
    } else {
      idx++;
      answer++;
    }

    while (stack.length > 0 && stack.at(-1) === order[idx]) {
      stack.pop();
      idx++;
      answer++;
    }
  }

  // for(num of items){
  //     if(order[0] !== num){
  //         stack.push(num);
  //     } else {
  //         order.shift();      // shift에서 시간초과 발생
  //         answer++;
  //     }
  //     while(stack.length > 0 && stack.at(-1) === order[0]){
  //         stack.pop();
  //         order.shift();
  //         answer++;
  //     }
  // }

  return answer;
}
