#
#  Problem A: Counting Sheep
#  See README.md for problem details
#
#  Created by Trent Rand on 4/8/16.
#  Copyright 2016 Trent Rand. All rights reserved.
#

foundNumbers = []
testCases = input()


def record_digits(product):
    product_string = str(product)
    for digit in range(0, len(product_string)):
        if product_string[digit] not in foundNumbers:
            foundNumbers.append((product_string[digit]))


for testcase in range(1, int(testCases) + 1):
    startingDigit = input()

    # Handle special case (0*n is always = 0)
    if int(startingDigit) == 0:
        print("Case #" + str(testcase) + ": INSOMNIA")
    else:
        lastProduct = 1
        multiplier = 1
        while len(foundNumbers) < 10:
            lastProduct = int(startingDigit) * multiplier
            record_digits(lastProduct)

            multiplier += 1  # increment multiplier for next time

        print("Case #" + str(testcase) + ": " + str(lastProduct))
    foundNumbers = []  # reset <foundNumbers> for next testcase
