def count_pairs_with_sum(array, target_sum):
    count = 0
    for k in range(len(array)):
        for l in range(k+1, len(array)):
            if array[k] + array[l] == target_sum:
                count += 1
    return count
 
array = [2, 7, 4, 1, 3, 6]
target_sum = 10
result = count_pairs_with_sum(array, target_sum)
print(f"Number of pairs with sum {target_sum}: {result}")
