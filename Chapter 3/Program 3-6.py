# grader.py
# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named constats represnts the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade
if score >= A_SCORE:
    print('your grade is A!')
else:
    if score >= B_SCORE:
        print('Your grade is B')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                 print('Your grade is F. See me after class')