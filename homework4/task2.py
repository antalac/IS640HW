import random

def rand_tuple():
    rand_tup = (random.randint(1, 9), random.randint(1, 9))
    return rand_tup

rand = rand_tuple()
incorrect = True
while incorrect:
    inp = int(input(f'How much is {rand[0]} times {rand[1]}?'))
    if inp == rand[0] * rand[1]:
        incorrect = False
    else:
        print(f'{rand[0]} times {rand[1]} is not {inp}, please try again')
print('done')