def alg(i):
 s = i
 n = 2
 while s < 37:
  s = s + 3
  n = n * 2
 return n


print(alg(18))
print(alg(19))

for i in range(-1000, 1000):
 if alg(i) == 128:
  print(i)
  exit()

