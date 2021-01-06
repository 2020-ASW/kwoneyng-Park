from math import sqrt
import sys
sys.setrecursionlimit(30000)

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        sq = sqrt(n)
        self.nums = nums
        if sq > int(sq):
            self.flr = int(sq)+1
        else: self.flr = int(sq)
        
        self.seg = [0]*(2**self.flr)
        for i in range(n):
            self.seg[2**(self.flr-1)+i//2] += nums[i]
            
        for i in range(self.flr-2,-1,-1):
            for j in range(2**i, 2**(i+1)):
                self.seg[j] = self.seg[j*2] + self.seg[j*2+1]
                
        
    def update(self, i: int, val: int) -> None:
        temp = self.nums[i]
        self.nums[i] = val
        self.seg[2**(self.flr-1)+i//2] += (val-temp)
        
        start = 2**(self.flr-1) + i//2
        while start > 1:
            start //= 2
            self.seg[start] = self.seg[start*2] + self.seg[start*2+1]
            
            

    def sumRange(self, i: int, j: int) -> int:
        def calc(i,j,rs):
            print(i,j,rs)
            if i == j:
                return rs + self.seg[i]
            if i%2 == 1:
                return calc(i+1,j,rs+self.seg[i])
            elif j%2 == 0:
                return calc(i,j-1,rs+self.seg[j])
            else:
                return calc(i//2, j//2, rs)
        print('start sum Range')
        print(i,j)
        ans = 0
        if i == j:
            return self.nums[i]
        
        if i % 2 == 1:
            ans += self.nums[i]
            i+=1
        if j % 2 == 0:
            ans += self.nums[j]
            j -= 1
        if i <= j:
            print('process calc',i,j,ans)
            return calc((i+2**self.flr)//2, (j+2**self.flr)//2, ans)
        return ans
        