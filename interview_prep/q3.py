'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example

"abcde" -> 0  # no characters repeats more than once
"aabbcde" -> 2  # 'a' and 'b'
"aabBcde" -> 2  # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1  # 'i' occurs six times
"Indivisibilities" -> 2  # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2  # 'a' and '1'
"ABBA" -> 2  # 'A' and 'B' each occur twice
'''

# my solution
def duplicate_count(text):
    if text == "":
        return 0
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
            
    count = 0
    for value in char_dict.values():
        if value > 1:
            count += 1
    return count


# modal gemini solution
def duplicate_count(text):
    """
    Counts the number of distinct case-insensitive alphabetic characters and
    numeric digits that occur more than once in the input string.

    Args:
        text (str): The input string to check for duplicates.

    Returns:
        int: The count of distinct characters/digits that appear more than once.
    """
    # Handle the edge case of an empty string immediately.
    if not text:
        return 0

    # Use a dictionary (hash map) to store the frequency of each character.
    # Convert the entire text to lowercase once to handle case-insensitivity
    # and simplify character comparison within the loop.
    char_counts = {}
    for char in text.lower():
        # Only consider alphabetic characters and numeric digits as per common problem definitions.
        # If any character (including spaces, symbols) should be counted, remove this 'if' condition.
        if char.isalnum(): # Checks if the character is alphanumeric (letter or number)
            char_counts[char] = char_counts.get(char, 0) + 1

    # Initialize a counter for distinct duplicate characters.
    duplicate_chars_count = 0

    # Iterate through the values (counts) in the dictionary.
    # If a character's count is greater than 1, it means it's a duplicate.
    for count in char_counts.values():
        if count > 1:
            duplicate_chars_count += 1

    return duplicate_chars_count


# modal chatgpt solution
def duplicate_count(text):
    char_dict = {}
    for char in text.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return sum(1 for count in char_dict.values() if count > 1)