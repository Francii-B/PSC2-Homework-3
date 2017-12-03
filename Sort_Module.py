def mergeSort(left, right):
    newList = []

    if len(left) == 1 and len(right) == 1:
        if (left[0] < right[0]):
            newList = left + right
        else:
            newList = right + left

    else:
        while len(left) >= 1 and len(right) >= 1:
            if left[0] <= right[0]:
                newList.append(left.pop(0))
            else:
                newList.append(right.pop(0))


    return newList+ left+ right


def merge(list):
    if len(list) == 1:
        return list

    # split in 2
    left = list[0:len(list)//2]
    right = list[len(list)//2:]

    leftSorted = merge(left)
    rightSorted = merge(right)

    return mergeSort(leftSorted, rightSorted)


def QuickSort(list):

    if len(list) > 1:
        pivot=list[0]
        left, right=[], []
        for i in range(1, len(list)):
            if (list[i] < pivot):
                left.append(list[i])
            else:
                right.append(list[i])
        return QuickSort(left) + [pivot] + QuickSort(right)

    else:
        return list

