def word_pattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False
    
    letter_word = {}
    word_letter = {}
    for i in range(len(pattern)):
        if not pattern[i] in letter_word:
            if words[i] in word_letter:
                return False
            letter_word[pattern[i]] = words[i]
            word_letter[words[i]] = pattern[i]
        elif letter_word[pattern[i]] != words[i]:
            return False
    
    return True


assert word_pattern("abba", "dog cat cat dog") == True
assert word_pattern("abba", "dog cat cat fish") == False
assert word_pattern("aaaa", "dog cat cat dog") == True
assert word_pattern("abba", "dog dog dog dog") == True
