function solution(bridge_length, weight, truck_weights) {
  var answer = 0;

  var bridge = Array(bridge_length).fill(0);
  var now = 0;
  while (truck_weights.length > 0) {
    answer++;
    now -= bridge.shift();

    if (truck_weights[0] + now <= weight) {
      let value = truck_weights.shift();
      now += value;
      bridge.push(value);
    } else {
      bridge.push(0);
    }
  }

  answer += bridge_length;
  return answer;
}
