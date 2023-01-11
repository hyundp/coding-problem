def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    end = len(nums)-1
    start = 0

    # 만약 순서 유지가 필요없이 0을 뒤로 보내는것만 필요하다면 swap이용 가능
    while(start < end):
        if nums[start] == 0:
            nums.remove(0)
            nums.insert(end, 0)
            end-=1
        else:
            start += 1