try:
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	print("–––Arithmetic operations–––")
	print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")

	choice = int(input("Enter your choice(1-4): "))
	if choice==1:
		result = num1+num2
	elif choice==2:
		result = num1-num2
	elif choice==3:
		result = num1*num2
	elif choice==4:
		result = num1/num2
	else:
		raise Exception("You can choose only between 1 to 4")
except ValueError:
	print("You must enter the number.")
except ZeroDivisionError:
	print("Division by zero is not possible.")
except Exception as e:
	print(e)
else:
	print("Result= ",result)
finally:
	print("Calculation attempt finished.")
