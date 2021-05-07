function permutations(vis,perms,list=[]){
    if (list.length == 3){
        let temp = []
        for (let i=0; i<3; i++){
            temp.push(Number(list[i]))
        }
        perms.push(temp)
        return
    }
    
    for (let i=0; i<3; i++){
        if (vis[i] == 0){
            vis[i] = 1
            permutations(vis,perms,list+[i])
            vis[i] = 0
        }
    }
}

function solution(expression) {
    var answer = 0;
    const pvis = Array(3).fill(0)
    const perms = []
    permutations(pvis, perms)
    const operand = []
    const numbers = []
    let temp = ''
    for (let i=0; i<expression.length; i++){
        let c = expression[i]
        if (c=='-' || c=='+' || c=='*'){
            if (temp) numbers.push(Number(temp));
            temp = ''
            operand.push(c)
        } else{
            temp += c
        }
    }
    let operands = ['-','+','*']
    if (temp) numbers.push(Number(temp))
    perms.forEach(perm=>{
        let total = []
        let stack = []
        total.push(numbers[0])
        for (let i=0; i<operand.length; i++){
            total.push(operand[i])
            total.push(numbers[i+1])
        }
        for (let i=0; i<3; i++){
            let calc = operands[perm[i]]
            let idx = 0
            while (idx<total.length){
                let item = total[idx++]
                if (item == calc){
                    let num1 = stack.pop()
                    let num2 = total[idx++]
                    if (calc == '-'){
                        stack.push(num1-num2)
                    } else if(calc =='*'){
                        stack.push(num1*num2)
                    } else {
                        stack.push(num1+num2)
                    }
                } else{
                    stack.push(item)
                }
            }
            total = []
            for (let i=0; i<stack.length; i++){
                total.push(stack[i])
            }
            stack = []
        }
        answer = Math.max(Math.abs(total[0]), answer)
    })
    
    return answer;
}