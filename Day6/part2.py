f = open("data.txt")

text = f.read().split('\n')

lines = [x.split(' ') for x in text]

times = [x for x in lines[0][1:] if x]

time = ""
for item in times:
  time += item
time = int(time)

distances = [x for x in lines[1][1:] if x]

distance = ""
for item in distances:
  distance += item
distance = int(distance)

sum = 0
for j in range(time):
  # if (j % 1000000 == 0):
  #   print(j / time)
  if (distance < (j * (time - j))):
    sum += 1

print(sum)