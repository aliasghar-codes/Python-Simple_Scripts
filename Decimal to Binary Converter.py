def convertbinary(n):
    if n > 1:
        convertbinary(n//2)
    print(n % 2, end = "")
i = int(input("Enter your number: "))
print("The binary value of your number is: ")
convertbinary(i)
