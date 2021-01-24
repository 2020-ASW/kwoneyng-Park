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
var answer

function dfs(cur){
    let lsum,rsum,m
    if (cur == null) return 0
    lsum = dfs(cur.left)
    rsum = dfs(cur.right)
    m = cur.val
    if (lsum>0) m += lsum
    if (rsum>0) m += rsum
    if (m > answer) answer = m
    
    let add = Math.max(lsum, rsum, 0)
    cur.val += add
    if (cur.val > answer) answer = cur.val
    return cur.val
}

var maxPathSum = function(root) {
    answer = -1/0
    dfs(root)
    return answer
};