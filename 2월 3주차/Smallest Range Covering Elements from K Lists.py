class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def binaryInput(row, val, arr):
            if not arr:
                arr.append([val,row])
                return
            l,r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if val > arr[m][0]:
                    l = m+1
                else:
                    r = m-1
            if l > len(arr):
                arr.append([val,row])
            else:
                arr.insert(l,[val,row])
        
        arr = []
        for i in range(len(nums)):
            for j in nums[i]:
                binaryInput(i,j,arr)
                
        cntGroup = [0]*len(nums)
        cnt = 0
        
        l = 0
        length = 1e9
        ans = []
        for r in range(len(arr)):
            if cntGroup[arr[r][1]] == 0:
                cnt += 1
            cntGroup[arr[r][1]] += 1
            if cnt == len(nums):
                while True:
                    if cntGroup[arr[l][1]] > 1:
                        cntGroup[arr[l][1]] -= 1
                        l += 1
                    else:
                        calc = arr[r][0] - arr[l][0]
                        if length > calc:
                            length = calc
                            ans = [arr[l][0],arr[r][0]]
                        break
        return ans
        