function solution(name) {
    var answer = 0;
    const n = name.length
    const A = 'A'.charCodeAt(0)
    const Z = 'Z'.charCodeAt(0)
    for (let i=0; i<n; i++){
        let ascii = name.charCodeAt(i)
        answer += Math.min(Math.abs(ascii-A), Math.abs(Z-ascii)+1)
    }
    
    const vis = Array(n).fill(0)
    let cnt = 0
    for (let i=1; i<n; i++){
        if (name.charCodeAt(i) == A) {
            vis[i] = 1;
        } else cnt++;
    }
    let frontord = 0
    let pointer = 0
    while (cnt){
        for (let dist=1; dist<n; dist++){
            let front = pointer+dist
            let back = pointer-dist
            if (front >= n) front-=n;
            if (back < 0) back+=n;
            if (A != name.charCodeAt(front) && vis[front] == 0){
                frontord += dist
                vis[front] = 1
                cnt--
                pointer = front
                break
            }
            if (A != name.charCodeAt(back) && vis[back] == 0){
                frontord += dist
                vis[back] = 1
                cnt--
                pointer = back
                break
            }
        }
    }
    
    for (let i=1; i<n; i++){
        if (name.charCodeAt(i) != A) {
            vis[i] = 0;
            cnt++
        }
    }
    let backord = 0
    pointer = 0
    while (cnt){
        for (let dist=1; dist<n; dist++){
            let front = pointer+dist
            let back = pointer-dist
            if (front >= n) front-=n;
            if (back < 0) back+=n;
            if (A != name.charCodeAt(back) && vis[back] == 0){
                backord += dist
                vis[back] = 1
                cnt--
                pointer = back
                break
            }
            if (A != name.charCodeAt(front) && vis[front] == 0){
                backord += dist
                vis[front] = 1
                cnt--
                pointer = front
                break
            }
        }
    }
    
    
    
    return answer+Math.min(frontord,backord);
}