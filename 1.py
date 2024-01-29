import heapq
#№1
def elements(lst):
    if not lst:  # проверка на пустой список
        raise ValueError("Empty list")
    result = 1
    for num in lst:
        if not isinstance(num, int):  # проверка на целое число
            raise TypeError("Non-integer value in the list")
        result *= num
    return result
print(elements([1, 2, 3, 4]))  # 24
print(elements([-1, 0, 1]))  # 0
print(elements([1, 2, 3, 4, 5]))  # 120
# №2
def min_elements(lst):
    if not lst:  # проверка на пустой список
        raise ValueError("Empty list")
    min_value = lst[0]
    for num in lst:
        if not isinstance(num, int):  # проверка на целое число
            raise TypeError("Non-integer value in the list")
        if num < min_value:
            min_value = num
    return min_value
print(min_elements([1, 2, 3, 4]))  # 1
print(min_elements([-1, 0, 1]))  # -1

#+++++++++++++++++++++++++++++++++++
#№3
def num_1(*args):
    count = 0

    for num in args:
        if is_prime(num):
            count += 1
    return count

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d  # чередование прироста 2 и 4: 5 + 2, 7 + 4, 11 + 2, и т.д.
    return prime


print(num_1(-2, 2, 3, 5, 10))
#++++++++++++++++++++++++++++++++++++++++++++++++++++

def remove_num(nums, target):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == target:
            nums.pop(i)
            count += 1
        else:
            i += 1
    return count

# Example usage:
nums = [4, 5, 6, 7, 8, 9, 10]
target = 9
print(remove_num(nums, target))  # Output: 1
print(nums)  # Output: [4, 5, 6, 8, 9, 10]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def merge_lists(list1, list2):
    return list(heapq.merge(list1, list2))

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = merge_lists(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def power_list(nums, power):
   return [num ** power for num in nums]

# Example usage:
nums = [1, 2, 3, 4, 5]
power = 2
result = power_list(nums, power)
print(result)  # Output: [1, 4, 9, 16, 25]