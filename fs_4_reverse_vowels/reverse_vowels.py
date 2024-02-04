import re
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = "" 
    for char in s:
        if char in "aeiouAEIOU": 
            vowels += char  
    result_string = ""  
    for char in s:
        if char in "aeiouAEIOU":  
            result_string += vowels[-1]  
            vowels = vowels[:-1]  
        else:
            result_string += char  
    return result_string
