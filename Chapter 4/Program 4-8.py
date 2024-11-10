# squares.py
# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# print the table headins
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.

for number in range(1,11):
    square = number**2
    print(number, '\t', square)