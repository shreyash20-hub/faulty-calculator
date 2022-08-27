first= int(input("Enter the first number:"))
operator= input("Enter the operator(+,-,*,/,% :)")
second= int(input("Enter the second number:"))

first=int(first)
second=int(second)


if first == 45 and second == 3:
    print("faulty calculator")

elif operator == "*":
    print(first*second)

elif first == 56 and second== 9:
    print("faulty calculator")

elif operator == "+":
    print(first+second)

elif first== 56 and second == 6:
    print("faulty calculator")

elif operator == "/":
    print(first+second)

else :
    print("calculation is right")