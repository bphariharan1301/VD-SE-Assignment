def findDuplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index] < 0:
            duplicates.append(index)
        else:
            nums[index] = -nums[index]

    return duplicates


# main program
nums = [1, 3, 4, 2, 2]
print(findDuplicates(nums))  # Output: [2]
