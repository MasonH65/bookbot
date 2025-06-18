def get_words(book_text):
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def count_char(book_text):
    char_count = {}  
    lower_text = book_text.lower()
    for letter in lower_text:
        if letter in char_count:
            char_count[letter] +=1 
        else:
            char_count[letter] = 1
    return char_count

def sort_dict(char_count):
    num_dict = {}
    dict_list = []
    for char in char_count:
        num_dict = {'char': char, 'num': char_count[char]}
        dict_list.append(num_dict)
    dict_list.sort(reverse = True, key = lambda character: character['num'])
    return dict_list
    
