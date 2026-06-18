arr = [5, 15, 25, 35, 45]
x = int(input("Enter number: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Found at position", mid)
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")