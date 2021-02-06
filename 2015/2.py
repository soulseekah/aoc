data = file('2.txt')

# Part 1

wrap = 0
for line in data.readlines():
	l, w, h = map(int, line.split('x'))
	slack = [l, w, h]
	slack.remove(max(slack))
	area = (2*l*w) + (2*w*h) + (2*h*l)
	wrap = wrap + area + reduce(lambda a, b: a * b, slack)
print wrap 

# Part 2

ribbon = 0
data.seek(0)
for line in data.readlines():
	l, w, h = map(int, line.split('x'))
	smallest = [l, w, h]
	smallest.remove(max(smallest))
	ribbon = ribbon + reduce(lambda a, b: (2*a) + (2*b), smallest) + reduce(lambda a, b: a * b, [l, w, h])
print ribbon
