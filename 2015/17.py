lines = sorted(map(int, filter(len, map(lambda l: l.strip(), file('17.txt').readlines()))))

gotit = 0
min_containers = 999
cnt_min = 0
for i in range(1, 2**len(lines)):
	containers = map(lambda c: c[0], filter(lambda c: c[1] == '1', zip(lines, list('%20s' % bin(i)[2:]))))
	if sum(containers) == 150:
		gotit += 1
		if len(containers) < min_containers:
			min_containers = len(containers)
			cnt_min = 1
		elif len(containers) == min_containers:
			cnt_min += 1
print gotit # Part one
print cnt_min # Part two
