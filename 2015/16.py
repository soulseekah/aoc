import re

lines = filter(len, map(lambda l: l.strip(), file('16.txt').readlines()))

sues = {}
for line in lines:
	sue, matches = re.findall(r'Sue (\d+): (.*)', line)[0]
	sues[sue] = dict(map(lambda l: map(lambda k: k.strip(), l.strip().split(':')), matches.split(',')))

match = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}

matches = {}
for sue, props in sues.iteritems():
	ok = True
	for prop, value in props.iteritems():
		# Part 2 starts here
		if prop in ['cats', 'trees']:
			if match[prop] > int(value):
				ok = False
				break
		elif prop in ['pomeranians', 'goldfish']:
			if match[prop] < int(value):
				ok = False
				break
		# Part 2 ends here
		elif match[prop] != int(value):
			ok = False
			break
	if ok:
		matches[sue] = props

print matches
