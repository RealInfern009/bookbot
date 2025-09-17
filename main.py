from stats import get_num_words
from stats import sort
import sys

def main():

    arguments = sys.argv
    print(1 in arguments)
    if len(arguments) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = arguments[1]

    characters, dictionary = get_num_words(book_path)
    sorted_dictionary = sort(dictionary)
    
    print(sorted_dictionary)
    print(f"Found {characters} total words")
    sys.exit(0)
def get_book_text(book):
    pass


main()