import random

arr = random.sample(range(1, 100), 10)

print("Original list:", arr)

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted list:", arr)