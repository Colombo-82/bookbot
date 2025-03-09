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
def count_characters(book):
    count = {}
    lower_case_text = str.lower(open_and_read_file(book))
    splitted_text = list(lower_case_text)
    for char in splitted_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def main():
    print(f"{word_count(book)} words found in the document")
    print(f"This is the count of every character in the Dictionary:")
    print(count_characters(book))

main()