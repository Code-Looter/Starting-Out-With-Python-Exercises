# test_average.py
# This program gets three test scores and siplays
# their average. It congratulates the use if the
# average is a high score.

# The HIG_SCORE named constant holds the value that is
# considered a ghigh score.

HIGH_SCORE = 95

# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# if the average is a high score
# congratulate the user.
if average >= HIGH_SCORE:
    print('CONGRATULATIONS!!!!')
    print('That is a great average')