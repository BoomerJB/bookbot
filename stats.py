def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

def count_characters(text):
	text = text.lower()
	char_counts = {}
	for char in text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Skip non-alphabet characters
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list

main()
