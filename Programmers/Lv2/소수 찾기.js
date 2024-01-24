const permutations = (array, size) => {
  var result = [];
  if (size === 1) return array.map((v) => [v]);
  else {
    array.forEach((fixed, idx, origin) => {
      const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
      const tmp = permutations(rest, size - 1);
      const attached = tmp.map((tmp) => [fixed, ...tmp]);
      result.push(...attached);
    });
  }
  return result;
};

const isPrime = (num) => {
  if (num < 2) return false;

  for (let i = 2; i <= Math.sqrt(num); i++) {
    const remainder = num % i;
    if (remainder === 0) return false;
  }
  return true;
};

function solution(numbers) {
  var answer = new Set();

  for (let i = 1; i <= numbers.length; i++) {
    const getList = [...permutations([...numbers], i)];
    const primeNumbers = getList.filter((arr) => {
      const number = +arr.join("");
      const check = isPrime(number);
      return check;
    });

    primeNumbers.forEach((arr) => {
      answer.add(+arr.join(""));
    });
  }

  return answer.size;
}
