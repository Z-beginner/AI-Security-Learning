from typing import List
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        added_list = []
        word_list = []
        num = 0
        for word in words:
            for i in word:
                num += weights[ord(i) - ord('a')]
            added_list.append(num)
            num = 0
        for added in added_list:
            number = added % 26
            word_list.append(chr(ord('z') - number))
        return ''.join(word_list)
words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
sol = Solution()
result = sol.mapWordWeights(words,weights)
print(f'"{result}"')