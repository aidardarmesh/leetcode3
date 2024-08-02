def checkIfPangram(sentence):
    return len(set(sentence)) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))

sentence = "leetcode"
print(checkIfPangram(sentence))
