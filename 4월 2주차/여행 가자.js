const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')
//const input = ['3','3','0 1 0','1 0 1','0 1 0','1 2 3']

function find(x,root){
    if (root[x] != x){
        root[x] = find(root[x],root)
    }
    return root[x]
}

function union(x,y,root){
    let px = find(x,root)
    let py = find(y,root)
    root[py] = px
    
}


const n = parseInt(input.shift())
const m = parseInt(input.shift())
const arr = []
for (let i=0; i<n; i++){
    arr.push(input.shift().split(' '))
}
let order = input.shift().split(' ')

let root = Array(n).fill(0)
for (let i=0; i<n; i++){
    root[i] = i
}
for (let i=0; i<n; i++){
    for (let j=0; j<n; j++){
        if (arr[i][j] == '1'){
            union(i,j,root)
        }
    }
}

let ans = 'YES'
order = order.map((v)=>parseInt(v,10)-1).map((v)=> find(v,root))
console.log(order.every((v)=> v===order[0]) ? 'YES':'NO')
