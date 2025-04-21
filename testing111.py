

while True:
    name = input("Pls Enter your name: ")
    if name.strip() == "":
        print("Invalid input, please try again.")
    elif not name.isalpha():
        print("Invalid input, please try again. Only abcd available")
    else:
        print("you name is " + name)




