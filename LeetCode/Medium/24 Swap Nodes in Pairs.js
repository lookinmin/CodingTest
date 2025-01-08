/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
  const dummy = new ListNode(0, head);
  let prev = dummy;

  while (prev.next !== null && prev.next.next !== null) {
    // 다음 노드와 다다음 노드가 모두 존재한다면
    let first = prev.next;
    let second = prev.next.next;

    first.next = second.next;
    second.next = first;
    // 다음과 다다음의 노드 위치 교환

    prev.next = second;
    // prev(현재)의 다음을 second로 지정
    prev = first;
    // 다다음노드를 현재로 최신화
  }

  return dummy.next;
  // head를 리턴
};
