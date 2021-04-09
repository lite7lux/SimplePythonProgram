an addition program in python

#input number 1
number1_string = input("Enter first number:  ")

# convert first number string input to float
number1 = float(number1_string)

#input number 2
number2_string = input("Enter second number:  ")

# convert second number string input to float
number2 = float(number2_string)

# addition funcction
def addition(number1, number2):
    add = number1 + number2
    return add

result = addition(number1, number2)

#print output
print("the addition is: ", result)
