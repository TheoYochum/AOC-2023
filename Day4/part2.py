f = open("data.txt")

lines = f.read().split('\n')

winning = []

numbers = []

repeats = {}
sum = 0
for line in range(len(lines)):
  wins = 0
  dict = {}
  card = lines[line][9:].split('|')
  winners = card[0].split(' ')
  drawn = card[1].split(' ')
  for winner in winners:
    if (len(winner) != 0):
      dict[int(winner)] = 1
  if (not repeats.__contains__(line)):
    repeats[line] = 1
  for num in drawn:
    if (len(num) != 0 and dict.__contains__(int(num))):
      wins += 1
      if (repeats.__contains__(line + wins)):
        repeats[line+wins] = repeats[line + wins] + 1 * repeats[line]
      else:
        repeats[line + wins] = 1 * repeats[line] + 1
  sum += repeats[line]
print(sum)