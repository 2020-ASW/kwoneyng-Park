function solution(numbers, hand) {
    var answer = '';
    const keypad = {}
    for (let i=0; i<3; i++){
        for (let j=0; j<3; j++){
            keypad[i*3+j+1] = [i,j]
        }
    }
    keypad[0] = [3,1]
    let lh = [3,0]
    let rh = [3,2]
    numbers.forEach(v=>{
        if (v % 3 == 1){
            lh = keypad[v]
            answer += 'L'
        } else if (v % 3 == 0 && v){
            rh = keypad[v]
            answer += 'R'
        } else{
            let tx,ty
            [tx,ty] = keypad[v]
            let ld,rd
            ld = Math.abs(tx-lh[0]) + Math.abs(ty-lh[1])
            rd = Math.abs(tx-rh[0]) + Math.abs(ty-rh[1])
            if (ld < rd){
                answer += 'L'
                lh = keypad[v]
            } else if (ld > rd){
                answer += 'R'
                rh = keypad[v]
            } else if (hand == 'left'){
                answer += 'L'
                lh = keypad[v]
            } else{
                answer += 'R'
                rh = keypad[v]
            }
        }
    })
    
    
    
    return answer;
}