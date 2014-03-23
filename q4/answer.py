def _next_letter(a_string, index):
    return a_string[index + 1]

def _is_last_leter(a_string, index):
    return len(a_string) -1 == index

def compact(a_string):
    new_string = ""
    temp_string = a_string.replace(" ", "")
    for index, character in enumerate(temp_string):
        if _is_last_leter(temp_string, index) or _next_letter(temp_string, index) != character:
            new_string += character

    return new_string

