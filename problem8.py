import string

def strip_list(document):
    f = open(document, 'r')
    #entire_file = f.read()
    #entire_file.strip()
    #print entire_file
    clean_text = []
    for line in f:
        #print line
        clean_line = line.strip()
        #print clean_line
        clean_line = clean_line.lower()
        #print clean_line
        clean_line = clean_line.translate(None, string.punctuation)
        clean_line = clean_line.split()
        clean_text += clean_line
    print clean_text,
    return clean_text
    f.close()


def strip_text(document):
    f = open(document, 'r')
        #entire_file = f.read()
        #entire_file.strip()
        #print entire_file
    clean_text = ''
    for line in f:
            #print line
        clean_line = line.strip()
            #print clean_line
        clean_line = clean_line.lower()
            #print clean_line
        clean_line = clean_line.translate(None, string.punctuation)
        #print clean_line.split()
        clean_text += clean_line
        #clean_text = clean_text.split()
    print clean_text,
    return clean_text
    f.close()


word_list = './common_words_100.txt'
speech = './speech.txt'

#strip_text(speech)
#strip_list(speech)



def remove_common(text, remove):
    words_to_check = strip_list(remove)
    text_to_change = strip_list(text)
    for words in words_to_check:
        if words in text_to_change:
            text_to_change = text_to_change.remove(words)
    print text_to_change
    return text_to_change

remove_common(speech, word_list)
