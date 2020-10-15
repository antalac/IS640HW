import random

def is_prime(num):
    for y in range(2, num):
        remain = num % y 
        if remain == 0:
            return False
    return True 

for x in range(6):
    random_num = random.randint(1, 100)
    if is_prime(random_num):
        print(f'The random number {random_num} is a prime number.')
    else:
        print(f'The random number {random_num} is not a prime number.')
