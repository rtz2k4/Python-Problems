def maxProduct(array, n):
    minVal = array[0]
    maxVal = array[0]

    maxProduct = array[0]

    for i in range(1, n):
        if (array[i]<0):
            temp = maxVal
            maxVal = minVal
            minVal = temp

        maxVal = max(array[i], maxVal*array[i])
        minVal = min(array[i], minVal*array[i])

        maxProduct = max(maxProduct, maxVal)

    return maxProduct

if __name__ == '__main__':
    myArray = [-1, -3, -10, 0, 60]
    n = len(myArray)

    print("Maximum subarray product is", maxProduct(myArray, n))