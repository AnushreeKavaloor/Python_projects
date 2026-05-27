while True:
	try:
		print("–––MENU–––")
		print("+\n-\n*\n/\n%\n**\nx or X for EXIT")
		choice = input("Enter your choice: ")
		if choice.lower()=='x':
			print("Exiting....")
			break
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		match choice:
			case '+':
				result = num1 + num2
				print(f"Result: {result}")
			case '-':
				result = num1 - num2
				print(f"Result: {result}")
			case '*':
				result = num1 * num2
				print(f"Result: {result}")
			case '/':
				if num2!=0:
					result = num1 / num2
					print(f"Result: {result}")
				else:
					print("Division by zero is impossible")
			case '%':
				if num2!=0:
					result = num1 % num2
					print(f"Result: {result}")
				else:
					print("Division by zero is invalid to find remainder")
			case '**':
				result = num1**num2
				print(f"Result: {result}")
			
			case _:
					print("Invalid Operation")
	except ValueError:
		print("You must enter only numbers")
	finally:
		print("Operation completed!")
