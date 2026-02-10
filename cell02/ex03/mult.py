fisrt = int(input("Enter a first number: "))
second = int(input("Enter a second number: "))

result = fisrt * second

print(f"{fisrt} x {second} = {result}")

if result == 0:
    print("This number is both positive and negative.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is positive.")