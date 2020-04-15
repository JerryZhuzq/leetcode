'''Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

'''



# My solution

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        left, right = [], []
        count = 0
        for i in reversed(S):
            if i == "#":
                count += 1
                continue
            elif count > 0:
                count -= 1
                continue
            else:
                left.append(i)
        count = 0
        for i in reversed(T):
            if i == "#":
                count += 1
                continue
            elif count > 0:
                count -= 1
                continue
            else:
                right.append(i)
        return (left == right)

# O(N)  O(1) space solution

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))