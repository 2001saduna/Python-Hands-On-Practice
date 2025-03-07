'''
Problem: Text Analyzer

Write a Python function called analyze_text that takes a string as input and returns a dictionary containing the following information:

word_count: The total number of words in the string.
character_count: The total number of characters in the string (including spaces and punctuation).
unique_words: A list of unique words found in the string (case-insensitive).
word_frequency: A dictionary where the keys are unique words (case-insensitive), 
and the values are the number of times each word appears in the string.

dictionary:

users = {
    "name" : "Melody",
    "age" : 23
}
'''
text = "The sun comes up and the sun goes down. The sun comes up and the sun goes down. This is the sun going down."

# def analyze_text(text):
#     word_count = len(text.split())
#     character_count = len(text)
#     unique_words = list(set(text.split()))
#     word_frequency = {}
    
#     for word in unique_words:
#         word_frequency[word] = text.lower().split().count(word)
    
#     print(f"This is word count:{word_count},\nThis is charcter count:{character_count},\nThis is number of unique words:{unique_words},\nThis is word frequency:{word_frequency}")

#     return word_count, character_count, unique_words, word_frequency



'''model Answer'''

import string

def analyze_text(text):
    """Analyzes text and returns word count, character count, unique words, and word frequency."""

    # Remove punctuation and lowercase the text
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    word_count = len(words)
    character_count = len(text)
    unique_words = list(set(words))
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    result = {
        'word_count': word_count,
        'character_count': character_count,
        'unique_words': unique_words,
        'word_frequency': word_frequency,
    }
    print(result)
    return result

analyze_text(text)