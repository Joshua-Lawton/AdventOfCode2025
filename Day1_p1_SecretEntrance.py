print("Hello World")

# Find secret entrance by rotating the Dial based on L/R[n]
# The Dial starts at 50, and has a range of 0-99 (inclusive)
# Due to being a rotating Dial, 0 and 99 are next to each other
# The aim is to go through all rotations, and count the number of times a 0 appears

# Outline
# Count the zeroes
# Start at 50
# Read the file
# Loop through each set
# Check the associated letter
# Either + or - based on R or L
# Add to number
# Check if 0
#   Add to zeroes
# repeat
# return zeroes when file is complete

zeroes = 0
dialNumber = 50
dialInstructions = open('Day1_Dial.txt', 'r')
# dialInstructions = open('Day1_Example.txt', 'r')
instructionOutput = open('DialOutput.txt', 'w')

print("The dial starts by pointing at", dialNumber)
instructionOutput.write("The dial starts by pointing at " + str(dialNumber) + "\n")

for dialLine in dialInstructions:
    if dialLine[0] == "L":
        dialNumber -= int(dialLine[1:])
        print(dialLine[1:])
    elif dialLine[0] == "R":
        dialNumber += int(dialLine[1:])
        print(dialLine[1:])
    dialNumber = dialNumber % 100
    if dialNumber == 0:
        zeroes += 1
    print ("The dial is rotated", dialLine, "to point at", dialNumber, ".")
    instructionOutput.write("The dial is rotated " + str(dialLine) + " to point at " + str(dialNumber) + ".\n")
    print ("There are", zeroes, "zeroes")
    instructionOutput.write("There are " + str(zeroes) + " zeroes\n")
