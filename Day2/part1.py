import re
f = open("data.txt")

text = f.read()

text = text.replace('red', '12').replace('green', '13').replace('blue', '14').replace('Game ', '').replace(',', '').replace(';', '')

lines = text.strip().split('\n')
for line in range(len(lines)):
  lines[line] = lines[line].split(' ')

sum = 0

for line in range(len(lines)):
  over = False
  for number in range(len(lines[line]) - 1, 1, -2):
    if (int(lines[line][number]) < int(lines[line][number - 1])):
      over = True
      break
  if (not over):
    sum += line + 1

print(sum)