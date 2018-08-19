#Sean, 04/11/2018, To create a calculator to handle binary numbers, addition & subtraction


def binaryCalculator():
    """Binary Calculator that uses a simple menu format for execution
        of funtions that convert binary to decimal and decimal to binary. Runs until the user input is 5."""
    global first_number
    global second_number
    global user_input
    print("What do you want to do?")
    print("1. Enter the binary number")
    print("2. Enter the second binary number")
    print("3. Add the two binary numbers together")
    print("4. Subtract the second binary number from the first")
    print("5. Exit the program\n")
    user_input = input('Enter Command\n')
    first_number_count = 0
    first_number_count2 = 0
    while user_input != '5':
        if user_input == '1':
            first_number = (input("Enter the first number:\n"))
            print("Your First Number is:", first_number, "in decimal:", bintodec(first_number))
            binaryCalculator()
            break
        if user_input == '2':
            second_number = (input("Enter the second number:\n"))
            print("Your Second Number is:", second_number, "in decimal:", bintodec(second_number))
            binaryCalculator()
            break
        if user_input == '3':
            if "first_number" and "second_number" not in globals():
                print("Please Do Commands 1&2 First")
                first_number = input("Enter the first number:\n")
                second_number = input("Enter the second number:\n")
                binaryCalculator()
                break
            else:
                first_number_count += bintodec(first_number)+bintodec(second_number)
                print(first_number,"+",second_number,"Sum Binary=",
                      dectobin(first_number_count),"Sum Decimal=",first_number_count)
                binaryCalculator()
                break
        if user_input == '4':
            if "first_number" and "second_number" not in globals():
                print("Please Do Commands 1&2 First")
                first_number = int(input("Enter the first number:\n"))
                second_number = int(input("Enter the second number:\n"))
                binaryCalculator()
                break
            if second_number < first_number:
                print("Second Number Should be Larger Than First")
            else:
                first_number_count2 += int(second_number)-int(first_number)
                print(second_number,"-",first_number,"Difference Binary=",first_number_count2,"Difference Decimal="
                      ,bintodec(first_number_count2))
                binaryCalculator()
                break
        if user_input not in str("1,5"):
            print("Invalid Input, Try Again")
            binaryCalculator()
            break


def dectobin(n):
    """Translate a positive integer from decimal to binary.
    Params: n (int): decimal number > 0
    Returns: (string) binary number as a int
    """
    if n == 0:
        return ''
    else:
        return dectobin(n // 2) + str(n % 2)


def bintodec(x):
    """Converts binary into decimal.
        Params: x (str): binary number as an int
        Returns: (int) decimal number
    """
    n = 0
    for i in str(x):
        if i > '1':
            print("Please Enter a Binary Number\n")
            binaryCalculator()
            quit()
        n *= 2
        if i == '1':
            n += 1
    return n

print(625 % 2)
binaryCalculator()
