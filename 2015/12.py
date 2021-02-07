import re
import json

data = file('12.txt').read()

# Part one
print sum(map(int, re.findall('-?\d+', data)))

# Part two
def gather_numbers(s):
	n = 0

	if type(s) is list:
		for i in s:
			n += gather_numbers(i)

	if type(s) is dict:
		if 'red' in s.values():
			return n
		for i in s.values():
			n += gather_numbers(i)

	if type(s) is int:
		return n + s
	
	return n

print gather_numbers(json.loads(data))
