
# 3.17 (a)

print('(a)')
rows = 10
for x in range(1, rows+1):
    print("*" * x)

print("")

# 3.17 (b)

print('(b)')
rows = 10
for x in range(rows + 1, 0, -1):
    for y in range(0, x - 1):
        print("*", end='')
    print(" ")   

# 3.17 (c)

print('(c)')

rows = 10
for x in range(1, rows + 1):
    for y in range(1, x):
        print(' ', end='')
    for y in range(x,11):
        print('*', end='')
    print('')

# 3.17 (d)

print('(d)')

rows = 10
for x in range(rows, 0, -1):
    for y in range(1,x):
        print(' ', end='')
    for y in range(x,11):
        print('*', end='')
    print('')