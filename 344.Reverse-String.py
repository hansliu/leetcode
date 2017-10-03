def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    def reverse(s, start, end):
        r = list(s)
        while start < end:
            r[start], r[end] = r[end], r[start]
            start += 1
            end -= 1
        return "".join(r)
    return reverse(s, 0, len(s)-1)

print reverseString("hello")
