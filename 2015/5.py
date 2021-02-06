import re

data = file('5.txt').readlines()

# Part 1

nice = 0
for line in data:
	# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
	if len(re.findall('[aeiou]', line)) < 3:
		continue
	# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
	if not re.search('(.)\\1', line):
		continue

	# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
	if re.search('ab|cd|pq|xy', line):
		continue

	nice += 1
print nice

# Part 2

nice = 0
for line in data:
	if not line.strip():
		continue
	
	# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
	if not re.search('(..).*\\1', line):
		print 'rule 1 infriction: %s' % line.strip()
		continue

	# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
	if not re.search('(.).\\1', line):
		print 'rule 2 infriction: %s' % line.strip()
		continue

	print 'nice: %s' % line.strip()
	nice += 1
print nice
