def auto_layout(number):
    """
    Does some magic layout.

    >>> auto_layout(2)
    [2]
    >>> auto_layout(3)
    [3]
    >>> auto_layout(4)
    [2, 2]
    >>> auto_layout(5)
    [2, 3]
    >>> auto_layout(6)
    [2, 4]
    >>> auto_layout(7)
    [3, 4]
    >>> auto_layout(8)
    [2, 2, 4]
    >>> auto_layout(9)
    [2, 3, 4]
    >>> auto_layout(10)
    [2, 4, 4]
    >>> auto_layout(11)
    [3, 4, 4]
    >>> auto_layout(24)
    [2, 2, 4, 4, 4, 4, 4]
    """
    if number == 1:
        raise ValueError
    slices = [4] * (number / 8)
    if (number - sum(slices)) % 2 == 1:
        slices.append(3)
        while number - sum(slices) >= 4:
            slices.append(4)
    else:
        while number - sum(slices) > 4:
            slices.append(4)
    while number > sum(slices):
        slices.append(2)
    return sorted(slices)


def slice_layouts(items):
    """
    >>> slice_layouts([1, 2])
    [[1, 2]]
    >>> slice_layouts([1, 2, 3])
    [[1, 2, 3]]
    >>> slice_layouts([1, 2, 3, 4])
    [[1, 2], [3, 4]]
    >>> slice_layouts([1, 2, 3, 4, 5])
    [[1, 2], [3, 4, 5]]
    >>> slice_layouts([1, 2, 3, 4, 5, 6])
    [[1, 2], [3, 4, 5, 6]]
    >>> slice_layouts([1, 2, 3, 4, 5, 6, 7])
    [[1, 2, 3], [4, 5, 6, 7]]
    >>> slice_layouts([1, 2, 3, 4, 5, 6, 7, 8])
    [[1, 2], [3, 4], [5, 6, 7, 8]]
    """
    r = list()
    index = 0
    for n in auto_layout(len(items)):
        r.append(items[index:index + n])
        index += n
    return r


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()