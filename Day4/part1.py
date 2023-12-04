f = open("data.txt")

lines = f.read().split('\n')

winning = []

numbers = []

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
  for num in drawn:
    if (len(num) != 0 and dict.__contains__(int(num))):
      wins += 1
  if (wins != 0):
    sum += 2 ** (wins - 1)

print(sum)
