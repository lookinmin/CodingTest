function solution(book_time) {
  var answer = 0;
  var minutes = [];
  for (let [start, end] of book_time) {
    let [sh, sm] = start.split(':').map(Number);
    let [eh, em] = end.split(':').map(Number);
    minutes.push([sh * 60 + sm, eh * 60 + em + 10]);
  }

  minutes.sort((a, b) => a[0] - b[0]);
  // 시작 빠른거 기준

  let rooms = [];

  const heappush = (heap, item) => {
    heap.push(item);
    heap.sort((a, b) => a - b);
  };

  const heappop = (heap) => {
    return heap.shift();
  };

  for (let [s, e] of minutes) {
    if (rooms.length === 0) {
      heappush(rooms, e);
      // 끝나는 시간 기준 최소 힙 구성
      answer++;
      continue;
    }

    if (rooms[0] <= s) {
      // 다음 시작시간보다 일찍 끝남
      heappop(rooms);
    } else {
      answer++;
      // 방 하나 더 필요함
    }
    heappush(rooms, e);
  }
  return answer;
}
