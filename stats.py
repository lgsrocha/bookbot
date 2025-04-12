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
            elif f"{charactery}".isalpha(): 
                character_count[charactery] = 1

    return character_count

def dic_sort(dic):
    sorted_dic = (dict(sorted
                       (dic.items(), 
                        key=lambda 
                        item: item[1], 
                        reverse=True)))
    return sorted_dic

def formated_info(words_count, file_path, character_count):
    report = ""
    report += "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file_path}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {words_count} total words\n"
    report += "--------- Character Count -------\n"
    sorted_dic = dic_sort(character_count)
    for keys in sorted_dic:
        report += f"{keys}: {sorted_dic[keys]}\n"
    report += "============= END ==============="
    return report