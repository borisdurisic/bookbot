def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dic = {}
    for c in text:
        char = c.lower()
        if char_dic.get(char) == None:
            char_dic[char] = 1
        else:
            char_dic[char] += 1
    
    return char_dic