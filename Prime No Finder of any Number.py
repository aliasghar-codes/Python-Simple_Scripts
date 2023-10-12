num = int(input("Enter your number: "))
Prime = True
for i in range(2, num):
    if (num % i == 0):
        Prime = False
if Prime == True:
    print("Your number is Prime")
else:
    print("Your number is not Prime")

# so what it does is it store user input in num variable that we specify Prime named variable to true initially then for function starts with 2 b'cos 1 is not the prime number and initiall value is prime that's why then num variable is the ending point of range if function then specify that num that user gives when multiply with the range of 2 to num means i then if there modulus means the reminder of division is equal to 0 then its not the prime number then if function specifies that if prime is equal to true means the users given number is prime if its only divisible by itself or one then prime is equal to true so that our program will print your number is prime else it will print your number is not prime.
