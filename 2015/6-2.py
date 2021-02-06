SIZE = 1000

lights =  [[0 for n in range(SIZE)] for m in range(SIZE)]
data = list(filter(len, map(lambda c: c.strip(), open('6.txt', 'rb').readlines())))

while True:
	try:
		command = data.pop(0).decode('utf8').split()
	except:
		break

	if command[0] == 'turn':
		x1, y1 = map(int, command[2].split(','))
		x2, y2 = map(int, command[4].split(','))

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				lights[x][y] = (lights[x][y] + 1) if command[1] == 'on' else max(0, lights[x][y] - 1)
	elif command[0] == 'toggle':
		x1, y1 = map(int, command[1].split(','))
		x2, y2 = map(int, command[3].split(','))

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				lights[x][y] = lights[x][y] + 2

total = 0
for x, column in enumerate(lights):
	for y, brightness in enumerate(column):
		total += brightness
print(total)
