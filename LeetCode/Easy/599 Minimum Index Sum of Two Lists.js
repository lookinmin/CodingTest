var findRestaurant = function (list1, list2) {
  var dic1 = {};
  var dic2 = {};

  list1.forEach((value, idx) => {
    dic1[value] = idx;
  });

  list2.forEach((value, idx) => {
    dic2[value] = idx;
  });

  var tmp = [];
  for (let value of Object.keys(dic1)) {
    if (Object.keys(dic2).includes(value)) {
      tmp.push([value, dic1[value] + dic2[value]]);
    }
  }
  tmp.sort((a, b) => a[1] - b[1]);
  const keyValue = tmp[0][1];
  var res = [];
  res.push(tmp[0][0]);
  for (let i = 1; i < tmp.length; i++) {
    if (tmp[i][1] === keyValue) {
      res.push(tmp[i][0]);
    } else {
      break;
    }
  }
  return res;
};

// -------------------------------------------------------
// faster than before

/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function (list1, list2) {
  var res = new Array();
  var idx = Infinity;

  for (let i = 0; i < list1.length; i++) {
    const j = list2.indexOf(list1[i]);

    if (j !== -1) {
      if (i + j < idx) {
        res = [list1[i]];
        idx = i + j;
        continue;
      } else if (i + j === idx) {
        res.push(list1[i]);
      }
    }
  }
  return res;
};
