num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of your desired number is {factorial}")

# So here first num is storing a user input then the initial value of factorial named variable is 1 then in range we specify that it starts from 1 and then ends on num which user gives us then add 1 in it then we specify that factorial named value here will be now is i multiply by that whole range means if user input 5 in range then here range store 1,2,3,4,5 and the initial value of factorial is 1 which divide by that whole range of numbers so i will get our desired output because n! factorial means 1 x 2 x 3 x 4 x 5.......n and 5! means 1x2x3x4x5. And at the end i am printing that factorial value.  
