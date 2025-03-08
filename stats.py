#Defining Book to Read
book = "books/frankenstein.txt"

#Opening the file:
def open_and_read_file(txt):
    with open(txt) as f:
        file_contents = f.read()
    return file_contents

#Counting words
def word_count(text):
    text = open_and_read_file(book)
    splitted_txt = str.split(text)
    wcount = len(splitted_txt)
    return wcount

def main():
    print(f"{word_count(book)} words found in the document")

main()