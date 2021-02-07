import string
import re

p = 'cqjxjnds'

cmap = list(string.ascii_lowercase)
def incr(p):
	v = map(lambda c: cmap.index(c), list(p))

	if not v:
		return 'a' # enlengthen

	v[-1] += 1 # bloop

	if v[-1] == len(cmap): # recurse and reset last digit
		return incr(''.join(map(lambda n: cmap[n], v[:-1]))) + 'a'
	return ''.join(map(lambda n: cmap[n], v))

# Part 1

m1 = '|'.join(map(lambda n: string.ascii_lowercase[n:n+3], range(0, 24)))

def find(p):
	while True:
		p = incr(p)

		if 'i' in p or 'o' in p or 'l' in p:
			continue

		if not re.findall(m1, p):
			continue

		if len(set(re.findall('(.)\\1', p))) < 2:
			continue

		break
	return p

p = find(p)
print p, 'is the next password and',

p = find(p)
print p, 'is the password thereafter'
