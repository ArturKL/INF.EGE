f = open('27-A.txt', 'r')
n = int(f.readline())
nums = sorted([[i, int(f.readline())] for i in range(n)], key=lambda x: x[1], reverse=True)
print(nums[:100])
