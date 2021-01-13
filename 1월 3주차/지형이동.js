var land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
var height = 3
var n = land.length
var answer = 0;
var marking = Array(n).fill(0)
for(var i=0; i<n;i++){
    marking[i] = Array(n).fill(0)
}
var dx,dy,q,ht,cnt,cur,x,y,xi,yi
ht = new Map()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

for (var i=0; i<n; i++){
    for (var j=0; j<n; j++){
        if (marking[i][j] == 0){
            cnt += 1
            q = [[i,j]]
            while (q.length){
                cur = q.shift()
                x = cur[0]; y = cur[1];
                marking[x][y] = cnt
                for (var k=0; k<4; k++){
                    xi = x+dx[k]; yi = y+dy[k]
                    if (xi >= 0 && xi < n && yi >= 0 && yi < n){
                        if (marking[xi][yi] == 0){
                            if (Math.abs(land[xi][yi] - land[x][y]) <= height){
                                q.push([xi,yi])
                            }
                        } else if (marking[xi][yi] != marking[x][y]){
                            var a,b
                            a = marking[xi][yi]
                            b = marking[x][y]
                            if (a>b){
                                [a,b] = [b,a]
                            }
                            if (ht.get((a,b))){
                                ht[(a,b)] = Math.min(Math.abs(land[x][y] - land[xi][yi]), ht[(a,b)])
                            } else{
                                ht.set((a,b), Math.abs(land[x][y]-land[xi][yi]))
                            }
                        }
                    }
                }
            }
        }
    }
}


console.log(marking)
ht.forEach((value,key)=>{
    console.log(value, key)
})