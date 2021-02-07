import itertools # iddkfa

lines = filter(len, map(lambda l: l.strip(), file('9.txt').readlines()))

costs = {}
route = []

# Part 1

for line in lines:
	src, _, to, _, cost = line.split()
	if not src in route:
		route.append(src)
	if not to in route:
		route.append(to)
	costs[(src, to)] = int(cost)
	costs[(to, src)] = int(cost)

def calcost(route):
	global costs
	total = 0
	for i, r in enumerate(route):
		try:
			total += costs[(route[i], route[i+1])]
		except:
			pass
	return total

print min(map(calcost, itertools.permutations(route, len(route))))

# Part 2

print max(map(calcost, itertools.permutations(route, len(route))))
