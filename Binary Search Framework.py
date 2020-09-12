
# abstract framework
def binarySearch(nums, target):
    left, right = ..., ...
    while ...:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            ...
        elif nums[mid] < target:
            ...
        elif nums[mid] > target:
            ...

    return ...


# basic binary search, only search for a value or an index
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return nums[mid]  # return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# binary search for the left bound of an interval, [left, right]
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# binary search for the right bound of an interval. [left, right]
def binarySearch(nums, target):
    left, right = 0, len(nums-1)
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    if right < 0 or nums[right] != target:
        return -1
    return right








# search for the left bound of an interval, [left, right)
def binarySearch(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == nums[target]:
            right = mid
        elif nums[mid] > nums[target]:
            right = mid-1
        elif nums[mid] < nums[target]:
            left = mid+1
    if left == len(nums) or nums[left] != target:
        return -1
    return left


# search for the left bound of an interval, [left, right]
def binarySearch(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == nums[target]:
            right = mid - 1
        elif nums[mid] > nums[target]:
            right = mid - 1
        elif nums[mid] < nums[target]:
            left = mid + 1
    if left >= len(nums) or nums[right] != target:
        return -1
    return left


