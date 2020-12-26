nums1 = [1,3]
nums2 = [2]

ht = {}

for i in nums1:
    if not ht.get(i):
        ht[i] = 1

for i in nums2:
    if not ht.get(i):
        ht[i] = 1

arr = []
for key,val in ht.items():
    arr.append(key)

arr.sort()
n = len(arr)
if n%2 == 0:
    print((arr[n//2]+arr[n//2-1])/2)
else:
    print(arr[n//2])