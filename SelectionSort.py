print('nums = [59,92,93,71,88,26,14,8,81,11]')
print("")

def sort (nums):

    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [59,92,93,71,88,26,14,8,81,11]
sort(nums)

print(nums)