import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_dict



def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_count(text)
    #print(f"{num_words} words found in the document")
    #print(chars_dict)
    #print(sort_dict(chars_dict))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sort_dict(chars_dict):
        if entry["char"].isalpha() == True:
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    main()
