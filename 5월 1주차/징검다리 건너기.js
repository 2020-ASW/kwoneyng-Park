function check(stones,m,k){
    let cnt = 0;
    for (let i=0; i<stones.length; i++){
        if (stones[i] >= m) cnt = 0
        else cnt++
        if (cnt>=k) return false
    }
    return true
}

function solution(stones, k) {
    var answer = 0;
    let l=0, r=200000000;
    while (l<=r){
        let m = Math.floor((l+r)/2);
        if(check(stones,m,k)){
            l = m+1
        } else{
            r = m-1
        }
    }
    
    return r;
}