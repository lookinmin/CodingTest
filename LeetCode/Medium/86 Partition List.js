/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
  let dummy = new ListNode(0);
  let tmp = new ListNode(0);

  let less = dummy;
  let greater = tmp;
  let cur = head;

  while (cur) {
    if (cur.val < x) {
      less.next = cur;
      less = less.next;
    } else {
      greater.next = cur;
      greater = greater.next;
    }
    cur = cur.next;
  }
  greater.next = null;
  less.next = tmp.next;
  return dummy.next;
};
