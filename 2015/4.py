from hashlib import md5

key = 'ckczppom%d'
nonce = 1
length = 5

# Part 1

while len(md5(key % nonce).hexdigest().lstrip('0')) != (32 - length):
	nonce += 1
print nonce

# Part 2

length = 6
nonce = 1

while len(md5(key % nonce).hexdigest().lstrip('0')) != (32 - length):
	nonce += 1
print nonce
