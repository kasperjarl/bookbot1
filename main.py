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
    
    num_chars.sort(reverse=True, key=sort_on)
    
    list_of_dict = []
    for pair in num_chars:
        list_of_dict.append(pair)
    for pair in list_of_dict:
        print(f"The {pair['char']} character was found {pair['num']} times")

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
    lower_case_text = text.lower()
    chars_dict = {}

    for char in lower_case_text:
        if char.isalpha() == True:
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

    char_list = []
    for char, num in chars_dict.items():
        char_info = {"char": char, "num": num}
        char_list.append(char_info)
    return char_list

### NÅET HERTIL HVOR DU SKAL SORT DIN DICT ###
def sort_on(dict):
    return dict["num"]

main()