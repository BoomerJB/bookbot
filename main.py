import sys
from stats import count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()
