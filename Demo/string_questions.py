# 1. Reverse a string  
# (a) Using built-in function  
def reverse_string_builtin(s):
    return s[::-1]

# (b) Using for loop  
def reverse_string_manual(s):
    res = ""
    for char in s:
        res = char + res
    return res


# 2. Count vowels in a string  
# (a) Using built-in function  
def count_vowels_builtin(s):
    return sum(map(s.lower().count, "aeiou"))

# (b) Using for loop  
def count_vowels_manual(s):
    count = 0
    for c in s.lower():
        if c in "aeiou":
            count += 1
    return count


# 3. Remove duplicate characters from a string  
# (a) Using built-in function  
def remove_duplicates_builtin(s):
    return "".join(dict.fromkeys(s))  # Maintains order

# (b) Using for loop  
def remove_duplicates_manual(s):
    seen, res = set(), ""
    for c in s:
        if c not in seen:
            seen.add(c)
            res += c
    return res


# 4. Count words in a string  
# (a) Using built-in function  
def count_words_builtin(s):
    return len(s.split())

# (b) Using for loop  
def count_words_manual(s):
    count, in_word = 0, False
    for c in s:
        if c.isspace():
            in_word = False
        elif not in_word:
            count += 1
            in_word = True
    return count


# 5. Capitalize the first letter of each word  
# (a) Using built-in function  
def capitalize_words_builtin(s):
    return s.title()

# (b) Using for loop  
def capitalize_words_manual(s):
    words = s.split()
    res = []
    for word in words:
        res.append(word[0].upper() + word[1:])
    return " ".join(res)


# 6. Find the longest word and return its length  
# (a) Using built-in function  
def longest_word_length_builtin(s):
    return max(map(len, s.split()))

# (b) Using for loop  
def longest_word_length_manual(s):
    max_len = 0
    for word in s.split():
        if len(word) > max_len:
            max_len = len(word)
    return max_len


# 7. Check if one string is a rotation of another  
# (a) Using built-in function  
def is_rotation_builtin(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

# (b) Using for loop  
def is_rotation_manual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    return False


# 8. Compress a string using counts of repeated characters  
# (a) Using built-in function  
from itertools import groupby
def compress_string_builtin(s):
    return "".join(f"{k}{len(list(g))}" for k, g in groupby(s))

# (b) Using for loop  
def compress_string_manual(s):
    res, count = "", 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            res += s[i] + str(count)
            count = 1
    res += s[-1] + str(count)
    return res if len(res) < len(s) else s


# 9. Length of longest substring without repeating characters  
# (a) Using built-in function  
def longest_unique_substring_builtin(s):
    from collections import Counter
    res, left = 0, 0
    seen = Counter()
    for right in range(len(s)):
        seen[s[right]] += 1
        while seen[s[right]] > 1:
            seen[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

# (b) Using for loop  
def longest_unique_substring_manual(s):
    seen, start, max_len = {}, 0, 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len


# 10. Return all permutations of a given string  
# (a) Using built-in function  
from itertools import permutations
def get_permutations_builtin(s):
    return ["".join(p) for p in permutations(s)]

# (b) Using for loop (Backtracking)  
def get_permutations_manual(s):
    def backtrack(path, options):
        if not options:
            res.append("".join(path))
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i+1:])
    res = []
    backtrack([], list(s))
    return res
