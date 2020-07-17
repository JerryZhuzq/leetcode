class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        middle = len(palindrome) // 2
        for i in range(middle):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        if len(palindrome) > 1:
            return palindrome[:len(palindrome) - 1] + 'b'
        return ''


# Not hard, just remember the corner case: aaaaaaa
