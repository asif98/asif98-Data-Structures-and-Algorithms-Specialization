# python3

import sys

def exp(prime, x, n) :
	if n == 0 :
		return 1
	elif n%2 == 0 :
		return (exp(prime, x, n//2)**2) % prime
	else :
		return ((exp(prime, x, n//2)**2)*x) % prime

def exp(prime, x, n) :
	if n == 0 :
		return 1
	elif n%2 == 0 :
		return (exp(prime, x, n//2)**2) % prime
	else :
		return ((exp(prime, x, n//2)**2)*x) % prime

def ask(a, b, l):
	if (cum_hash1[a+l] - cum_hash1[b+l] + exp(prime1, x, l)*(cum_hash1[b] - cum_hash1[a]))%prime1 == 0 :
		if (cum_hash2[a+l] - cum_hash2[b+l] + exp(prime2, x, l)*(cum_hash2[b] - cum_hash2[a]))%prime2 == 0 :
			return True
	return False

text = sys.stdin.readline()
q = int(sys.stdin.readline())

prime1 = 1000000007
prime2 = 1000000009
x = 263

cur_hash1 = 0
cur_hash2 = 0
cum_hash1 = [0]
cum_hash2 = [0]
for i in range(len(text)) :
	cur_hash1 = x*cur_hash1 + ord(text[i])
	cur_hash1 = cur_hash1 % prime1
	cum_hash1.append(cur_hash1)

	cur_hash2 = x*cur_hash2 + ord(text[i])
	cur_hash2 = cur_hash2 % prime2
	cum_hash2.append(cur_hash2)



for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if ask(a, b, l) else "No")
