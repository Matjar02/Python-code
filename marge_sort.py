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

# reading data from a file
with open("input.txt", "r") as file:
    arr = list(map(int, file.readline().split()))

#  range
min_value = int(input("min value: "))
max_value = int(input("max value: "))

# data filtering
filtered_arr = [x for x in arr if min_value <= x <= max_value]

# sorting
merge_sort(filtered_arr)

# saving to file
with open("output.txt", "w") as file:
    file.write(" ".join(map(str, filtered_arr)))

print("The sorted data was saved in the file output.txt")
