def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        # 77986 words found in the document
        word_coount_result = word_count(file_contents)
        print(f"{word_coount_result} words found in the document")
        characters = count_characters(file_contents)
        # The 'e' character was found 46043 times
        for char in characters:
            print(f"The '{char}' character was found {characters[char]} times")
        print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = list(text)
    characters_dict = {}
    for char in characters:
        lower_char = char.lower()
        if lower_char in characters_dict:
            characters_dict[lower_char] += 1
        else:
            characters_dict[lower_char] = 1
    return characters_dict

main()