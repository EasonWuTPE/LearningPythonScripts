

def myrange(n):
	x = 0
	while x < n:
		j=x
		x+=1
		if j%7==0:
			yield j

for i in myrange(10):
	print( i, end=" " )

print("\n")
