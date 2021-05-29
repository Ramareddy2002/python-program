n=int(input('enter number'))
i=1
print('factors of %d are:'%(n))
while i<=n:
	if n%i==0:
		print(i)
		i+=1
	else:
		i+=1
'''
output
enter number 16
factors of 16 are:
	1
	2
	4
	8
	16
	'''
