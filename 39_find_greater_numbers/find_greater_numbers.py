def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    count = 0
    next_num = 1
    current_num = 0

    for x in range(len(nums)):
        if(next_num < len(nums)-1):
            if nums[current_num] < nums[next_num]:
                count = count + 1
                next_num = next_num + 1
            else:
                current_num  = current_num + 1
                next_num = next_num + 1

    return count
    