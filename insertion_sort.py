import random

arr = random.sample(range(1, 100), 10)

print("Original list: ----", arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted list: ----", arr)