var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let IN = 0

const dx = [-1,0,0,1]
const dy = [0,-1,1,0]
let n,m,k
[n,m,k] = input[IN++].split(' ').map(x=>Number(x))
const arr = []
for (let i=0; i<n; i++){
    arr.push(input[IN++].split(' ').map(x=>Number(x)))
}