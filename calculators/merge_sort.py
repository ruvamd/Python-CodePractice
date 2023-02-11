def merge(A, B):
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result.extend(A[i:])
    result.extend(B[j:])
    return result

print(merge([5,10,15,20], [3,7,13,60]))