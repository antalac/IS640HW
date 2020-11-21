with open('book.txt', 'r') as book_file:
    letter_dict = {}
    for line in book_file:
        for char in line:
            if char.isalpha():
                capital = char.upper()
                if capital in letter_dict:
                    letter_dict[capital] = letter_dict[capital] + 1
                else:
                    letter_dict[capital] = 1

with open('summary.txt','w') as summary_file:
    for key in letter_dict.keys():
        summary_file.write(f'{key}: {letter_dict[key]}\n')
    summary_file.write(f'\n')
    if len(letter_dict.keys()) == 26:
        summary_file.write('it contains all letters')
    else: 
        summary_file.write('it does not contains all letters')