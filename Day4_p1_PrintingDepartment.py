# Given a 2D mapping of . and @, determine how many @'s have less than 4 @'s in the surrounding 8 slots
# E.g.
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# A forklift is only able to access an @ if there are less than 4 @'s surrounding it.
# The accessible @'s in the example become x's
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# There are 13 accessible @'s (x's), which is the expected output

# Outline
# Read the file
# Turn into a 2D array
# Check the size of the array (to reduce checks against edges/corners later)
# Iterate through each first array
    # Iterate through each second array
        # Check if the item is an @
            # Check the surrounding 8 spots, and count the number of @'s
            # If there are 4, break early (don't need to check if there are 5 or more)
            # If there are less than 4, mark the spot in a new array (to improve in the future)
                # Form of [[a,b], [c,d], [e,f], ...]
            # Check for edge, and check only the 5 required spots instead of all 8 (negative indexing issues?)
            # Check for corner, and don't check any spots (3 at most in any case, therefore always available)
            # Add 'timer' / number of checks left, as another earlier possible break (checking 5 spots that all return .'s means the last 3 don't need to be bothered with)



# Outline
# Read the file
# For Set 1:
    # Take each line
    # Add all numbers within range to an array containing all usable IDs
        # Make sure to not add duplicates
# For Set 2:
    # Take each line
    # Check if the line is within the array
    # If in array, add to available ingredients number (or array)
# Count available ingredients number (or count num of items in array)