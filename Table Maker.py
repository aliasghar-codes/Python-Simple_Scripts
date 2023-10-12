num = int(input("Enter the number for what you want your table of: "))
num2 = int(input("Till what value your table should end: "))
for i in range(1, num2 + 1):
    print()
    print(str(num), "x", str(i), "=", num*i)
print("\nThanks for using our app\n")
num1 = input("Press Enter key to continue... ")

# So what it does is first num variable takes input from the user for the number you want your table of and then num2 variable takes input from the user to specify the ending point of the table like 10,15 or 20 till what value you want your table to end then for function's range's first value specify that your table will start with 1 not 0 which is by default value and num2 which user tell program is the ending value in range but by default its value is n-1 so we add 1 in it than print() specify empty line and the second last print function first prints string of num means 2 or 4 or anything what user entered then x to show multiply then i which is range and made up of num2 variable so its list will print then = then out most imp function for what i made that program which is num x i here the num is same all the time but i is range which changes according to num2 value so in the end they are multiplying to print our table the last print function is optional and the last num1 variable (I write it because that program was closing suddenly after showing the table so i write it to tell the program to stay until the user presses enter key then you can close yourself).