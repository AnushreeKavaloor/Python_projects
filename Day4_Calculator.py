num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter your choice(1-4): "))
if choice==1:
	result = num1 + num2
	print("Total = ", result)
elif choice==2:
	result = num1 - num2
	print("Subtraction = ",result)
elif choice==3:
	result = num1* num2
	print("Multiplication: ",result)
elif choice==4:
	if num2!=0:
		result = num1/num2
		print("Division: ",result)
	else:
		print("Division by zero is not possible.")
else:
		print("Invalid! Please enter number between 1 to 4.")
