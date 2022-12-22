# Initialize a variable to keep track of the current number of H's to print
num_hs = 1

# Loop through the rows of the pattern
for i in range(9):
  # Print spaces to center the pattern
  for j in range(9 - i):
    print(" ", end="")
  # Print the H's
  for j in range(num_hs):
    print("H", end="")
  # Increase the number of H's to print for the next row
  num_hs += 2
  # Move to the next line
  print()

# Print the bottom part of the pattern
print(" "*17 + "HHHHHHHHH")
print(" "*16 + "HHHHHHHH")
print(" "*17 + "HHHHHHHHH")

