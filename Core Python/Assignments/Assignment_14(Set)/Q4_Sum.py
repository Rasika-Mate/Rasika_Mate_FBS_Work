# 4. WAP that finds all pairs of elements in a list whose sum is equal to a given value.

nums = [2, 4, 3, 5, 7, 8, 9]
target = 10

print("List:", nums)
print("Target:", target)
print("Pairs:")

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], "+", nums[j], "=", target)