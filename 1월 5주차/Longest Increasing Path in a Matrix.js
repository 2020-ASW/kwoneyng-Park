/**
 * @param {number[][]} matrix
 * @return {number}
 */


var ans
const dx = [-1,0,1,0]
const dy = [0,1,0,-1]

function find(arr,dp,x,y){
    dp[x][y] = 1
    for (let d=0; d<4; d++){
        xi = x+dx[d]
        yi = y+dy[d]
        if (0<=xi && xi<arr.length && 0<=yi && yi<arr[0].length && arr[x][y] < arr[xi][yi]){
            if (dp[xi][yi] > 0){
                dp[x][y] = Math.max(dp[xi][yi]+1,dp[x][y])
            } else{
                dp[x][y] = Math.max(find(arr,dp,xi,yi)+1, dp[x][y])
            }
        }
    }
    ans = Math.max(dp[x][y],ans)
    return dp[x][y]
}


var longestIncreasingPath = function(matrix) {
    ans = 0
    const dp = Array(matrix.length)
    for (let x=0; x<matrix.length; x++){
        dp[x] = Array(matrix.length).fill(0)
    }
    
    for (let x=0; x<matrix.length; x++){
        for (let y=0; y<matrix[0].length; y++){
            find(matrix,dp,x,y)
        }
    }
    return ans
};