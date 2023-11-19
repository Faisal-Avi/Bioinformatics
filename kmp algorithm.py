#https://www.tutorialspoint.com/execute_python_online.php
import time
def find_Z_values(pat_substr):
	s = pat_substr
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
	return Z

def find_failure_function(pat_substr):
	Z = find_Z_values(pat_substr)
	print('Z-box : ' + str(Z))
    
	sp_prime = [0] * (len(pat_substr))

	i=0

	for j in range(1,len(Z)):
		i = j + Z[j] - 1 
		if Z[j] == max(Z):
			sp_prime[i] = Z[j]
	print('SP-Prime : '+ str(sp_prime))
	sp_prime = max(sp_prime)
	f_prime = sp_prime + 1
	print('Failue Funciton : ' + str(f_prime))
	return f_prime
	
txt = 'xyabcxabcxabcdefeg'
pat = 'abcxabcde'
c = 1 # initialize text index
p = 1 # initialize pattern index
m = len(txt) # text length
n = len(pat) # pattern length
f_prime = 0 
pat_substr = ''
while c + (n-p) <= m: #15 +(9-4) <= 18
	while pat[p-1] == txt[c-1] and p <= n:
		#print('Text Char : ' + str(txt[c-1]) + ' at position : ' + str(c-1))
		#print('Pattern Char : ' + str(pat[p-1]) + ' at position : '+ str(p-1))
		if c == m:
			break
		if p == n:
			break
		p = p + 1
		c = c + 1
		#time.sleep(.5)
	#time.sleep(.5)
		
	#print('Scaning text at index : ' + str(c-1))
	if p == n:
		print('FOUND MATCH AT POSITION : ' + str(c-n+1))
	elif p == 1:
		c = c + 1
	#print('Mismatch found and shifting pattern')
	if p > 1:
		pat_substr = pat[:p-1]
		print(pat_substr)
		f_prime = find_failure_function(pat_substr)
		p = f_prime
	
#time.sleep(.5)