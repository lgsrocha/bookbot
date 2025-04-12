def get_book_text(path):
    # TODO validate path
    with open(path) as book:
        return book.read()

def word_splitter(string, mode = ""):
    words = string.split()
    if mode == "count":
        return len(words)
    return words

def character_counter(words):
    character_count = {}
    characters = ""
    for word in words:
        characters = list(word)
        for character in characters:
            charactery = character.lower()
            if charactery in character_count:
                character_count[charactery] += 1
            else :character_count[charactery] = 1

    return character_count