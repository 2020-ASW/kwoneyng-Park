function solution(a) {
    var answer = 2;
    var n = a.length
    if (n < 2) return n
    var lm = Array(n).fill(9999999999)
    var rm = Array(n).fill(9999999999)
    lm[0] = a[0]
    rm[n-1] = a[n-1]
    for (var i=1; i<n; i++){
        lm[i] = Math.min(a[i],lm[i-1])
    }
    for (var i=n-2; i>=0; i--){
        rm[i] = Math.min(a[i],rm[i+1])
    }
    for (var i=1; i<n-1; i++){
        if (rm[i] == a[i] || lm[i] == a[i]) answer += 1
    }
    
    
    return answer;
}