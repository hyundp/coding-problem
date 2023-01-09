def bs1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # find exact value
    start = 0
    end = len(nums)-1
    while(start <= end):
        mid = (start+end)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return -1

def bs2(nums, target):
    # find upper bound -> target에 해당하는 값이 nums에 여러개 있을 때
    start = 0
    end = len(nums) # upper bound는 찾는 값보다 크다
    while(start<end): # end가 mid를 그대로 받기 때문에 같은 경우는 포함하지 않는다.
        mid = (start+end)//2
        if(nums[mid]<=target):
            start = mid+1
        else:
            end = mid

    if(start>0 and nums[start-1]==target):
        return start-1
    else:
        return -1
    
def bs3(nums, target):
    # find lower bound -> target에 해당하는 값이 nums에 여러개 있을 때
    start = 0
    end = len(nums)-1 # lower bound는 찾는 값과 같다.
    while(start<end): # end가 mid를 그대로 받기 때문에 같은 경우는 포함하지 않는다.
        mid = (start+end)//2
        if(nums[mid]>=target):
            end = mid
        else:
            start = mid + 1

    if start < len(nums) and nums[start]==target:
        return start
    else:
        return -1