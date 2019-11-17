#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program converts celcius to fahrenheit


def convert():
    # input
    numcheck = input("enter temperature (°C): ")

    # process
    try:
        numinput = int(numcheck)
        answer = numinput * 1.8 + 32

        # output
        print("{}°F".format(answer))
    except ValueError:
        print("invalid input")


def main():
    convert()


if __name__ == "__main__":
    main()
