Open In Colab

def add_numbers(a,b):
    total = a + b
    return total
def greet_user(name):
    return f"Namaskara {name} GenAI journey started!"

#Test it

num1 = 5
num2 = 3
result = add_numbers(num1,num2)
print("Total: ", result)

your_name = input("Enter your name: ")
message = greet_user(your_name)
print(message)
