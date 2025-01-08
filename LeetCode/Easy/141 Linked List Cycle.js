/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let visited = new Set();
  let cur = head;

  while (cur !== null) {
    if (visited.has(cur)) {
      return true;
    }
    visited.add(cur);
    cur = cur.next;
  }

  return false;
};
