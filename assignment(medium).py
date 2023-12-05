def majority_elements(nums):
    if not nums:
        return []

    # Initialize candidates and their counters
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # Count occurrences of candidates and update counts
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Reset counters to count actual occurrences
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates meet the requirement
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# Example usage:
nums = [3, 3, 3, 5, 5, 5, 6, 6, 6]
result = majority_elements(nums)
print(result)
