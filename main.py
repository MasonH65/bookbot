from stats import get_words, count_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_words(book_text)
    char_count = count_char(book_text)
    print(word_count,char_count)
    
main()
