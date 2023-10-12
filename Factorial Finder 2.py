def fact(n):
    if n == 1:
        return 1
    else:
        return(n * fact(n-1))
n = int(input("Enter the number here: "))
if n == 0:
    print("The Factorial of 0 is 1")
else:
    print("The factorial of your number is ", fact(n))

# It's working on the formula n * n-1 if user entered 5 then 5 will be multiplied by 4 and stored in the fact name function then 4 will be multiplied by 3 then 3 with 2 and then 2 with 1 so we will get our factorial
