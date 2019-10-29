#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This takes two numbers
#  and prints which is greater


def main():
    while True:
        try:
            number1 = int(input("Please enter your first number: "))
            number2 = int(input("Please enter your second number: "))
            print()

            if number1 > number2:
                print(number1, "is greater")

            elif number2 > number1:
                print(number2, "is greater")

            else:
                print("Both numbers are equal")

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
