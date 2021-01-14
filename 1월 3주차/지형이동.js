function find(x,parent){
    if (parent[x] == x) return x
    parent[x] = find(parent[x], parent)
    return parent[x]
}

function merge(parent,ladder){
    var ans = 0
    var v,x,y,px,py
    ladder.forEach((iter)=>{
        [v,x,y] = iter
        px = find(x,parent)
        py = find(y,parent)
        if (px != py){
            parent[py] = px
            ans += v
        }
    })
    
    return ans
}

function solution(land, height) {
    var n = land.length
    var marking = Array(n).fill(0)
    for (var i=0; i<n; i++){
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
                marking[i][j] = cnt
                while (q.length){
                    cur = q.shift()
                    x = cur[0]; y = cur[1];
                    for (var p=0; p<4; p++){
                        xi = x+dx[p]; yi = y+dy[p];
                        if (xi>=0 && xi<n && yi>=0 && yi<n){
                            if (marking[xi][yi] == 0){
                                if (Math.abs(land[xi][yi] - land[x][y]) <= height){
                                    q.push([xi,yi])
                                    marking[xi][yi] = cnt
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    var a,b,dh
    for (var x=0; x<n; x++){
        for (var y=0; y<n; y++){
            for (var k=0; k<4; k++){
                xi = x+dx[k]; yi = y+dy[k];
                if (xi<n && xi>=0 && yi<n && yi>= 0 && marking[xi][yi] != marking[x][y]){
                    a = marking[xi][yi]
                    b = marking[x][y]
                    dh = Math.abs(land[xi][yi] - land[x][y])
                    if (a>b){
                        [a,b] = [b,a]
                    }
                    if (a in ht){
                        if (b in ht[a]){
                            ht[a][b] = Math.min(ht[a][b], dh)
                        } else{
                            ht[a][b] = dh
                        }
                    } else{
                        ht[a] = {}
                        ht[a][b] = dh
                    }
                }
            }
        }
    }
    var ladder = []
    Object.keys(ht).forEach((x)=>{
        Object.keys(ht[x]).forEach((y)=>{
            ladder.push([ht[x][y], x, y])
        })  
    })
    ladder = ladder.sort((a,b)=>{
        return a[0] - b[0]
    })
    
    var parent = []
    for (var i=0; i<cnt; i++){
        parent.push(i)
    }
    // return ht
    return merge(parent,ladder)
    
}