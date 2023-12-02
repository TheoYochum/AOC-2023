import re
f = open("data.txt")

text = f.read()

text = text.replace('red', '0').replace('green', '1').replace('blue', '2').replace('Game ', '').replace(',', '').replace(';', '')

lines = text.strip().split('\n')
for line in range(len(lines)):
  lines[line] = lines[line].split(' ')

sum = 0

for line in range(len(lines)):
  maxes = [0, 0, 0]
  for number in range(len(lines[line]) - 1, 1, -2):
    if (int(lines[line][number - 1]) > maxes[int(lines[line][number])]):
      maxes[int(lines[line][number])] = int(lines[line][number - 1])
  sum += maxes[0] * maxes[1] * maxes[2]

print(sum)