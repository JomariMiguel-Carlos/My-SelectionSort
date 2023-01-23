print('nums = [59,92,93,71,88,26,14,8,81,11]')
print("")

def sort(nums):
    for i in range(1,len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j-=1

        print(nums)


nums = [59,92,93,71,88,26,14,8,81,11]
sort(nums)

print(nums)
