f = open("data.txt")

lines = f.read().split('\n')

sum = 0
for line in range(len(lines)):
  length = 0
  for char in range(len(lines[line])):
    add = False
    if (length != 0):
      length -= 1
      continue
    if ((lines[line][char]).isnumeric()):
      x = 0
      while (not add and char + x < len(lines[line]) and lines[line][char + x].isnumeric()):
        for i in range(-1, 2):
          for j in range(-1, 2):
            if ((not add) and line + i > 0 and line + i < len(lines) and char + x + j > 0 and char + x + j < len(lines[line + i]) and (not lines[line + i][char + x + j].isnumeric()) and (not (lines[line + i][char + x + j] == '.'))):
              add = True
        x += 1
      if (add):
        i = 0
        end = 0
        while (char + i < len(lines[line]) and lines[line][char + i].isnumeric()):
          i += 1
          end = char + i
        length = end - char - 1
        adding = int(lines[line][char:end])
        sum += adding
print(sum)
