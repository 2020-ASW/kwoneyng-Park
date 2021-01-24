function find(x,parent){
    if (parent[x] == x) return x
    parent[x] = find(parent[x],parent)
    return parent[x]
}

function merge(a,b,v,parent,spend){
    if (a > b) [a,b] = [b,a]
    let ans = 0
    let flag = 0
    let pa,pb
    pa = find(a,parent)
    pb = find(b,parent)
    if (pa != pb){
        parent[pb] = pa
        spend[pb] = v
    }
}

function solution(n, costs) {
    var answer = 0;
    let parent = []
    for (let i=0; i<n; i++){
        parent.push(i)
    }
    costs.sort((a,b)=>{
        return a[2]-b[2]
    })
    let spend = Array(n).fill(0)
    costs.forEach(([a,b,v])=>{
        merge(a,b,v,parent,spend)
    })
    spend.forEach((x)=>{
        answer += x
    })
    return answer;
}