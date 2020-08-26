def is_palindrome(word):
    clean_word = ''
    for letter in word.lower():
        if letter.isalnum():
            clean_word += letter
    return clean_word == clean_word[::-1]
