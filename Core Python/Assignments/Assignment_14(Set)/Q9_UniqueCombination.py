# 9. WAP to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

nums = [1, 2, 3, 4, 5, 6, 7]
target = 12

print("Numbers:", nums)
print("Target:", target)
print("Triplets:")

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                print(nums[i], nums[j], nums[k])