# Name: Rakshith Jayakarthikeyan
# Assignment: PROG1003 - HW7 - Spelling

def load_words(filename):
    word_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word != "":
                word_list.append(word)
    return word_list


def clean_word(word):
    # remove punctuation and convert to lowercase
    word = word.strip().lower()
    cleaned = ""
    for ch in word:
        if ch.isalpha():
            cleaned += ch
    return cleaned


def check_spelling(text_file, dict_file):
    dictionary = set(load_words(dict_file))
    misspelled = []
    correct_counts = {}

    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                w = clean_word(word)
                if w == "":
                    continue
                if w not in dictionary:
                    misspelled.append(w)
                else:
                    if w not in correct_counts:
                        correct_counts[w] = 1
                    else:
                        correct_counts[w] += 1

    # write misspelled words
    with open("misspelled_words.txt", "w", encoding="utf-8") as out:
        for word in misspelled:
            out.write(word + "\n")

    # write correct words and counts
    with open("correct_words.txt", "w", encoding="utf-8") as out:
        for word, count in sorted(correct_counts.items()):
            out.write(f"{word} {count}\n")

    print("The following words are not spelled correctly:")
    for word in misspelled:
        print(word)


def main():
    filename = input("Enter file name: ").strip()
    check_spelling(filename, "words")


if __name__ == "__main__":
    main()