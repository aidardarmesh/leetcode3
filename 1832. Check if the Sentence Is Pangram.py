def checkIfPangram(sentence):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    s = set(sentence)

    for i in range(len(alphabet)):
        if not alphabet[i] in s:
            return False
    
    return True

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))

sentence = "leetcode"
print(checkIfPangram(sentence))
