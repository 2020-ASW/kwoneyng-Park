/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    const arr = []
    matrix.forEach(mat=>{
        mat.forEach(val=>{
            arr.push(val)
        })
    })
    arr.sort((a,b)=>{
        return a-b
    })
    
    return arr[k-1]
};