import sys
sys.setrecursionlimit
nums = []
target = 0
vis = [0]*len(nums)
ans = []
def calc(idx,rs,vis,cnt=0):
    if cnt == 4:
        if rs == target:
            s = []
            for i,v in enumerate(vis):
                if v == 1:
                    s.append(nums[i])
            s.sort()
            if s not in ans:
                ans.append(s)
            return
    elif idx <= len(nums):
        vis[idx] = 1
        calc(idx+1,rs+nums[idx],vis,cnt+1)
        vis[idx] = 0
        if len(vis) - idx + cnt > 4:
            calc(idx+1, rs, vis, cnt)
calc(0,0,vis)
print(ans)