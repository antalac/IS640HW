import random

rand = (random.randint(1, 9), random.randint(1, 9))
incorrect = True
while incorrect:
    inp = int(input(f'How much is {rand[0]} times {rand[1]}?'))
    if inp == rand[0] * rand[1]:
        incorrect = False
    else:
        print(f'{rand[0]} times {rand[1]} is not {inp}, please try again')
print('done')