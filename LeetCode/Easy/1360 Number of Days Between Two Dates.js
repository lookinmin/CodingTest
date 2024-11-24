/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
var daysBetweenDates = function (date1, date2) {
  const d1 = new Date(date1);
  const d2 = new Date(date2);

  let dateDiff = Math.abs(d1 - d2);
  // 밀리세컨드 기준 차이

  let cvt = dateDiff / (24 * 60 * 60 * 1000);
  return Math.round(cvt);
};
