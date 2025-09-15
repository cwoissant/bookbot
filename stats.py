def get_num_words(contents):
    return len(contents.split()) 

def count_characters(contents):
    chars = {}
    
    for c in contents:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else: 
            chars[c] = 1
    return chars
        
def sort_on(items):
    return items["num"]

def sorted_dict(chars):
    char_list = []

    for k in chars:
        if k.isalpha():
            char_list.append({"char": k, "num": chars[k]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list 
