zeroes = 0
dialNumber = 50
# dialInstructions = open('Day1_Dial.txt', 'r')
dialInstructions = open('Day1_Example.txt', 'r')
instructionOutput = open('DialOutput.txt', 'w')

print("The dial starts by pointing at", dialNumber)
instructionOutput.write("The dial starts by pointing at " + str(dialNumber) + "\n\n")

for dialLine in dialInstructions:
    if dialLine[0] == "L":
        dialNumber -= int(dialLine[1:])
        print(dialLine[1:])
    elif dialLine[0] == "R":
        dialNumber += int(dialLine[1:])
        print(dialLine[1:])
    if dialNumber < 0 or dialNumber > 100:
        print("Dial number outside of 0-100:", dialNumber)
        instructionOutput.write("Dial number outside of 0-100: " + str(dialNumber) + "\n")
        extrazeroes = abs(int(dialNumber / 100))
        if dialNumber < 0:
            extrazeroes += 1
        zeroes += extrazeroes
        print("There are", extrazeroes, "extra zeroes")
        instructionOutput.write("There are " + str(extrazeroes) + " extra zeroes\n")
    dialNumber = dialNumber % 100
    if dialNumber == 0:
        zeroes += 1
    print ("The dial is rotated", dialLine, "to point at", dialNumber, ".")
    instructionOutput.write("The dial is rotated " + str(dialLine) + " to point at " + str(dialNumber) + ".\n")
    print ("There are", zeroes, "zeroes")
    instructionOutput.write("There are " + str(zeroes) + " zeroes\n\n")