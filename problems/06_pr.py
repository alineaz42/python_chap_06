marks = int(input("Enter your mark: \n"))


if marks > 90 and marks <= 100:
    print("Excellint")
elif marks < 90 and marks >= 80:
    print("A")
else:
    print("less than 80%")
