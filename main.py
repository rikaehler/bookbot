def main():
    path_for_frankenstein = "books/frankenstein.txt"
    text = get_text(path_for_frankenstein)

    #print(text) // prints the entire document
    
    word_count = get_number_of_words(text)
    print(f"{word_count} words found in the text")


    letter_count = get_number_of_letters(text)
    print(f"these are the numbers letters found in the text: {letter_count}")



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


          
main()