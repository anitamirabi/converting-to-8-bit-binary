print("Input a number to convert it to 8-bit and to display how many 1s and 0s are in its 8-bit expression.")
for i in range(256):
    # Allows the user to convert up to 256 numbers without having to restart the program.
    list1 = []
    # Declares the list. This list will be used to collect each binary bit and its boolean value, except in this code it is technically an integer value.
    integerInput = float(input())
    # The user has the freedom to input a decimal or integer, as the displayed text only specifies a number, however if they input a decimal they will be met with an error message explaining why it's not possible.
    values = [integerInput / 128,
    integerInput / 64,
    integerInput / 32,
    integerInput / 16,
    integerInput / 8,
    integerInput / 4,
    integerInput / 2]
    # These values allowed me to find a concise way of expressing the forecoming inequality. They correspond to the 1st digit, 2nd digit etc. of the final binary number. I have chosen to only implement the first 7, because the 8th digit tells you whether the number is even or odd, and there was an easier method for that which saves processing time, the reason for this is, as you see later in the code each value in (values) goes through a loop that iterates 64 times.
    valuesIndex = len(values)
    # I intended to use the index of my list and discovered through debugging that it was not possible to articulate what I wanted - to the computer, without first establishing the index, and then asking for the computer to go through it, as opposed to just asking the computer to go through the list, which is why the variable valuesIndex is important. 
    if (integerInput > 255) or (integerInput < 0) or (integerInput % 1 > 0):
        print("error: number can't be expressed in 8-bit; has to be a postive integer from 1-255")
        # 8-bit binary code is usually interpreted as a positive integer from 0-255. 
        # The first expression, (integerInput > 255), checks whether the number is above 255.
        # The second, (integerInput < 0), checks whether it is a negative number.
        # The last expression, (integerInput % 1 > 0), checks whether there is a decimal point in the number.
        # If any of these expressions are true, then an error message is outputted, as the input cannot be expressed in 8-bit.
    else:
        for index in range (valuesIndex):       
            # This iterates each value in the list values until it is decided whether the current digit is a 1 or 0. When it is decided, either a 1 or 0 is appended onto my list.
            currentDigit = None
            # Defines currentDigit as a boolean value. This value is used structurally so that I had minimal nested If statements.
            for y in range(1, 65):
                if (y * 2) > values[index] >= (y * 2 - 1):
                    # If this statement is true, the item corresponding to the current index in the list (values), is in place of a 1. Referring to the fact that each item in (values) corresponds to one of the 8 final digits.
                    # The next few comments explain this If statement further and why/how I implemented it. 
                    # While trying to individually write a series of mathematical inequalities for my code, I discovered that it could be simplified (using some sort of loop) and went on to create this concise expression that checks whether each value falls in to the range where it would need to be 1. I created this by identifying the specific pattern formation in my manually written inequalities, which began:
                    # (if (2 > digit8 >= 1) or (4 > digit8 >= 3) or (6 > digit8 >= 5))
                    # As you can see the value on the left side of each inequality is a multiple of 2 and on the right is that number minus 1; (y * 2) > x >= (y * 2 - 1).
                    # Although not neccesary to the code, I believe the reason that the statement works can be explained, fairly simply, in that: if a number divided by x is equal or greater than the nearest odd counterpart but smaller than the nearest even counterpart then it must contain an odd number of x. This ignores any decimal places in the number as a range is given. 
                    # This is specified to the computer, in a way, because of its oddness and therefore inability to be simplified. This saves space and time.
                    currentDigit = True
                    # I previously nested the following If statement here but that made it quite complicated and did not work. I believe due to the 2 For loops, the If statement was iterating too many times, around 63 too many, for each value.
                    break
            if currentDigit == True:
                list1.append(1)
                currentDigit = None
                # If the statement came out as true, then 1 is appended to the list.
            elif currentDigit == None:
                list1.append(0)
                currentDigit = None
                # If not then 0 is appended to the list.
        if integerInput % 2 == 1:
            list1.append(1)
            # This is where the 8th digit is implemented, the modulo operation specifically checks whether the number is odd or even, when used with the number 2, if it is odd, it gives a 1, if not, it gives a 0.
        elif integerInput % 2 == 0:
            list1.append(0)
        print(*list1, sep="")
        # The list would print with [] brackets and commas in between without these parameters. Like this: [0, 0, 0, 0, 0, 0, 0, 0]
        amount1 = str(list1.count(1))
        amount0 = str(list1.count(0))
        print("Number of 1s: " + amount1 + "\nNumber of 0s: " + amount0)
        # These lines of code tell you how many 1s or 0s are in the 8-bit value.