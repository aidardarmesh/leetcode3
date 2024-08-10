def minMutation(startGene, endGene, bank):
    def mutate(gene):
        ans = []
        for i in range(len(gene)):
            for choice in ['A', 'C', 'G', 'T']:
                if gene[i] != choice:
                    ans.append(gene[:i] + choice + gene[i+1:])   
        return ans

    bank = set(bank)
    seen = set()
    from collections import deque
    queue = deque([(startGene, 0)])

    while queue:
        gene, mutations = queue.popleft()

        if gene == endGene:
            return mutations
        
        for mutatedGene in mutate(gene):
            if mutatedGene in bank and not mutatedGene in seen:
                seen.add(mutatedGene)
                queue.append((mutatedGene, mutations + 1))
    
    return -1

print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(minMutation("AACCGGTT", "AACCGGTA", []))
print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTG"]))