function union(x,y){
    let px = find(x)
    let py = find(y)
    if (px != py){
        let mn = Math.min(cost[px],cost[py])
        parent[py] = px
        cost[px] = mn
        cost[py] = mn
    }

}

function find(x){
    if (parent[x] == x){
        return x
    }
    parent[x] = find(parent[x])
    return parent[x]
}

var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let IN = 0;
let n,m,k;

[n,m,k] = input[IN++].split(' ').map(x=>Number(x));
const arr = input[IN++].split(' ').map(x=>Number(x));
// let n,m,k
// [n,m,k] = [5,3,20]
// const arr = [10,10,20,20,30]
// const input = ['1 3','2 4','5 4']
// let IN = 0
const parent = Array(n+1).fill(0)
const cost = Array(n+1).fill(1/0)
for (let i=1; i<n+1; i++){
    parent[i] = i
    cost[i] = arr[i-1]
}
let v,w;
for (let i=0; i<m; i++){
    [v,w] = input[IN++].split(' ').map(x=>Number(x));
    union(v,w)
}

let answer = 0;
for (let i=1; i<n+1; i++){
    let px = find(i)
    if (px != 0){
        answer += cost[px]
        union(0,px)
    }
}
if (answer <= k){
    console.log(answer)
}else{
    console.log('Oh no')
}