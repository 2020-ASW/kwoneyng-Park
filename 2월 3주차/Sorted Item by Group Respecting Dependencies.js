/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function(n, m, group, beforeItems) {
    const ans = []
    const narr = Array(n)
    const groupContain = {}
    const vis = Array(n).fill(0)
    for (let i=0; i<n; i++){
        narr[i] = []
        if (group[i] == -1){
            group[i] = m
            m += 1
        }
        if (groupContain[group[i]]){
            groupContain[group[i]].push(i)
        } else{
            groupContain[group[i]] = []
            groupContain[group[i]].push(i)
        }
    }
    const groupIndegree = Array(m).fill(0)
    const indegree = Array(n).fill(0)
    
    
    beforeItems.forEach((arr,nxt)=>{
        let ngroup = group[nxt]
        arr.forEach(cur=>{
            let cgroup = group[cur]
            narr[cur].push(nxt)
            if (ngroup == cgroup){
                indegree[nxt] += 1
            } else{
                groupIndegree[ngroup] += 1
            }
        })
    })
    
    const groupQueue = []
    groupIndegree.forEach((val,idx)=>{
        if (val == 0){
            groupQueue.push(idx)
        }
    })
    while (groupQueue.length){
        let curGroup = groupQueue.shift()
        let groupItems = groupContain[curGroup]
        console.log(curGroup, groupItems)
        if (!groupItems) continue
        let queue = []
        groupItems.forEach(val=>{
            if (indegree[val] == 0){
                queue.push(val)
            }
        })
        
        while (queue.length){
            let cur = queue.shift()
            if (vis[cur] == 0){
                ans.push(cur)
                vis[cur] = 1
            }
            let cgroup = group[cur]
            narr[cur].forEach(val=>{
                let ngroup = group[val]
                if (cgroup == ngroup){
                    if (indegree[val] == 1){
                        indegree[val] = 0
                        queue.push(val)
                    } else if(indegree[val] > 0){
                        indegree[val] -= 1
                    }
                } else{
                    if (groupIndegree[ngroup] == 1){
                        groupIndegree[ngroup] = 0
                        groupQueue.push(ngroup)
                    } else if (groupIndegree[ngroup] > 0){
                        groupIndegree[ngroup] -= 1
                    }
                }
            })
        }
    }
    if (ans.length == n){
        return ans
    } else{
        return []
    }
    
};