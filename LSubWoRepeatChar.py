def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {} # char : idx mapping
    maximum = 0
    leftmost = 0
    for i, c in enumerate(s):
	if c in chars and leftmost < chars[c] + 1:
	    leftmost = chars[c] + 1
	chars[c] = i
	length = i - leftmost + 1
	maximum = max(maximum, length)
    return maximum


# optimized ver
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {} # char : idx mapping
    maximum = 0
    leftmost = -1
    for i, c in enumerate(s):
	if c in chars and leftmost <= chars[c]:
	    leftmost = chars[c]
	chars[c] = i
	maximum = max(maximum, i - leftmost)
    return maximum
