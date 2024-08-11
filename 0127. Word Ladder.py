def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)

    def ladderWords(word):
        ans = []
        alphabet = [chr(ord('a') + i) for i in range(26)]

        for i in range(len(word)):
            for ch in alphabet:
                newWord = word[:i] + ch + word[i+1:]

                if newWord in wordList:
                    ans.append(newWord)

        return ans
    
    from collections import deque
    queue = deque([(beginWord, 1)])
    seen = set([beginWord])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for newWord in ladderWords(word):
            if not newWord in seen:
                queue.append((newWord, steps + 1))
                seen.add(newWord)
    
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord, endWord, wordList))

