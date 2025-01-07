/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumOfLeftLeaves = function (root) {
  const dfs = (root, isLeft) => {
    if (root === null) return 0;
    if (!root.left && !root.right && isLeft) return root.val;
    // 내가 마지막
    return dfs(root.left, true) + dfs(root.right, false);
  };
  return dfs(root, false);
};
