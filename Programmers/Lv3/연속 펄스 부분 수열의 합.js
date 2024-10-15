function solution(sequence) {
  const n = sequence.length;

  var psum1 = Array(n + 1).fill(0);
  var psum2 = Array(n + 1).fill(0);

  var max1 = -Infinity;
  var min1 = Infinity;
  var max2 = -Infinity;
  var min2 = Infinity;

  let pulse = 1;
  for (let i = 0; i < n; i++) {
    psum1[i + 1] = psum1[i] + sequence[i] * pulse;
    psum2[i + 1] = psum2[i] + sequence[i] * pulse * -1;
    pulse *= -1;
  }

  for (let i = 0; i < n + 1; i++) {
    max1 = Math.max(psum1[i], max1);
    max2 = Math.max(psum2[i], max2);

    min1 = Math.min(psum1[i], min1);
    min2 = Math.min(psum2[i], min2);
  }

  return Math.max(max1 - min1, max2 - min2);
}
