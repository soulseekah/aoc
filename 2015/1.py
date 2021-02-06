# Part 1
data = file('1.txt').read()

level = 0
for c in data:
	level = level + (1 if c is '(' else -1)
print level

# Part 2

level = 0
for i, c in enumerate(data):
	level = level + (1 if c is '(' else -1)
	if level < 0:
		print i + 1
		break
