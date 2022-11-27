
##### _____ Euclids Algorithm _____ #####

# The user inputs 2 numbers and this script 
# will find the greatest common divisor

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
quotient = int(a / b) 
remainder = a % b

while remainder > 0:
    a = b
    b = remainder
    quotient = int(a / b)
    remainder = a % b

print("\n")
print("gcd =", b)
