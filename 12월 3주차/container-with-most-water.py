class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        ans = min(height[l], height[r])*(n-1)
        while l <= r:
            dh = min(height[l],height[r])
            maxA = dh*(r-l)
            if ans < maxA:
                ans = maxA
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans

# 헷갈렷던 점

# 가장 큰 벽을 두개 찾아서 계산했더니 컨테이너 안의 물이 최대값에 도달하지 못했다.