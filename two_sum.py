

def twosum(nums,target,result):
    l_nums = len(nums)
    if l_nums < 2:
        return
    twosum(nums[1:],target,result)
    for i in nums[1:]:
        if nums[0] + i == target:
            result.append([nums[0],i])
    return result

def twosum1(nums,target):
    l = len(nums)
    result = []
    for i in range(0,l-1):
        for j in nums[i+1:]:
            if nums[i] + j == target:
                result.append([nums[i],j])
    return result


nums = [-6,7,11,-2,15]
print(twosum(nums,9,[]))
