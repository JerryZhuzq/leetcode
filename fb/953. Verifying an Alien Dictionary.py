class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}

        for i in range(len(order)):
            order_dict[order[i]] = i

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            for j in range(len(word_1)):
                if j >= len(word_2):
                    if order_dict[word_1[j - 1]] == order_dict[word_2[j - 1]]:
                        return False
                    else:
                        break
                if order_dict[word_1[j]] == order_dict[word_2[j]]:
                    continue
                elif order_dict[word_1[j]] > order_dict[word_2[j]]:
                    return False
                else:
                    break

        return True
