f = open("data.txt")

lines = f.read().split('\n')


dictionary = {}
for line in range(len(lines)):
  length = 0
  for char in range(len(lines[line])):
    if (length != 0):
      length -= 1
      continue
    if (lines[line][char].isnumeric()):
      x = 0
      while (char + x < len(lines[line]) and lines[line][char + x].isnumeric()):
        x += 1
      for i in range(0, x):
        dictionary[(line * len(lines[line]) + char + i)] = [int(lines[line][char:char + x]), (line * len(lines[line]) + char)]
      length = x
sum = 0
keys = dictionary.keys()
for line in range(len(lines)):
  for char in range(len(lines[line])):
    if (lines[line][char] == '*'):
      three = False
      num1 = -1
      num2 = -1
      for i in range(-1,2):
        for j in range(-1,2):
          if ((line + i) * len(lines[line]) + (char + j) in keys and (num1 == -1 or num2 == -1)):
            # print((line + i) * len(lines[line]) + (char + j))
            if (num1 == -1):
              num1 = dictionary[(line + i) * len(lines[line]) + (char + j)]
            elif (dictionary[(line + i) * len(lines[line]) + (char + j)][1] == num1[1]):
              continue
            elif (num2 == -1):
              num2 = dictionary[(line + i) * len(lines[line]) + (char + j)]
            else:
              three = True
      if (num1 != -1 and num2 != -1 and not three):
        # print(str(num1[0]) + " and " + str(num2[0]))
        sum += num1[0] * num2[0]
# print(dictionary)
print(sum)
