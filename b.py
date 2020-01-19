input_ab = input().split(' ')
a = int(input_ab[0])
b = int(input_ab[1])

ab = ""
ba = ""

for i in range(b+1):
  ab = ab + input_ab[0]

for i in range(a+1):
  ba = ba + input_ab[1]

dic = [ab, ba]
sdic = sorted(dic)

print(sdic[0])
