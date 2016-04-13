#
#  Problem A: Counting Sheep
#  See README.md for problem details
#
#  Created by Trent Rand on 4/8/16.
#

# Flip pancake subsection and return
def flipPancakes(pancakeSubsection):
    pancakeSubsection = pancakeSubsection[::-1]
    print(pancakeSubsection)
    return pancakeSubsection


# Correct pancake stack so all happy sides up
def correctPancakes(pancakeStack):
    # track number of maneuver required to get all the pancakes happy side up.
    operations = 0

    # manipulate pancake stack until all pancakes are +
    while ('-' in pancakeStack):
        operations += 1

    return operations


testCases = input()  # read number of test cases
for testcase in range(1, int(testCases) + 1):
    pancakeStack = input()

    # Manipulate pancakeStack until all pancakes are happy side up (+)
    # operations = correctPancakes(pancakeStack)
    # print("Case #" + str(testcase) + ": " + str(operations))
