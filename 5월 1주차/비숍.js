function dfs(grad, c, vis, gradient, rs=0){
    ans[c] = Math.max(ans[c], rs)
    for (let i=grad; i<n*2; i+=2){
        if (!gradient[i]) continue;
        for (let j=0; j<gradient[i].length; j++){
            let x,y;
            // debugger;
            [x,y] = gradient[i][j]
            if (vis[x+y] == 0){
                vis[x+y] = 1
                dfs(i+2, c, vis, gradient, rs+1)
                vis[x+y] = 0
            }
        }
    }
}

var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let IN = 0
let n = input[IN++]
const arr = Array(n)
for (let i=0; i<n; i++){
    arr[i] = input[IN++].split(' ').map(x=>parseInt(x))
}

// let n = 5
// const arr = [[1,1,0,1,1],[0,1,0,0,0],[1,0,1,0,1],[1,0,0,0,0],[1,0,1,1,1]]
const vis = Array(2*n).fill(0)
const gradient = {}
for (let x=0; x<n; x++){
    for (let y=0; y<n; y++){
        if (arr[x][y] == 0) continue;
        if (!gradient[n+x-y]) gradient[n+x-y] = Array();
        gradient[n+x-y].push([x,y])
    }
}
var ans = Array(2).fill(0)
dfs(0,0,vis, gradient)
dfs(1,1,vis, gradient)

console.log(ans[0]+ans[1])
