
##### _____ Greatest of 2 numbers _____ #####

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("\n")
if a < b:
    print(b, "is the greatest number")
elif a > b:
    print(a, "is the greatest number")
else:
    print("Both numbers are equal")