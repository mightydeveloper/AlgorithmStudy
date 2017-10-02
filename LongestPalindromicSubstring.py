def longestPalindrome(s):
    t = "#"+"#".join(s)+"#"
    maxBorder = 0
    maxCenter = 0
    p = [0 for _ in range(len(t))]
    best = (0,0)

    for i in range(len(t)):
	if maxBorder > i:
	    i_mirror = 2*maxCenter - i
	    p[i] = min(p[i_mirror], maxBorder-i)
	else:
	    p[i] = 1

	# Expand palindrome
	while i-p[i]>=0 and i+p[i]<len(t) and t[i-p[i]] == t[i+p[i]]:
	    p[i] += 1

	if maxBorder < i + p[i]:
	    maxBorder = i + p[i]
	    maxCenter = i
	    if maxBorder - maxCenter > best[1] - best[0]:
		best = maxCenter, maxBorder
    left = 2*best[0] - best[1] + 1
    right = best[1]
    return "".join([x for x in t[left:right] if x!='#'])




