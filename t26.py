f = open('26.txt', 'r')
s, n = map(int, f.readline().split())
nums = sorted([int(i) for i in f.readlines()])
print(s)
print(sum(nums[:567]) + 50)
print(nums)
ans = 0
res = 0
for i in range(n):
    if s - nums[i] < 0:
        s += nums[i - 1]
        break
    else:
        s -= nums[i]
        ans += 1
for j in range(i, n):
    if s - nums[j] < 0:
        res = nums[j - 1]
print(ans, res)