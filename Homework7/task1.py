import random
random.seed(2020)
random_ints = []
rand_dict = {}
for x in range(20):
    rand_int = random.randint(100,120)
    random_ints.append(rand_int)
    if rand_int not in rand_dict:
        rand_dict[rand_int] = 1
    else:
        rand_dict[rand_int] = rand_dict[rand_int] + 1
mode = [(0,0)]
for ints in rand_dict.keys():
    if rand_dict[ints] > mode[0][1]:
        mode = [(ints,rand_dict[ints])]
    elif rand_dict[ints] == mode[0][1]:
        mode.append((ints,rand_dict[ints]))
mode = [x[0] for x in mode]
random_ints.sort()
median = random_ints[9]
print(f'mode: ',end='')
for x in mode:
    print(x,end=' ')
print()
print(f'median: {median}')
