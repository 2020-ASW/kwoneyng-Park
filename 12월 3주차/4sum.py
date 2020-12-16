class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-3):
            for j in range(i+1,n-2):
                tsum = nums[i]+nums[j]
                l,r = j+1, n-1
                while l < r:
                    if tsum+nums[l]+nums[r] < target:
                        l += 1
                    elif tsum+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        ap = [nums[i], nums[j], nums[l], nums[r]]
                        if ap not in ans:
                            ans.append(ap)
                        l += 1
                        r -= 1
                            
        return ans