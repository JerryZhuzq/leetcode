"""
arr:需要排序的列表
n：列表长度
i：开始节点
"""
def heapify(arr: list, n: int, i: int) -> list:
    # 递归条件
    if i >= n:
        return
    # 默认父节点最大index
    largest = i
    lchild = 2 * i + 1
    rchild = 2 * i + 2

    if lchild < n and arr[i] < arr[lchild]:
        largest = lchild
    # 如果右节点小于整个节点长度，并且右节点大于父节点
    # 那么index交换
    if rchild < n and arr[i] < arr[rchild]:
        largest = rchild
    # 如果父节点已经为最大值了，那么就不用交换，否则进行交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 进行递归，递归条件就是i >= n:
        # 因为节点是不可能大于整个列表的最大长度的
        heapify(arr, n, largest)


arr = [4,10,3,5,1,20]
# print('----heapify前-----')
# print(arr)
n = len(arr)
# # 此处我设置为root节点的index:0开始
# heapify(arr, n ,0)
# print('----heapify后-----')
# print(arr)

# result
# ----heapify前-----
# [4, 10, 3, 5, 1, 2]
# ----heapify后-----
# [10, 5, 3, 4, 1, 2]


def heapify(arr, n, i):
    if i >= n:
        return
    left = 2*i+1
    right = left + 1
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
heap_sort(arr)
print(arr)