# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_index = 0
    b_index = 0

    for item in range(len(merged_arr)):
        if a_index > len(arrA) - 1:
            merged_arr[item] = arrB[b_index]
            b_index += 1

        elif b_index > len(arrB) - 1:
            merged_arr[item] = arrA[a_index]
            a_index += 1

        else:
            if arrA[a_index] > arrB[b_index]:
                merged_arr[item] = arrB[b_index]
                b_index += 1
            else:
                merged_arr[item] = arrA[a_index]
                a_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
