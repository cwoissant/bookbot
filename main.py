from stats import get_num_words, count_characters, sorted_dict 
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]   
    contents = get_book_text(book_path)

    num_words = get_num_words(contents)

    num_chars = count_characters(contents)
    dict_list = sorted_dict(num_chars)

    report(num_words, dict_list)


def get_book_text(path):
    with open(path) as f:
        return f.read() 

def report(num_words, dict_list):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k in dict_list:
        print(f"{k['char']}: {k['num']}")
    print("============= END ===============")

main()
