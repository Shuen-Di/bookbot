def words_count(t):
#Takes a string as input and returns the number of words in the string
    w = t.split()
    return len(w)

def chars_count(c):
#Takes a string as input and returns how many times each characters appears in the string
    c = str.lower(c)
    char_dict = {}
    char_count = 0
    for char in c:
        if char in char_dict:
            char_dict[char] += 1

        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(d):
#Takes a dictionary remove non alpha keys and sort it in a decreasing order of values    
    dict_list = []
    for key, value in d.items():
        new_dict = {"char": key, "num": value}
        for item in new_dict:
            char = new_dict["char"]            
            num = new_dict["num"]
        if str(char).isalpha():        
            dict_list.append(new_dict)
        dict_list.sort(key=sort_on, reverse=True)
    return dict_list