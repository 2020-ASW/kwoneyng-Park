n = int(input())
nums = []
for i in range(n):
    nums.append(float(input()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i]*nums[i-1])

print(nums)
print(round(max(nums), 3))