class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        res = ""
        if len(words)==0:
            return ""
        for i in range(len(words)-1):
            res+=(words[len(words)-i-1])
            res+=" "
        res += words[0]
        return res
