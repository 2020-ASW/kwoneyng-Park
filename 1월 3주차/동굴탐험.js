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
    var q = [0]
    var cur
    while (q.length){
        cur = q.shift()
        narr[cur].forEach(nxt=>{
            if (indegree[nxt] > 0){
                indegree[nxt] -= 1
                if (indegree[nxt] == 0){
                    cnt -= 1
                    q.push(nxt)
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