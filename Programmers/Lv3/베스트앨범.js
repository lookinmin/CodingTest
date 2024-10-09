function solution(genres, plays) {
  var res = [];
  var dict = {};
  // 각 장르별 노래 2개씩
  for (let i = 0; i < genres.length; i++) {
    if (genres[i] in dict) {
      dict[genres[i]].total += plays[i];
      dict[genres[i]].songs.push({ idx: i, plays: plays[i] });
    } else {
      dict[genres[i]] = {
        total: plays[i],
        songs: [{ idx: i, plays: plays[i] }],
      };
    }
  }

  const cvt = Object.entries(dict).sort((a, b) => b[1].total - a[1].total);
  for (let i = 0; i < cvt.length; i++) {
    var tmp = cvt[i][1].songs.sort(
      (a, b) => b.plays - a.plays || a.idx - b.idx,
    );
    for (let j = 0; j < Math.min(2, tmp.length); j++) {
      res.push(tmp[j].idx);
    }
  }
  return res;
}
