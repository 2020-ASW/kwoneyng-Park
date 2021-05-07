function solution(n, stations, w) {
    var answer = 0;
    let left = 0
    stations.forEach(idx=>{
        let cover = idx-w-1-left;
        answer += Math.ceil(cover/(2*w+1))
        left = idx+w
    })
    if (left < n){
        let cover = n-left
        answer += Math.ceil(cover/(2*w+1))
    }
    

    return answer;
}