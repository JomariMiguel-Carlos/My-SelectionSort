print('nums = [59,92,93,71,88,26,14,8,81,11]')
print("")

def quick_sort(nums):
    length = len(nums)
    if length <=1:
        return nums
    else:
        pivot = nums.pop()

    items_greater = []
    items_lower = []

    for item in nums:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)



print(quick_sort([59,92,93,71,88,26,14,8,81,11]))