f = open("data.txt")

text = f.read()

lines = [x.split('\n') for x in text.strip().split('\n\n')]
seeds = [int(x) for x in lines[0][0][8:].split(' ')]
lines = lines[1:]
maps = [[[int(z) for z in y.split(' ')] for y in x[1:]] for x in lines]

locations = []
for seed in seeds:
  for map in maps:
    i = 0
    mapped = False
    while (i < len(map) and not mapped):
      if (seed - map[i][1] > 0 and seed - map[i][1] < map[i][2]):
        seed = map[i][0] + seed - map[i][1]
        break
      i += 1
  locations.append(seed)

print(min(locations))