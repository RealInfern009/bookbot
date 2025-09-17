def get_num_words(book_path):
    with open(book_path) as f:
        characters = {}
        book_content = f.read()

        for letter in book_content:
            lower_case_letter = letter.lower()
            if lower_case_letter in characters:
                characters[lower_case_letter] += 1
            else:
                characters[lower_case_letter] = 1        

        num_words = book_content.split()


        return len(num_words),characters

def sort(dictionary):
    sorted_list = []

    for letter in dictionary:
        amount = dictionary[letter]
        new_entry = {
            "char": letter,
            "num": amount,
        }

        sorted_list.append(new_entry)

    sorted_list.sort(key=lambda x: x['num'],reverse = True)

    for letter in sorted_list:
        print(f"{letter["char"]}: {letter['num']}" )


    return sorted_list