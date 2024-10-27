# loan_qualifier
# This program determines whether a bank customer
# qualifies for a loan.

MIN_Salary = 30000.0    # the minimum annual salary
MIN_YEARS = 2           # The minimumn years on the job

# Get the customer's annual salary
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.

years_on_job = int(input('Enter the number of ' + 'years employed: '))

# Determine whether the custome qualifies.

if salary >= MIN_Salary:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', 'for at least', MIN_YEARS, 'years to qualify.')
    
else:
    print('You must earn at least $', format(MIN_Salary, ',.2f'), ' per year to qualify.', sep='')