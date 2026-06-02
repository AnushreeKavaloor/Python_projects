l = [2,5,9]
it = iter(l)
#iterator
print("Iterator results")
print(next(it))
print(next(it))
print(next(it))

print("Generator results")
def squares(x):
	for i in range(x):
		yield(i*2)
#generator
		
gl = squares(26)

for n in gl:
		if n>50:
			break
		print(n)
