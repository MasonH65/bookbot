from stats import get_words, count_char, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_words(book_text)
    char_count = count_char(book_text)
    sorted_dict_list = sort_dict(char_count)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for dict in sorted_dict_list:
        if dict['char'].isalpha():
            print(f'{dict["char"]}: {dict['num']}')
    print('============= END ===============')
    
main()
