def main():
    report("books/frankenstein.txt")

def count_words(text):
    return len(text.split())


def char_dict(text):
    counts = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char not in counts:
            counts[lowered_char] = 1
        else:
            counts[lowered_char] += 1
    return counts


def report(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        print(f"--- Begin report of {file_name} ---")
        print(f"{count_words(file_contents)} words found in the document")
        print()
        letter_counts = char_dict(file_contents)
        letters = []
        for char in letter_counts:
            if char.isalpha():
                letters.append((letter_counts[char], char))
        letters.sort(reverse=True)
        for count, letter in letters:
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")


if __name__ == "__main__":
    main()
