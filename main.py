def main():
    book_path = "books/frankestien.txt"
    text = get_book_text(book_path)
    words = words_count(text=text)
    char_map = char_count(text=text)
    char_sorted_list = chars_dict_to_sorted_list(char_map)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def words_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lower_text = text.lower()
    char_count_map = {}
    
    for char in lower_text:
        char_count_map[char] = char_count_map.get(char, 0) + 1
    return char_count_map

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(nums_char_dict):
    sorted_list = []
    for char in nums_char_dict:
        sorted_list.append({"char" : char, "num" : nums_char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
