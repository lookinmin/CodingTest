/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function (date) {
  // 날짜를 연도, 월, 일로 분리
  date = date.split('-').map(Number);
  const year = date[0];
  const month = date[1];
  const day = date[2];

  // 각 월의 일수를 정의 (평년 기준)
  const dayForMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  // 윤년인지 확인
  const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
  if (isLeapYear) {
    dayForMonths[2] = 29; // 2월을 29일로 설정
  }

  // 총 일수를 계산
  let total = day;
  for (let m = 1; m < month; m++) {
    total += dayForMonths[m];
  }

  return total;
};
