import itertools

lines = filter(len, map(lambda l: l.strip(), file('13.txt').readlines()))

mood = {}
table = set()

for line in lines:
	who, _, sign, amount, _, _, _, _, _, _, to = line.strip('.').split()
	mood[(who,to)] = int(amount) if sign == 'gain' else -int(amount)
	table.add(who)

def calmood(table):
	global mood

	total = 0
	for i, p in enumerate(table):
		try:
			if not i:
				total += mood[(p, table[-1])]
				total += mood[(p, table[i+1])]
			elif i is (len(table) - 1):
				total += mood[(p, table[0])]
				total += mood[(p, table[i-1])]
			else:
				total += mood[(p, table[i-1])]
				total += mood[(p, table[i+1])]
		except:
			pass
	return total

# Part 1
print max(map(calmood, itertools.permutations(table, len(table))))

# Part 2
table.add('Me')
print max(map(calmood, itertools.permutations(table, len(table))))
