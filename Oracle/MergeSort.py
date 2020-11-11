def mergeSort(nums):

    def partition(l, r):
        if l >= r:
            return [nums[l]]

        mid = l + (r-l) // 2
        left = partition(l, mid)
        right = partition(mid+1, r)

        tmp = []

        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1

        if i < len(left):
            tmp += left[i:]

        if j < len(right):
            tmp += right[j:]

        return tmp
    return partition(0, len(nums)-1)
