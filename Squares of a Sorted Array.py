def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # use two point
    start = 0
    end = len(nums)-1
    while start < end:
        if(abs(nums[start]) > abs(nums[end])): # >=로 포함하면 불필요한 과정을 한번 더 하게 되므로 =은 생략.
            temp = abs(nums[start])
            nums.remove(nums[start])
            nums.insert(end,temp)
        else:
            end-=1
    for i in range(len(nums)):
        sq = nums[i] * nums[i]
        nums[i] = sq
    return nums
