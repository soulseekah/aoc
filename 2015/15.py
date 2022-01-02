lines = filter(len, map(lambda l: l.strip(), file('15.txt').readlines()))

ingredients = {}

for line in lines:
	ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
	ingredients.update({ingredient[:-1]: {
		'capacity': int(capacity[:-1]),
		'durability': int(durability[:-1]),
		'flavor': int(flavor[:-1]),
		'texture': int(texture[:-1]),
		'calories': int(calories),
	}})

limit = 100

def count(recipe):
	scores = {}
	calories = 0
	for ingredient, amount in recipe.iteritems():
		for name, prop in ingredients[ingredient].iteritems():
			if name == 'calories':
				calories += (prop * amount)
				continue
			scores[name] = scores.get(name, 0) + (prop * amount)
	return calories, reduce(lambda a, b: max(0, a) * max(0, b), scores.values())

max_score = 0
cal_score = 0
for i in range(0, 101):
	for j in range(0, 101 - i):
		for k in range(0, 101 - i - j):
			for l in range(0, 101 - i - j - k):
				calories, score = count(dict(zip(ingredients.keys(), [i, j, k, l])))
				max_score = max(score, max_score)
				if calories == 500:
					cal_score = max(score, cal_score)

print max_score, cal_score
