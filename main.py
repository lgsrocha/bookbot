import sys
from stats import get_book_text, word_splitter, character_counter, formated_info



def main():
    if (len(sys.argv)) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath=sys.argv[1]
    book_text = get_book_text(filepath)
    words_count = word_splitter(book_text, "count")
    words = word_splitter(book_text)
    character_count = character_counter(words)
    
    print(formated_info(words_count,filepath,character_count))

main()  