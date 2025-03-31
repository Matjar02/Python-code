import unittest

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # Rekurencja
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        # Scalanie
        i = j = k = 0
        
        for _ in range(len(left_arr) + len(right_arr)):
            if i < len(left_arr) and (j >= len(right_arr) or left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

def filter_numbers(arr, min_value, max_value):
    return [x for x in arr if min_value <= x <= max_value]

class TestSortingAndFiltering(unittest.TestCase):
    def test_merge_sort(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        sorted_data = sorted(data)
        merge_sort(data)
        self.assertEqual(data, sorted_data)
    
    def test_filter_numbers(self):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        filtered_data = filter_numbers(data, 3, 7)
        self.assertEqual(filtered_data, [3, 4, 5, 6, 7])

if __name__ == "__main__":
    unittest.main()
