def LMIS(A, n):
    longest = 1

    if n == 1:
        return longest

    # Recursively go down to size of 1 then slowly come back up to the end of the array
    for i in range(n - 1, 0, -1):
        previousLMIS = LMIS(A, i)
        if A[i - 1] < A[n - 1] and previousLMIS >= longest:
            longest = previousLMIS + 1

    return longest


a = [1, 2, 3, 4]

subser = LMIS(a, len(a))

print(subser)
