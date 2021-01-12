function go(m,n,rocks){
    var l = rocks.length
    var cur = 0
    for (var i=0; i<l; i++){
        if (rocks[i]-cur < m){
            n -= 1
            if (n < 0){
                return false
            }
        } else{
            cur = rocks[i]
        }
    }
    return true
}

function solution(distance, rocks, n) {
    rocks.sort((a,b)=>{
        return a-b
    })
    
    var l,r,m
    l = 0
    r = distance
    while (l<=r){
        m = parseInt((l+r)/2)
        if (go(m,n,rocks)){
            l = m+1
        } else {
            r = m-1
        }
    }
    
    return r;
}