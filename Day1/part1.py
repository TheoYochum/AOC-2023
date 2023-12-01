import re
f = open("data.txt")

text = f.read()

lines = text.strip().split('\n')


regex = re.compile(r'.*?([0-9]).*?([0-9]){0,1}[^0-9]*?$')
sum = 0

for line in lines:
  matches = regex.match(line)
  if (matches.group(2) == None):
    sum += int(matches.group(1) + matches.group(1))
  else:
    sum += int(matches.group(1) + matches.group(2))

print(sum)
