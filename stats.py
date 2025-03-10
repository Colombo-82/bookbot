#Opening the file:
def open_and_read_file(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

#Spliting Text into words
def spliting_text_words(book_path):
    text = open_and_read_file(book_path)
    splitted_txt = str.split(text)
    
    return splitted_txt

#Counting words
def word_count(book_path):
    splitted_txt = spliting_text_words(book_path)
    wcount = len(splitted_txt)
    
    return wcount

#Dictionary with character counts
def characters_dictionary(book_path):
    char_dict = {}
    lower_case_text = str.lower(open_and_read_file(book_path))
    splitted_text = list(lower_case_text)
    
    for char in splitted_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

#Sorting
def sorting_dictionary(book_path):
    char_dict = characters_dictionary(book_path)
    list_of_dicts = []
    
    for char in char_dict:
        list_of_dicts.append({"character" : char, "count" : char_dict[char]})
    
    def sort_on(dict):
        return dict["count"]
    
    list_of_dicts.sort(reverse = True, key = sort_on)

    return list_of_dicts
    

def main(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_path)} total words")
    print("--------- Character Count -------")

    sorted_chars = sorting_dictionary(book_path)
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")