# retail_no_validation.py

# This program calculates prices.

MARK_UP = 2.5           # The markup percentage
another = 'y'           # Variable to control the loop.

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's " + "wholesale cost:"))

    # Calculate the retail price.
    retail = wholesale * MARK_UP

    # Display the retail price
    print('Retail price: $', format(retail, ',.2f'), sep='')

    # Do this again?
    another = input('Do you have another item? ' +
                    '(Enter y for yes):')