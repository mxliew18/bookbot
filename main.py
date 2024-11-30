def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    sorted_chars = sort_characters(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char_info in sorted_chars:
        print(f"The '{char_info['char']}' character was found {char_info['count']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    for l in text:
        l = l.lower() 
        if l.isalpha():
            if l in characters:
                characters[l] += 1
            else:
                characters[l] = 1
    return characters

def sort_characters(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

def sort_on(dict):
    return dict["count"]



main()

