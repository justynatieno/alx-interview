#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0

    # Initializing the result with the maximum value
    result = n

    # Starting from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        count = 0
        temp = n

        # dividing n by i as long as it's divisible
        while temp % i == 0:
            count += 1
            temp = temp // i

        # If n was divided completely by i,
        if temp == 1:
            result = min(result, count + minOperations(i))

    # If n is a prime number, return 1
    if result == n:
        return 1

    return result
