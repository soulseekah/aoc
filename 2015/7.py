import re

prg = filter(len, map(lambda c: c.strip(), file('7.txt').readlines()))

# Part 1

wires = {}

def go():
	global wires

	iterations = 0
	while True: # Run the simulation until it stabilizes
		previous = dict(wires)
		iterations += 1

		for line in prg:
			operation, destination = line.split(' -> ')
			match = re.search('(OR|AND|LSHIFT|NOT|RSHIFT)', operation) 
			try:
				if match:
					op = match.group(0)
					operands = filter(len, map(lambda o: o.strip(), operation.split(op)))

					if op == 'AND':
						wires[destination] = \
							int(operands[0] if operands[0].isdigit() else wires[operands[0]]) \
							& int(operands[1] if operands[1].isdigit() else wires[operands[1]])

					if op == 'OR':
						wires[destination] = \
							int(operands[0] if operands[0].isdigit() else wires[operands[0]]) \
							| int(operands[1] if operands[1].isdigit() else wires[operands[1]])

					if op == 'LSHIFT':
						wires[destination] = \
							int(operands[0] if operands[0].isdigit() else wires[operands[0]]) \
							<< int(operands[1] if operands[1].isdigit() else wires[operands[1]])

					if op == 'RSHIFT':
						wires[destination] = \
							int(operands[0] if operands[0].isdigit() else wires[operands[0]]) \
							>> int(operands[1] if operands[1].isdigit() else wires[operands[1]])

					if op == 'NOT':
						wires[destination] = ~int(operands[0] if operands[0].isdigit() else wires[operands[0]])
				else:
					wires[destination] = int(operation if operation.isdigit() else wires[operation])
			except:
				continue


		if wires == previous:
			print 'Stabilized in %d iterations with' % iterations,
			break

go()
print wires['a'], 'on a'

# Part 2
for i, v in enumerate(prg):
	if re.match('.* -> b$', v):
		prg[i] = '%d -> b' % wires['a']
wires = {}
go()
print wires['a'], 'on a'
