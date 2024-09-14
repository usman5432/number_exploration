name = input("Enter your name: ")
num1 = int(input("Enter your first favourite number: "))
num2 = int(input("Enter your second favourite number: "))
num3 = int(input("Enter your third favourite number: "))

print(f"\nHello, {name}! Let's explore your favourite numbers:")
if num1 % 2 == 0:
    print(f"The number {num1} is even")
else:
    print(f"The number {num1} is odd")

if num2 % 2 == 0:
    print(f"The number {num2} is even")
else:
    print(f"The number {num2} is odd")

if num3 % 2 == 0:
    print(f"The number {num3} is even")
else:
    print(f"The number {num3} is odd")

print(f"The number {num1} and its square: ({num1}, {num1**2})")
print(f"The number {num2} and its square: ({num2}, {num2**2})")
print(f"The number {num3} and its square: ({num3}, {num3**2})")

sum = num1+num2+num3
print(f"\nAmazing! The sum of your favourite numbers is: {sum}")
flag = True
for i in range(2,(sum)//2):
    if sum%i == 0:
        flag = False

if flag:
    print(f"Wow, {sum} is a prime number!")
else:
    print(f"{sum} is not a prime number!")