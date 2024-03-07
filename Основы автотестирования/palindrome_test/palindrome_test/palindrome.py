def palindrome(my_str):
    stripped_str = "".join(letter.lower() for letter in my_str if letter.isalpha())
    return stripped_str == stripped_str[::-1]
