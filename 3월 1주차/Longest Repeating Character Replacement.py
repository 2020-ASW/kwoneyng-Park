class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = [0]*26
        ans = 0
        total = 0
        left = 0
        for i in range(len(s)):
            total += 1
            alpha[ord(s[i])-ord('A')] += 1
            if total - max(alpha) > k:
                ans = max(ans, i-left)
                while left < i:
                    total -= 1
                    alpha[ord(s[left])-ord('A')] -= 1
                    left += 1
                    if total - max(alpha) <= k:
                        break
        print(left)
        ans = max(ans, len(s)-left)
        return ans