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
var minDepth = function (root) {
  if (root === null) return 0;

  const dfs = (node) => {
    if (node.left === null && node.right === null) {
      return 1;
    }
    let leftDepth = node.left !== null ? dfs(node.left) : Infinity;
    let rightDepth = node.right !== null ? dfs(node.right) : Infinity;

    return Math.min(leftDepth, rightDepth) + 1;
  };

  let res = dfs(root);
  return res;
};
