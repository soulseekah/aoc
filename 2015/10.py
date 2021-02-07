import re

n = '1113122113'

def read(n):
	m = ''
	for s in map(lambda m: m.group(), re.finditer(r'(.)\1*', n)):
		m += '%s%s' % (len(s), s[0])
	return m

# Part 1 and 2

for i in range(1, 51):
	n = read(n)
	if i == 40:
		print len(n)
print len(n)
