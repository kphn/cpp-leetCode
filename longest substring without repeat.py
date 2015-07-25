class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        length = 0
        first = 0;last = 0
        chars = set()
        while(last < len(s)):
        	if(s[last] not in chars):
        		chars.add(s[last])
        		last += 1
        	else:
        		if((last - first) > length):
        			length = (last - first)
        		while(s[first] != s[last]):
        			chars.remove(s[first])
        			first += 1
        		first += 1
        return length


