def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    neg_limit = -0x80000000
    pos_limit = 0x7fffffff
    if x > 0:
        ans = int(str(x)[::-1])
        if ans > pos_limit:
            return 0
        else:
            return ans
    elif x < 0:
        ans = 0-int(str(0-x)[::-1])
        if ans < neg_limit:
            return 0
        else:
            return ans
    else:
        return 0

print reverse(123)
print reverse(-123)
