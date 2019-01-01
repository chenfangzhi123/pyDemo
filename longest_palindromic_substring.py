class Solution(object):
    def longest_palindrome(self, str_):
        if len(str_) < 2:
            return str_
        max_len = 0
        res = ''
        for i in range(len(str_) - 1):
            str1 = self.extend_palindrome(str_, i, i)
            str2 = self.extend_palindrome(str_, i, i + 1)
            if len(str1) > max_len:
                res = str1
                max_len = len(str1)
            if len(str2) > max_len:
                res = str2
                max_len = len(str2)
        return res

    @staticmethod
    def extend_palindrome(s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j = j - 1
            k = k + 1
        return s[j + 1:k]


s = Solution()
print(s.longest_palindrome('abccbaaeb'))
