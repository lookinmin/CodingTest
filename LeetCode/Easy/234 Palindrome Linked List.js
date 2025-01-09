/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  let tmp = '';
  let cur = head;
  while (cur.next !== null) {
    tmp += cur.val.toString();
    cur = cur.next;
  }
  tmp += cur.val.toString();
  if (tmp === tmp.split('').reverse().join('')) {
    return true;
  } else {
    return false;
  }
};
