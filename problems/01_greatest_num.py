# finding the greatest number out of four number

num1 = int(input("Enter  number 1 : "))
num2 = int(input("Enter  number 2 : "))
num3 = int(input("Enter  number 3 : "))
num4 = int(input("Enter  number 4 : "))

# if num1 > num2 and num1 > num3 and num1 > num4:
#     print("The greatest of them all is num1 : ", num1)
# elif num2 > num3 and num2 > num4:
#     print("The greatest of them all is num2 : ", num2)
# elif num3 > num4:
#     print("The greatest of them all is num3 : ", num3)
# else:
#     print("The greatest of them all is  num4 : ", num4)

if num1 > num4:
    f1 = num1
else:
    f1 = num4
if num2 > num3:
    f2 = num2
else:
    f2 = num3
if f1 > f2:
    print(f1)
else:
    print(f2)
