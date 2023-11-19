#t = input('Please input text: ') 
#p = input('Please input pattern: ')
#https://www.tutorialspoint.com/execute_python_online.php

t = 'bbabaxababay'
p = 'aba'

s = p + '$' + t

Z = [0] * len(s)  

Z[0] = 0           # setting first position = 0

r = 0
l = 0

for k in range(1, len(s)):
	if k <= r:     # Inside Z box
		k_prime_pos = k - l
		beta_length = r - k + 1
		if Z[k_prime_pos] < beta_length:
			Z[k] = Z[k_prime_pos]  # Z[k] = Z[k']
		elif Z[k_prime_pos] > beta_length:
			Z[k] = r - k + 1       # Z[k] = length of beta
		else: 
			i = r + 1              # Need to check form z with x
			while i < len(s) and s[i] == s[i - k]:
				i = i + 1
			Z[k] = i - k

			l = k
			r = i - 1
	else:  # Outside the Z-box
		n = 0
		while n + k < len(s) and s[n] == s[n+k]:
			n = n + 1
		Z[k] = n
		if n > 0:
			l = k         # setting the new position of l
			r = k + n - 1 # setting the new position of r 	

mf = Z

for kk in range(len(p)+1):    #removing elements of list for pattern
	del mf[0]

pos = []

for ff in range(len(mf)):     # finding the position of Z value
	if mf[ff] == len(p):
		pos.append(ff+1)
		
print(pos)
	