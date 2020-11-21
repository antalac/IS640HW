word_count = 0
char_count = 0
word_len_list = []
sentence_len_list = []

with open('speech.txt', 'r') as speech_file:
    data = speech_file.read()
    char_count = len(data)
    data = data.replace('\n', ' ')
    data = data.replace('-', ' ')

    total_chars = 0

    stripped_speech = ""

    data = data.replace("(Applause.)", "")
    for char in data:
        total_chars += 1
        if char.isalpha() or (char == ' ') or (char == '.'):
            stripped_speech = stripped_speech + char.lower()
    
    sentences = stripped_speech.split('.  ')

    worddict = {}
    for sentence in sentences:
        wordlist = sentence.split(' ')
        while("" in wordlist): 
            wordlist.remove("") 

        word_count += len(wordlist)
        sentence_len_list.append(len(wordlist))

        for word in wordlist:
            if word not in worddict:
                worddict[word] = 1
            else:
                worddict[word] = worddict[word] + 1
            word_len_list.append(len(word))

with open('summary.txt','w') as summary_file:
    
    sortedwordlist = sorted(worddict.keys(), key=len)
    top10 = sortedwordlist[-10:]
    top10 = top10[::-1]

    ly_words = []
    for key in worddict.keys():
        if key[-2:] == 'ly':
            ly_words.append(key)

    summary_file.write(f'Total Word Count: {word_count}\n')
    summary_file.write(f'Total character count: {char_count}\n')
    summary_file.write(f'The average word length: {sum(word_len_list)//len(word_len_list)}\n')
    summary_file.write(f'The average sentence length: {sum(sentence_len_list)//len(sentence_len_list)}\n')
    summary_file.write(f'\n')
    summary_file.write(f'A word distribution of all words ending in “ly”\n')
    for word in ly_words:
        summary_file.write(f'{word}: {worddict[word]}\n')
    summary_file.write(f'\n')
    summary_file.write(f'A list of top 10 longest words in descending order:\n')
    for word in top10[0:9]:
        summary_file.write(f'{word}, ')
    summary_file.write(f'{top10[-1]}')