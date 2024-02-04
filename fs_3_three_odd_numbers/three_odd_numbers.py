def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    pointer1 = 0
    pointer2 = 1
    pointer3 = 2
    sum = 0
    for x in range(len(nums)):
        if pointer3 < len(nums)-1:
            sum = nums[pointer1] + nums[pointer2] + nums[pointer3]
            if sum % 2 != 0:
                return True
            else:
                pointer1 += 1
                pointer2 += 1
                pointer3 += 1

    return False
