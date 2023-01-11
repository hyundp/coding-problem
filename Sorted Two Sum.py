def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    end = len(numbers) - 1
    start = 0
    # 정렬된 문제는 two point 생각하면 좋다. 왜냐하면 지나간 것을 신경쓰지 않아도 되기 때문이다.
    while(start < end): 
        two_sum = numbers[start] + numbers[end]
        if (two_sum < target):
            start += 1
        elif (two_sum > target):
            end -= 1
        else:
            return [start+1, end+1]