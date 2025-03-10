#Defining Book to Read
book = "books/frankenstein.txt"

#Opening the file:
def open_and_read_file(book):
    with open(book) as f:
        file_contents = f.read()
    
    return file_contents

#Spliting Text into words
def spliting_text_words(book):
    text = open_and_read_file(book)
    splitted_txt = str.split(text)
    
    return splitted_txt

#Counting words
def word_count(text):
    splitted_txt = spliting_text_words(text)
    wcount = len(splitted_txt)
    
    return wcount

#Dictionary with character counts
def characters_dictionary(book):
    char_dict = {}
    lower_case_text = str.lower(open_and_read_file(book))
    splitted_text = list(lower_case_text)
    
    for char in splitted_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

#Sorting
def sorting_dictionary(book):
    char_dict = characters_dictionary(book)
    list_of_dicts = []
    
    for char in char_dict:
        list_of_dicts.append({"character" : char, "count" : char_dict[char]})
    
    def sort_on(dict):
        return dict["count"]
    
    list_of_dicts.sort(reverse = True, key = sort_on)

    return list_of_dicts
    

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")

    sorted_chars = sorting_dictionary(book)
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()