import math


def tro():

    intro = (input("\n welcome to my calc"
                   " \n please enter the number below "
                   "\n"
                   "\n 1. decimal to binary "
                   "\n 2. binary to decimal "
                   "\n 3. add number"
                   "\n 4. subtract number"
                   "\n 5. multiply number"
                   "\n 6. divide number"
                   "\n 7. root"
                   "\n 8. modules"
                   "\n 9. Factorial"
                   "\n 10. sin"
                   "\n 11. cos"
                   "\n 12. tan"
                   "\n 13. natural log"
                   "\n 14. binary to text"
                   "\n 15. text to binary"
                   "\n 16. hexadecimal to decimal"
                   "\n 17. hexadecimal to decimal to binary"
                   "\n 18. password creator"
                   "\n 19. exit"
                   "\n == "))
    print("\n")

    if intro == "1":
        bin()
    elif intro == "2":
        din()
    elif intro == "3":
        add()
    elif intro == "4":
        subtract()
    elif intro == "5":
        times()
    elif intro == "6":
        divide()
    elif intro == "7":
        r()
    elif intro == "8":
        modules()
    elif intro == "9":
        factorial()
    elif intro == "10":
        sin()
    elif intro == "11":
        cos()
    elif intro == "12":
        tan()
    elif intro == "13":
        in_1()
    elif intro == "14":
        bin_text()
    elif intro == "15":
        text_bin()
    elif intro == "16":
        hex_din()
    elif intro == "17":
        hex_din_bin()
    elif intro == "18":
        pass_creator()
    elif intro == "19":
        exit()

    else:
        ValueError(1, 19)
        print("wrong")
        tro()


def bin():
    try:
        print("welcome to decimal to binary ")

        num = input("please enter your number ")

        binary = []

        while num != 0:
            if num % 2 == 0:
                num = num / 2
                binary.insert(0, 0)

            else:
                num = (num - 1) / 2
                binary.insert(0, 1)

        print(binary)

    except ValueError:
        print("only numbers")
        bin()


def din():
    try:
        bib = list(input("Enter a Binary number: "))
        decimal = 0

        for x in range(len(bib)):
            digit = bib.pop()
            if digit == "1":
                decimal = decimal + pow(2, x)

        print("Decimal is ", decimal)

    except ValueError:
        print("only number")


def add():
    try:
        num1 = float(input("enter your number: "))
        num2 = float(input("enter your number: "))
        print(num1, "+", num2, "=", num1 + num2)

    except ValueError:
        print("numbers only")


def subtract():
    try:
        num1 = float(input("enter your number: "))
        num2 = float(input("enter your number: "))
        print(num1, "-", num2, "=", num1 - num2)

    except ValueError:
        print("numbers only")


def times():
    try:
        num1 = float(input("enter your number: "))
        num2 = float(input("enter your number: "))
        print(num1, "*", num2, "=", num1 * num2)
    except ValueError:
        print("numbers only")


def divide():
    try:
        num1 = float(input("enter your number: "))
        num2 = float(input("enter your number: "))
        print(num1, "/", num2, "=", num1 / num2)
    except ValueError:
        print("numbers only")


def power():
    try:
        num1 = float(input("enter the base number: "))
        num2 = float(input("enter the power number: "))
        print(num1, "^", num2, "=", num1 ** num2)
    except ValueError:
        print("numbers only")


def r():
    try:
        num1 = float(input("enter the 1st number: "))
        num2 = float(input("enter the 2nd number: "))
        print(num1, " root ", num2, "=", num2 ** (1 / num1))
    except ValueError:
        print("numbers only")


def modules():
    try:
        num1 = float(input("enter the 1st number: "))
        num2 = float(input("enter 2nd number: "))
        print(num1, " % ", num2, "=", num1 % num2)
    except ValueError:
        print("numbers only")


def factorial():
    try:
        num1 = float(input("enter your 1st number: "))
        num2 = float(input("enter your 2nd number: "))
        total_num = num1 + num2
        num2 = 1
        while num1 > 1:
            num2 *= num1
            num1 = num1 - 1
        print("n!(", num1, ")=", num2)
    except ValueError:
        print("numbers only")


def sin():
    try:
        num1 = float(input("enter your number: "))
        print("sin(", num1, ")=", math.sin(num1))
    except ValueError:
        print("numbers only")


def cos():
    try:
        num1 = float(input("enter your number: "))
        print("cos(", num1, ")=", math.cos(num1))
    except ValueError:
        print("numbers only")


def tan():
    try:
        num1 = float(input("enter your number: "))
        print("tan(", num1, ")=", math.tan(num1))
    except ValueError:
        print("numbers only")


def in_1():
    try:
        num1 = float(input("enter your number: "))
        print("In( ", num1, " )= ", math.log(num1))
    except ValueError:
        print("numbers only")


def bin_text():
    try:
        bin = input("enter your binary number: ")
        binary_int = int(bin, 2)
        byte_number = binary_int.bit_length() + 7 // 8

        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()

        print(ascii_text)

    except ValueError:
        print("numbers only")


def text_bin():
    try:
        test_str = input("please enter your text: ")
        print("the original string is : " + str(test_str))
        res = ' '.join(format(ord(i), 'b') for i in test_str)
        print("the string after binary conversion: " + str(res))
    except ValueError:
        print("numbers only")


def hex_din():
    try:
        test_string = input("enter your hexadecimal: ")
        print("the original string: " + str(test_string))

        res = int(test_string, 16)
        print("the decimal number of hexadecimal string: " + str(res))
    except ValueError:
        print("numbers only")


def hex_din_bin():
    try:
        test_string = input("enter your hexadecimal: ")
        print("the original string: " + str(test_string))

        res = int(test_string, 16)
        print("the decimal number of hexadecimal string: " + str(res))

        num = res

        binary = []

        while num != 0:
            if num % 2 == 0:
                num = num / 2
                binary.insert(0, 0)

            else:
                num = (num - 1) / 2
                binary.insert(0, 1)

        print("the binary number is: ", binary)
    except ValueError:
        print("numbers only")


def pass_creator():
    import random
    try:
        chart = "§±1!2@€3£#4$5%6^7&8*9(0)-_=+qwertyuiopasdfghjkl;'[]\`~zxcvbnm,<.>/?:|}{}"
        number = int(input("please enter the number of your password: "))

        length = int(input("please enter your password length: "))

        for e in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chart)
                print(password)

                f = open("password.txt", "w+")
                f.write(password)
                f.close()
    except ValueError:
        print("numbers only")


tro()

new = input("\n would you like to use it again == ")

while new == "yes" or new == "yh" or new == "sure" or new == "yeah":
    tro()
else:
    exit()
