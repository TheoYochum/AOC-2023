f = open("data.txt")

text = f.read()

lines = [x.split('\n') for x in text.strip().split('\n\n')]
seeds = [int(x) for x in lines[0][0][7:].split(' ')]

seed_ranges = []
for i in range(0, len(seeds), 2):
  seed_ranges.append([seeds[i], seeds[i + 1]])

lines = lines[1:]
maps = [[[int(z) for z in y.split(' ')] for y in x[1:]] for x in lines]
for map in maps:
  new_ranges = []
  for seed_range in seed_ranges:
    for line in map:
      if (seed_range[0] >= line[1] + line[2] or seed_range[0] + seed_range[1] <= line[1]):
        # Out of bounds
        continue
      elif (seed_range[0] < line[1] and seed_range[0] + seed_range[1] < line[1] + line[2]):
        # Overlaps on end
        new_ranges.append([line[0], seed_range[1] - (line[1] - seed_range[0])])
        seed_range = [seed_range[0], (line[1] - seed_range[0])]
      elif (seed_range[0] >= line[1] and seed_range[0] < line[1] + line[2] and seed_range[0] + seed_range[1] > line[1] + line[2]):
        # Overlaps on start
        new_ranges.append([line[0] + (seed_range[0] - line[1]), line[1] + line[2] - seed_range[0]])
        seed_range = [line[1] + line[2], seed_range[1] - (line[1] + line[2] - seed_range[0])]
      elif (seed_range[0] >= line[1] and seed_range[0] < line[1] + line[2]):
        # Subset
        new_ranges.append([line[0] + (seed_range[0] - line[1]), seed_range[1]])
        seed_range = [-1,0]
      elif (seed_range[0] < line[1] and seed_range[0] + seed_range[1] >= line[1] + line[2]):
        # Superset
        new_ranges.append([line[0], line[2]])
        seed_ranges.append([line[1] + line[2], seed_range[1] - line[2] - (line[1] - seed_range[0])])
        seed_range = [seed_range[0], line[1] - seed_range[0]]
    if (seed_range[0] != -1):
      new_ranges.append(seed_range)
  seed_ranges = new_ranges
locations = []
for range in seed_ranges:
  locations.append(range[0])


print(min(locations))