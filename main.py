
def count_words(file_contents: str) -> int:
    return len(file_contents.split()) 


def open_book(file_name: str) -> str:
    with open(f"books/{file_name}.txt", "r") as f:
        return f.read()

'''
def count_char(file_contents: str) -> dict:
    letters_used = set()
    for char in file_contents:
        if char.lower().isalpha():
            letters_used.add(char.lower())
    count_dict = {}
    for char in letters_used:
        count_dict[char] = file_contents.count(char)
    return count_dict
'''

def count_char(file_contents: str) -> list:
    letters_used = {char.lower() for char in file_contents if char.lower().isalpha()}
    char_dict = {char: file_contents.count(char) for char in letters_used}
    new_list = []
    for letter, count in char_dict.items():
        new_list.append({"letter": letter, "count": count})
    return sorted(new_list, key=lambda x: x["count"], reverse=True)


def display_report(file_name:str , word_count: int, sorted_list: list):
    print(f"--- Begin report of books/{file_name}.txt--- ")
    print(f"{word_count} words found in the document\n")
    for char_info in sorted_list:
        print(f"The '{char_info["letter"]}' character was found {char_info["count"]} times")
    print("--- End report ---")


def main():
    contents = open_book("frankenstein")
    count = count_words(contents)
    char_dict = count_char(contents)
    display_report("frankenstein", count, char_dict)

main()


