def FindKthLargest(input,K):
    # Sort the input array in descending order
    input = sorted(input, reverse=True)

    # Return the Kth element
    return input[K-1]

input = [1, 5, 9, 2, 25, 16, 19, 22, 4, 7, 55]
K = 4
result = FindKthLargest(input,K)
print(result) # Output: 16
