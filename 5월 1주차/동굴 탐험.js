class Queue{
    head = null
    tail = null
    push(x){
        if (!this.head){
            this.head = new Node(x)
            this.tail = this.head
        } else{
            this.tail.nxt = new Node(x)
            this.tail = this.tail.nxt
        }
    }
    pop(){
        if (this.head){
            let rs = this.head.val
            this.head = this.head.nxt
            return rs
        }
    }
    empty(){
        if (this.head) return false
        else return true
    }
}

class Node{
    constructor(val){
        this.val = val
        this.nxt = null
    }
}

function solution(n, path, order) {
    var cnt = n-1
    var narr = Array.from({length:n},()=>[])
    var indegree = Array.from({length:n}, ()=>1)
    path.forEach(([a,b])=>{
        narr[a].push(b)
        narr[b].push(a)
    })
    indegree[0] = 0
    order.forEach(([a,b])=>{
        narr[a].push(b)
        indegree[b] += 1
    })
    if (indegree[0]){
        return false
    }
    const queue = new Queue()
    queue.push(0)
    while (!queue.empty()){
        let cur = queue.pop()
        narr[cur].forEach(nxt=>{
            if (indegree[nxt] > 0){
                indegree[nxt] -= 1
                if (indegree[nxt] == 0){
                    cnt -= 1
                    queue.push(nxt)
                }
            }
        })
    }
    
    if (cnt>0){
        return false
    } else{
        return true
    }
}