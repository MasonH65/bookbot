def get_words(book_text):
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
