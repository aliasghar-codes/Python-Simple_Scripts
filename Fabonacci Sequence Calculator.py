def fabo(n):
    if n <= 1:
        return n
    else:
        return fabo(n-1) + fabo(n-2)
n = int(input("Enter your number: "))
if n <= 0:
    print("enter the positive number")
else:
    print("Your sequence is:")
    for i in range(n+1):
        print(fabo(i))
