function solution(food_times, k) {
    var total = 0
    var n = food_times.length
    food_times.forEach((item)=>{
        total += item
    })
    if (k >= total) return -1
    
    food_times = food_times.map((x,idx)=>{
        return [idx,x]
    })
    
    food_times.sort((a,b)=>{
        return a[1] - b[1]
    })
    var idx,val,cycle,start
    cycle = 0
    start = 0
    while (food_times.length){
        [idx, val] = food_times[start]
        if ((val-cycle)*n <= k){
            k -= (val-cycle)*n
            cycle = val
            n -= 1
            start += 1
        } else break
    }
    food_times.splice(0,start)
    food_times.sort((a,b)=>{
            return a[0] - b[0]
    })
    return food_times[k%n][0] + 1
}