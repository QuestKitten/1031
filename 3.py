# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

# mathmaticalsymbols can also be used instead of the full word
if operation == "add":
    result = first_number + second_number
    print(f"Sum: {result}")
elif operation == "+":
    result = first_number + second_number
    print(f"Sum: {result}")

elif operation == "subtract":
    result = first_number - second_number
    print(f"Difference: {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"Difference: {result}")

elif operation == "multiply":
    result = first_number * second_number
    print(f"Product: {result}")
elif operation == "x":
    result = first_number * second_number
    print(f"Product: {result}")

elif operation == "divide":
    result = first_number / second_number
    print(f"quotient: {result}")
elif operation == "/":
    result = first_number / second_number
    print(f"quotient: {result}")

else:
    print("Sorry, I do not understand your request.")
