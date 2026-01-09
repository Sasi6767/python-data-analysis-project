import re
from collections import Counter


def fun1(s):
    """
    Returns True if the given string is a palindrome, ignoring spaces but considering case sensitivity.
    """
    cleaned_s = ''.join(
        s.split())  # Remove all spaces from the string to ensure spacing does not affect palindrome check
    return cleaned_s == cleaned_s[::-1]  # Reverse the string and compare it with the original


def fun2(s):
    """
    Converts the string to upper case and returns the second-most frequent letter/digit.
    """
    s = s.upper()  # Convert entire string to uppercase for uniformity
    filtered_chars = [char for char in s if char.isalnum()]  # Extract only alphanumeric characters

    if len(set(filtered_chars)) < 2:  # Check if there are at least two unique characters
        return None  # If not, return None as there is no second most frequent character

    freq_counter = Counter(filtered_chars)  # Count frequency of each alphanumeric character
    most_common = freq_counter.most_common()  # Get sorted list of characters based on frequency
    return most_common[1][0] if len(most_common) > 1 else None  # Return second most frequent character if it exists


def fun3(s):
    """
    Counts the number of uppercase letters, lowercase letters, and digits in the string.
    Returns a tuple (uppercase_count, lowercase_count, digit_count).
    """
    upper_count = sum(1 for char in s if char.isupper())  # Count uppercase letters
    lower_count = sum(1 for char in s if char.islower())  # Count lowercase letters
    digit_count = sum(1 for char in s if char.isdigit())  # Count numerical digits

    return (upper_count, lower_count, digit_count)  # Return the counts as a tuple
