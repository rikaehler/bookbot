def main():
    path_for_frankenstein = "books/frankenstein.txt"
    text = get_text(path_for_frankenstein)
    #print(text) // prints the entire document
    
    print()
    print(" - - - This is a report of books/frankenstein.txt - - -")
    word_count = get_number_of_words(text)
    print(f"{word_count} words found in the text")
    print()


    letter_dict = get_number_of_letters(text)
    #print(f"these are the numbers of letters found in the text: {letter_dict}")
    
    list_of_dicts = sort_on(letter_dict)
    for dict_ in list_of_dicts:
        for key, value in dict_.items():
            print(f"The letter '{key}' was found {value} times")
    
    print ()
    print ("- - - End report - - -")


# returns text from file as string
def get_text(path):
    with open(path) as f:
        return f.read()

# splits string with text and returns number of words   
def get_number_of_words(book):
    if book == "":
        return 0
    words = book.split()
    return len(words)

# counts individual letters if in alphabet (.isalpha()), return dict with number of letters
def get_number_of_letters(book):
    result = {}
    lowered_string = book.lower()
    for letter in lowered_string:
        if letter .isalpha() and letter not in result:
            result[letter] = lowered_string.count(letter)
    return result

def sort_on(unsorted_dict):
    # sort dict with lamba function in reverse (descending) order  
    sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))
    # create alist, add each key:value from sorted_dict into list of dictionaries 
    lst = [{letter: value for letter, value in sorted_dict.items()}]
    return lst
         
main()