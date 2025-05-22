def reverse_string(string):
    return f"Reversed_string: {string[::-1]}"




def count_vowels(string):
    count = 0
    for vowel in string:
        if vowel.lower() in 'aeiou':
            count += 1
    return f"Number counts: {count}"


