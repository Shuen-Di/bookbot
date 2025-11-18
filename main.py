import sys
from stats import words_count, chars_count, sort_dict

if len(sys.argv) == 2:    
    input = sys.argv[1]
    #print(input)
else:
    print("Usage: python3 main.py <path_to_book>")    
    sys.exit(1)

#input = "books/frankenstein.txt"
def main():
    text = get_book_text(input)
    words = words_count(text)
    characters = chars_count(text)
    characters_list = sort_dict(characters)
    
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {input}...
    ----------- Word Count ----------
    Found {words} total words
    --------- Character Count -------
     """)   
    for item in characters_list:
        print(f"{item["char"]}: {item["num"]}")
    print("\n============= END ===============")
    return 

    
def get_book_text(f):
#Takes a filepath as input and returns the contents of the file as a string
    with open(f) as file:        
        return file.read()


    



main()