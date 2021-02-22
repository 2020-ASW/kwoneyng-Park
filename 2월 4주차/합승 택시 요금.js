function solution(n, s, a, b, fares) {
    const arr = Array(n)
    for (let i=0; i<n; i++){
        arr[i] = Array(n).fill(1/0)
    }
    
    for (let i=0; i<n; i++){
        arr[i][i] = 0
    }
    
    fares.forEach(([a,b,c])=>{
        arr[a-1][b-1] = Math.min(arr[a-1][b-1], c)
        arr[b-1][a-1] = Math.min(arr[b-1][a-1], c)
    })
    
    for (let k=0; k<n; k++){
        for (let x=0; x<n; x++){
            for (let y=0; y<n; y++){
                arr[x][y] = Math.min(arr[x][y], arr[x][k] + arr[k][y])
            }
        }
    }
    let ans = 1/0
    s -= 1
    a -= 1
    b -= 1
    for (let k=0; k<n; k++){
        ans = Math.min(ans, arr[a][k] + arr[b][k] + arr[s][k])
    }
    
    return ans
    // arr.forEach(row=>{
    //     console.log(row)
    // })
    
}