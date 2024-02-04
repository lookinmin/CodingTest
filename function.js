arr = ["hi", "my name", "is", "minsu"];
str = "hi my name is minsu";

console.log(arr.join(" ")); // List -> string
console.log(str.split(" ")); // string -> List
arr.reverse();
console.log(arr.splice(0, 2)); // 원본 배열의 변환 발생

console.log(arr.slice(0, 2)); // 원본 배열을 변환하지 않음
console.log(arr);

console.log(arr.find((value) => value === "my name")); // 콜백함수의 조건을 만족하는 값을 리턴 (idx아님)

console.log(arr.filter((value) => value.includes("i")));
console.log(arr.map((value) => value.toUpperCase()));
test = [300, 500, 10, 25, 550];

console.log(test.some((value) => value > 400));
console.log(test.every((value) => value > 100));
console.log(
  test.reduce((prev, now) => {
    return prev + now;
  }, 0)
);

console.log(test.sort((a, b) => a - b));
console.log(arr.sort().reverse());
let check = /minsu/;
console.log(check.test(str));
console.log(str.match(/minsu/));

// 가장 기본
const getJson = async () => {
  const response = await fetch("URL");
  const data = await response.json();
};

// Method 구현

const methodFunc = async (url = "", data = {}) => {
  try {
    const response = await fetch(url, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify(data),
      // body의 type은 반드시 Content-Type 헤더와 일치할 것
    });
    return response.json();
  } catch (err) {
    console.log(err);
  }
};

// axios로 post

const axiosPost = async (body) => {
  try {
    const res = await axiosPost.post(url, body);
    const data = res.data;
    return data;
  } catch (err) {
    console.log(err);
  }
};

// axios + params

const paramsAxios = async ({ offset = 0, limit = 10 }) => {
  try {
    const res = await axios.get(url, {
      params: { offset, limit },
    });
    const product = res.data;
    return product;
  } catch (err) {
    console.log(err);
  }
};
