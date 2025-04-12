def get_book_text(path):
    # TODO validate path
    with open(path) as book:
        return book.read()

def word_count(string):
    words = string.split()
    return len(words)        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")
    
main()  