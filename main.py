from stats import get_book_text, word_splitter, character_counter

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words_count = word_splitter(book_text, "count")
    words = word_splitter(book_text)
    character_count = character_counter(words)
    print(f"{words_count} words found in the document")
    print(character_count)
    
main()  