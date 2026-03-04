while True:
    print("""
    \n1.\tCelsius to Fehrenheit:
    \n2\tFahrenheit to Celsius.
    """)
    user_input=input("Please make your selection(exit to leave): \n")
    if user_input.lower()=="exit":
        print("Exiting the loop.")
        break

    if user_input not in1("1","2"):
        print("Enter a valid range.")
        continue


    temperature = float(input("Enter your temperature: \n"))
    if user_input=="1":
        reading=((9/5)*temperature)+32
        initial= "degrees celsius"
        scale= "Fehrenheit"
    else:
       reading=5/9*(temperature-32)
       initial = "Fehrenheit"
       scale = "degrees celsius"
    print(f"{temperature} {initial} is {reading:.2f} {scale}")
