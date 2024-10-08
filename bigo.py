"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Cherie Wang and Natnaele Gulte, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: cw43222
UT EID 2: ng26482
"""


def length_of_longest_substring_n3(s):
    """
    This function accepts a string s and should return the length of the longest
    substring of s which has all non-repeating characters. The Big O for this function must be O(N^3).
    """
    max_len = 0
    for i in range(len(s)): #starting index
        for j in range(i, len(s)): #ending index
            freq = [0] * 256
            substr = s[i:j+1] #substr inclusive
            count = 0
            for char in substr:
                index = ord(char)
                freq[index] += 1
                if freq[index]>1:
                    break
                count += 1
            if max_len < count:
                max_len = count
    if max_len == 0:
        max_len = len(s)
    return max_len


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.
    
    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
    in s that contains no repeating characters."""
    max_len = 0
    # Outer loop for the starting index
    for start in range(len(s)):
        current_length = 0
        for end in range(start, len(s)):
            is_valid = True
            for k in range(start, end + 1):
                for m in range(start, end + 1):
                    if s[k] == s[m] and k != m:
                        is_valid = False
                        break
                if not is_valid:
                    break
            if not is_valid:
                break
            current_length += 1

            max_len = max(max_len, current_length)


    return max_len


def length_of_longest_substring_n(s):
    """
    This function accepts a string s and should return the length of 
    the longest substring of s which has all non-repeating characters.
    The Big O for this function must be O(N).You may choose to challenge 
    yourself by implementing the sliding window approach for this 
    problem, which is O(N).
    """
    max_len = 0
    for i in range(len(s)): #starting index a
        freq = [0]*256
        count = 0
        for char in s[i:]: #ab
            index = ord(char)
            freq[index] += 1
            if freq[index] > 1:
                break
            count += 1
        max_len = max(max_len, count)
        current_char = s[i]
        char_index = ord(current_char)
        freq[char_index] -= 1
    return max_len
