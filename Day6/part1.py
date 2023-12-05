f = open("data.txt")

text = f.read().split('\n')

lines = [x.split(' ') for x in text]

times = [x for x in lines[0][1:] if x]

distances = [x for x in lines[1][1:] if x]

product = 1
for i in range(len(times)):
  sum = 0
  time = int(times[i])
  distance = int(distances[i])
  for j in range(time):
    if (distance < (j * (time - j))):
      sum += 1
  product *= sum

print(product)