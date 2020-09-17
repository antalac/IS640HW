# Question 1

print('{: >20} {: >20} {: >20}'.format('Number','Square','Cube'))
for number in range (6):
    square = number * number
    cube = number * number * number
    print('{: >20} {: >20} {: >20}'.format (number, square, cube))

# Question 2

C_Value = [-40, 0, 40, 100]

for number in C_Value:
    print('The Fahrenheit conversion is', number * 9 / 5 + 32)

# Question 3

number1 = int(input('please enter your value'))
number2 = int(input('please enter another value'))
number3 = int(input('please enter a third value'))

vsum = number1 + number2 + number3
avg = vsum / 3

print('The sum is', vsum)
print(f'The average is: {avg:,.2f}')

