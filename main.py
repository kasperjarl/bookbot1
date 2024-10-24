def main():
    book_path ="./books/frankenstein.txt"

    # Print the book text
    text = get_book_text(book_path)
    # print(text)

    # Print the number of words
    num_words = count_words(text)
    #print(num_words)

    # Print the number of each char
    num_chars = count_chars(text)
    #print(num_chars)


    ### Print a report ###
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} was found in the document")
    
    for char in num_chars:
        print(f"The '{char}' was found {num_chars[char]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_chars(text):
    counter = 0
    lower_case_text = text.lower()
    chars_dict = {}

    for char in lower_case_text:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

### NÅET HERTIL HVOR DU SKAL SORT DIN DICT ###

main()