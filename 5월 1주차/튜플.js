function solution(s) {
    var answer = [];
    const arr = [];
    let temp = ''
    for (let i=1; i<s.length-1; i++){
        let c = s[i];
        if (c == '{'){
            temp = '';
        } else if (c == '}'){
            if (temp){
                arr.push(temp.split(',').map(Number))
                temp = ''
            }
        } else{
            temp += c
        }
    }
    arr.sort((a,b)=>{
        return a.length - b.length;
    })
    const vis = Array(100000).fill(0)
    arr.forEach(list=>{
        list.forEach(v=>{
            if (vis[v] == 0){
                answer.push(v)
                vis[v] = 1
            }
        })
    })
    return answer;
}