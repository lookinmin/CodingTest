/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function (area) {
  // W - L

  var half = Math.ceil(Math.sqrt(area));
  for (let num = half; num <= area; num++) {
    let k = area / num;
    if (Number.isInteger(k)) {
      return [num, k];
    }
  }
};
