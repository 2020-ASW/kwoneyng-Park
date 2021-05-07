function solution(A, B) {
    var answer = 0;
    const n = A.length
    A.sort((a,b)=>{
        return b-a
    })
    B.sort((a,b)=>{
        return b-a
    })
    let a=0,b=0
    while (a<n){
        if (A[a] < B[b]){
            a++;b++;answer++;
        } else{
            a++;
        }
    }
    
    return answer;
}