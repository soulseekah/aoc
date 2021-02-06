data = file('3.txt').read()

# Part 1

position = [0, 0]
locations = set()
locations.add(tuple(position)) # first location
for c in data:
	c = c.strip()
	if not c:
		continue

	position[1] = position[1] + 1 if c == '^' else position[1]
	position[1] = position[1] - 1 if c == 'v' else position[1]
	position[0] = position[0] - 1 if c == '<' else position[0]
	position[0] = position[0] + 1 if c == '>' else position[0]

	locations.add(tuple(position))
print len(locations)

# Part 2
santa = [0, 0]
robo = [0, 0]
locations = set()
locations.add(tuple(santa))
locations.add(tuple(robo))
turn = 'santa'
for c in data:
	c = c.strip()
	if not c:
		continue

	position = santa if turn == 'santa' else robo

	position[1] = position[1] + 1 if c == '^' else position[1]
	position[1] = position[1] - 1 if c == 'v' else position[1]
	position[0] = position[0] - 1 if c == '<' else position[0]
	position[0] = position[0] + 1 if c == '>' else position[0]

	locations.add(tuple(position))

	position = santa if turn == 'santa' else robo

	turn = 'robo' if turn == 'santa' else 'santa'

print len(locations)
