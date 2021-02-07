lines = filter(len, map(lambda l: l.strip(), file('14.txt').readlines()))

tmax = 2503

deer = {}

for line in lines:
	name, can, fly, speed, kms, _, endurance, seconds, but, then, must, rest, _, recovery, seconds = line.split()
	position = 0
	deer[name] = map(int, [speed, endurance, recovery, position])

# Part 1
for d in deer:
	fuel = tmax
	speed, endurance, recovery, position = deer[d]
	while fuel:
		sprint = (speed * min(fuel, endurance))
		fuel -= sprint / speed

		deer[d][-1] += sprint
		if not fuel:
			break

		fuel -= min(fuel, recovery)
	
print max(map(lambda d: d[-1], deer.values()))

for line in lines:
	name, can, fly, speed, kms, _, endurance, seconds, but, then, must, rest, _, recovery, seconds = line.split()
	position = 0
	points = 0
	resting = 0
	running = endurance
	deer[name] = map(int, [speed, endurance, recovery, position, resting, running, points])

# Part 2
for t in range(1, tmax + 1):
	for d in deer:
		if deer[d][-3]: # resting
			deer[d][-3] -= 1
			if not deer[d][-3]:
				deer[d][-2] = deer[d][1] # start running
				continue

		if deer[d][-2]: # running
			deer[d][-4] += deer[d][0]# position
			deer[d][-2] -= 1
			if not deer[d][-2]:
				deer[d][-3] = deer[d][2] # start recovering
	
	first = [d] # initial deer
	pmax = deer[d][-4]
	for d in deer:
		if deer[d][-4] > pmax:
			pmax = deer[d][-4]
			first = [d]
			continue
		if deer[d][-4] == pmax and d not in first:
			first.append(d)

	for f in first:
		deer[f][-1] += 1 # poooints

print max(map(lambda d: d[-1], deer.values()))
