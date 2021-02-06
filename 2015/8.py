import re

lines = filter(len, map(lambda l: l.strip(), file('8.txt').readlines()))

# Part 1

code = len(''.join(lines))
memory = sum(map(lambda line: len(re.sub('\\\\x[0-9a-f]{2}', '_', line[1:-1].replace('\\\\', '=').replace('\\"', '"'))), lines))
print code - memory

# Part 2

print sum(map(lambda line: len('"%s"' % line.replace('"', '__').replace('\\', '..')), lines)) - code
