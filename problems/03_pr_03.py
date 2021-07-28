text = input("Enter a text :")


if "make a lot of money" in text:
    comment = True
elif "buy now" in text:
    comment = True
elif "click this" in text:
    comment = True
elif "subscribe this" in text:
    comment = True
else:
    comment = False

if comment:
    print("This text is spam ")
else:
    print("This text is not spam")
