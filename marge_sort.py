def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        # merge
        i = j = k = 0
        
        for _ in range(len(left_arr) + len(right_arr)):
            if i < len(left_arr) and (j >= len(right_arr) or left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

arr_test = [2, 3, 5, 1, 7, 4, 4, 2, 6, 0]
merge_sort(arr_test)

print(arr_test)
