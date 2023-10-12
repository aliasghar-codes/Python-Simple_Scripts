a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
def greterofthree():
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print(greterofthree())
