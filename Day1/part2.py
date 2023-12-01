import re
def main():
  f = open("data.txt")

  text = f.read()

  lines = text.strip().split('\n')


  regex1 = re.compile(r'^.*?([0-9]|one|two|three|four|five|six|seven|eight|nine).*([0-9]|one|two|three|four|five|six|seven|eight|nine)')
  regex2 = re.compile(r'^.*?([0-9]|one|two|three|four|five|six|seven|eight|nine)')
  sum = 0

  for line in lines:
    matches = regex1.match(line)
    if (matches == None):
      matches = regex2.match(line)
      sum += 10 * parse(matches.group(1)) + parse(matches.group(1))
    else:
      sum += 10 *parse(matches.group(1)) + parse(matches.group(2))

  print(sum)

def parse(string):
  match string:
    case 'one':
      return 1
    case 'two':
      return 2
    case 'three':
      return 3
    case 'four':
      return 4
    case 'five':
      return 5
    case 'six':
      return 6
    case 'seven':
      return 7
    case 'eight':
      return 8
    case 'nine':
      return 9
    case _:
      return int(string)
main()