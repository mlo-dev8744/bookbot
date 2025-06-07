def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_dict(dict):
    sorted_list = []
    for key, value in dict.items():
        sorted = {"char":key, "num": value}
        sorted_list.append(sorted)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list