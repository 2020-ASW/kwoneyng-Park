class FreqStack {
    constructor(){
        this.stack = {}
        // 수 : 횟수
        this.maxFreq = 0
        this.freq = {}
        // 횟수 : 리스트
    }
    
    push(x){
        let curFreq
        if (!this.stack[x]) this.stack[x] = 1
        else this.stack[x] += 1
        curFreq = this.stack[x]
        this.maxFreq = Math.max(curFreq, this.maxFreq)
        if (this.freq[curFreq]) this.freq[curFreq].push(x)
        else {
            this.freq[curFreq] = []
            this.freq[curFreq].push(x)
        }
        // console.log(curFreq, this.freq[curFreq])
    }
        
    pop(){
        // console.log(this.maxFreq)
        if (this.freq[this.maxFreq].length == 0) this.maxFreq -= 1
        let ans = this.freq[this.maxFreq].pop()
        this.stack[ans] -= 1
        return ans
    }
}
