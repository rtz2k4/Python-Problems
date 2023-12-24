def find_pair(arr, n, diff): 
    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            if arr[j] - arr[i] == diff:
                print(f"Pair found: {arr[i]} and {arr[j]}")
                return
    print("No such pair!")


# Time complexity O(n*n)
    

# Another method is by using binary search 
# Thus we get time complexity O(n*logn)
# The functions assumes that the array is sorted
    
def findPair(arr, n):
    size = len(arr)
    i, j = 0, 1

    while i<size and j<size:
        if i != j and arr[j] - arr[i] == n:
            print("Pair found: {arr[i]} and {arr[j]}")

        elif arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1
    print("No pair found")
    return False
