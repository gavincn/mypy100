def rotate(nums,k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums[:] = nums[len(nums) - k: len(nums) + 1] + nums[0:k + 1]
    print(nums)


list = [1, 2, 3, 4, 5, 6, 7]
rotate(list, 3)
