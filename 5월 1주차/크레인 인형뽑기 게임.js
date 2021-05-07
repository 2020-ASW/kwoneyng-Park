function solution(board, moves) {
    var answer = 0;
    const stack = Array()
    moves.forEach(y=>{
        y--
        for (let x=0; x<board.length; x++){
            if (board[x][y]){
                let pick = board[x][y]
                board[x][y] = 0
                if (stack && stack[stack.length-1] == pick){
                    stack.pop()
                    answer += 2
                } else{
                    stack.push(pick)
                }
                break;
            }
        }
    })
    return answer;
}