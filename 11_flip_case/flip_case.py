def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ""
    for char in phrase:
        if char.upper() == to_swap.upper():
            if(char.isupper()):
                char = char.lower()
            elif(char.islower()):
                char = char.upper()
            str = str + char
        else:
            str = str + char
    return str