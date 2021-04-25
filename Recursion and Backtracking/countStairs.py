"""
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time.
Count the number of ways, the person can reach the top
"""
def possibleStair(n):
    if n <= 1:
        return 1
    return possibleStair(n-1) + possibleStair(n-2)



print(possibleStair(2))