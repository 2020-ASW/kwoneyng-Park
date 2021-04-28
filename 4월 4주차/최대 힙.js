class Heap{
    arr = [null];
    push(x){
        let n = this.arr.length;
        this.arr.push(x);
        while (n > 1 && this.arr[parseInt(n/2)] < x){
            this.arr[n] = this.arr[parseInt(n/2)];
            this.arr[parseInt(n/2)] = x
            n = parseInt(n/2);
        }
    }
    pop(){
        if (this.arr.length < 2){
            return 0;
        }
        let ans = this.arr[1];
        this.arr[1] = this.arr[this.arr.length-1];
        this.arr.pop()
        let cur = 1;
        let n = this.arr.length;
        let val = this.arr[1];
        while (cur*2 < n){
            let left = cur*2;
            let right = cur*2+1;
            let max = this.arr[left];
            let maxcur = left;
            if (right < n && max < this.arr[right]){
                max = this.arr[right]
                maxcur = right
            }
            if (this.arr[cur] > max){
                break;
            }
            this.arr[cur] = this.arr[maxcur]
            this.arr[maxcur] = val
            cur = maxcur
        }
        return ans;
    }
}

var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let n = Number(input[0])
input.shift()
const hq = new Heap()
let ans = ''
for(let i=0; i<input.length; i++){
    let su = Number(input[i]);
    if (su === 0){
        ans += hq.pop() + "\n"
    }
    else {
        hq.push(su);
    }
}
console.log(ans)