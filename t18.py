f = open('01.in.txt', 'r')
nums = [float(i[:-1].replace(',', '.')) for i in f.readlines()]
c = 0
maxx = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        c += nums[i - 1]
    else:
        c += nums[i - 1]
        if c > maxx:
            maxx = c
        c = 0
print(maxx)
