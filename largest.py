x=int(input("X: "))
y=int(input("Y: "))
z=int(input("Z: "))

if x>y and x>z:
    print(f"{x} is larger.")
elif y>x and y>z:
    print(f"{y} is larger")
else:
    print(f"{z} is larger.")