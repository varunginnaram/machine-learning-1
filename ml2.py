def calculate_range(array):
    if len(array) < 3:
        return "Range determination not possible"
    else:
        return max(array) - min(array)
 
array = [5, 3, 8, 1, 0, 4]
result = calculate_range(array)
print(f"The range is: {result}")
