# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

nums = [10, 25, 5, 65, 30, 90, 75]

# Bubble Sort Algorithm
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

# After sorting, the second largest is the second last element
second_largest = nums[-2]
print("Sorted List:", nums)
print("Second Largest Number:", second_largest)