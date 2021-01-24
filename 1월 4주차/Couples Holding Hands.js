/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function(row) {
    let n = row.length
    let ans = 0
    for (let i=0; i<n; i++){
        row[i] = parseInt(row[i]/2)
    }
    
    let cur, coup
    for (let i=0; i<n; i+=2){
        cur = row[i]
        for (let j=i+1; j<n; j++){
            if (cur == row[j]){
                coup = j
                break
            }
        }
        if (coup != i+1){
            ans += 1
            row[coup] = row[i+1]
        }
    }
    return ans
    
};