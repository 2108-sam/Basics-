while True:
    uinput=input("Enter your number (exit to get out): ")
    if uinput.lower()=="exit":
        print("Goodbye")
        break
    try:
        number=int(uinput)
        num=number%2
        if num==0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number")
    except ValueError:
        print("Please enter a valid number")