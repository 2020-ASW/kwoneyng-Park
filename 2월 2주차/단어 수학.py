n = int(input())

alpha = [0]*26

for _ in range(n):
    num = input()
    num = num[::-1]
    mul = 1
    for i in num:
        alpha[ord(i)-ord('A')] += mul
        mul *= 10

alpha.sort(reverse=True)
ans = 0
mul = 9
for i in alpha:
    ans += mul*i
    mul -= 1

print(ans)
