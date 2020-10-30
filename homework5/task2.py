summaryfile = open('homework5/summary.txt', 'w')
# try:
file1 = open('homework5/book.txt', 'r')
Lines = file1.readlines()
charcount = [0] * 26
for line in Lines:
    chars = list(line)
    for char in chars:
        if char.isalpha():
            charNum = ord(char.upper()) - 65
            # print(index)
            if charcount[charNum]:
                charcount[charNum] = charcount[charNum] + 1
            else:
                charcount[charNum] = 1
print(charcount)

allletters = True
for x in range(26):
    #final = x + 65
    if charcount[x] > 0:
        letter = chr(x + 65)
        summaryfile.write(f'{letter} {charcount[x]}\n')
    else:
        allletters = False

if allletters:
    summaryfile.write(f'It has all letters.')
else:
    summaryfile.write(f'It doesnt have all letters.')
summaryfile.close()