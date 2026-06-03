import random
secret = random.randint(1,50)
count = 0
print("Only 10 trials will be provided to guess")
while True:
	guess = int(input("Enter number of your guess: "))
	count+=1
	if guess==secret:
		print(f"You won in {count} tries")
		break
	elif guess>secret:
	    print(f"Too high! Still {10-count} trials left")
	else:
		print(f"Too low! Still {10- count} trials left")
	if count==10:
		print(f"10 trials completed. The correct number is {secret}")
		break
