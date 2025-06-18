from stats import get_words, count_char, sort_dict
import sys 

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(book_path)
    word_count = get_words(book_text)
    char_count = count_char(book_text)
    sorted_dict_list = sort_dict(char_count)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for dict in sorted_dict_list:
        if dict['char'].isalpha():
            print(f'{dict["char"]}: {dict['num']}')
    print('============= END ===============')
    
main()
