/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function (points) {
  // 각 좌표를 문자열로 변환하여 Set에 추가해 중복 체크
  const toSet = new Set(points.map((p) => `${p[0]},${p[1]}`));
  if (toSet.size !== 3) {
    return false; // 점이 중복될 경우 false
  }

  const [p1, p2, p3] = points;

  // 기울기 비교로 일직선 여부 체크
  const slopeCheck = (p1, p2, p3) => {
    return (
      (p2[1] - p1[1]) * (p3[0] - p1[0]) !== (p3[1] - p1[1]) * (p2[0] - p1[0])
    );
  };

  return slopeCheck(p1, p2, p3);
};
