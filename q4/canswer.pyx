from libc.stdlib cimport realloc, malloc

def ireplace(char *a_string):
    counter = 0
    while counter < len(a_string):
        current_char = <char>a_string[counter]
        next_char = <char>a_string[counter + 1]
        if next_char == ' ' or current_char == next_char:
            #shift up 
            for i in range(counter + 1, len(a_string)):
                a_string[i] = a_string[i+1]
        else:
            counter += 1

    #a_string = <char*>malloc((len(a_string)-3) * sizeof(char))
    #a_string = <char*>realloc(a_string, len(a_string) * sizeof(char))
    #memmove(a_string, a_string, len(a_string))



