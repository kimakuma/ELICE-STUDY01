arr = []

name_num = int(input())

for i in range(name_num):
  index = 0

  name = input()

  for k in name:
    if k.isupper(): index += 1

    if index == 2: 
      index = name.index(k)
      break

  arr.append(name[index:])

for name in arr:
  print(name)
