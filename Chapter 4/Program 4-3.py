# Infinite_loop.py
# This program demonstrates an infinite loop.
# Create a variable to control the loop.

keep_going = 'y'

# WARNING!!! INFINITE LOOOP!!!!!
while keep_going == 'y':
    # Get a salesperson's sales and commisiion rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the comission rate: '))

    # Calculate the commission.

    commission = sales * comm_rate

    # Display the commission
    print('The commission is $',  format(commission, ',.2f'),sep='')