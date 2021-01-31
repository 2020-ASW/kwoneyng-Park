function solution(arr) {
    var answer = 1;
    let n = parseInt(arr.length/2) + 1
    console.log(n)
    const mndp = Array(n).fill(0)
    const mxdp = Array(n).fill(0)
    mndp.forEach((val,idx)=>{
        mndp[idx] = Array(n).fill(1/0)
        mxdp[idx] = Array(n).fill(-1/0)
    })
    for(let i=0; i<n; i++){
        mndp[i][i] = arr[i*2]*1
        mxdp[i][i] = arr[i*2]*1
    }
    const operator = []
    for (let i=0; i<arr.length; i++){
        if (arr[i] == '-' || arr[i] == '+'){
            operator.push(arr[i])
        }
    }
    
    for(let calc=0; calc<n; calc++){
        for (let x=0; x<n-calc; x++){
            let y = x+calc
            for (let k=0; k<y; k++){
                if (operator[k] == "-"){
                    mndp[x][y] = Math.min(mndp[x][k] - mxdp[k+1][y], mndp[x][y])
                    mxdp[x][y] = Math.max(mxdp[x][k] - mndp[k+1][y], mxdp[x][y])
                } else{
                    mndp[x][y] = Math.min(mndp[x][k] + mndp[k+1][y],mndp[x][y])
                    mxdp[x][y] = Math.max(mxdp[x][k] + mxdp[k+1][y], mxdp[x][y])
                }    
            }
        }
    }
    
    return mxdp[0][n-1];
}