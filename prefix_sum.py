

def prefix_sum_arr(arr):
    prefix_sum = [0]
    
    for num in arr:
        prefix_sum.append(prefix_sum + num)
    
    return prefix_sum


arr = [1, -20, -3, 30, 5, 4]
print(prefix_sum_arr(arr))



def prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    # Build the prefix sum array
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    return prefix_sum

# Example usage
arr = [2, 4, 6, 8, 10]
prefix = prefix_sum(arr)
print("Original array:", arr)
print("Prefix sum array:", prefix)

# To find sum from index 1 to 3 (i.e., arr[1] to arr[3])
l = 1
r = 3
subarray_sum = prefix[r] - (prefix[l-1] if l > 0 else 0)
print(f"Sum of elements from index {l} to {r}:", subarray_sum)