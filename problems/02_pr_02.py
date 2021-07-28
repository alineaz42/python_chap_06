# student fail or pass
# number
yourName = input("enter your name first: \n")
blangla = int(input("Enter the number of bangla: \n"))
english = int(input("Enter the number of english: \n"))
math = int(input("Enter the number of banglamath \n"))

resultList = [blangla, english, math, yourName]

if blangla < 33 or english < 33 or math < 33:
    print("You have faield Mr.", resultList[3])
elif (blangla+english+math)/3 < 40:
    print("You have faield because total percentage is less than 40 Mr.",
          resultList[3])
else:
    print("You have Passed Mr.", resultList[3], " and your marks is ",
          blangla, english, math, "total is:", blangla+english+math)
