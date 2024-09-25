# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0
    
    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print the asterisks in each row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after completing a row
        print()
        # Increment the row counter
        row += 1







