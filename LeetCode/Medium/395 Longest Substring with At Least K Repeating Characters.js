/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
  if (s.length < k) return 0;

  const count = new Map();

  for (let w of s) {
    count.set(w, (count.get(w) || 0) + 1);
  }

  if ([...count.values()].every((v) => v >= k)) {
    return s.length;
  }

  let start = 0;
  let maxLength = 0;

  for (let i = 0; i < s.length; i++) {
    if (count.get(s[i]) < k) {
      maxLength = Math.max(maxLength, longestSubstring(s.slice(start, i), k));
      start = i + 1;
    }
  }

  return Math.max(maxLength, longestSubstring(s.slice(start), k));
};
