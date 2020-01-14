# Given a string consisting of only A’s and B’s. We can transform the given string to another string by toggling any character. Thus many transformations of the given string are possible. The task is to find Weight of the maximum weight transformation.
# Weight of a sting is calculated using below formula.
#
#
# Weight of string = Weight of total pairs +
#                    weight of single characters -
#                    Total number of toggles.
#
# Two consecutive characters are considered as pair only if they
# are different.
# Weight of a single pair (both character are different) = 4
# Weight of a single character = 1

# Input: str = "AA"
# Output: 3
# Transformations of given string are "AA", "AB", "BA" and "BB".
# Maximum weight transformation is "AB" or "BA".  And weight
# is "One Pair - One Toggle" = 4-1 = 3.
#
# Input: str = "ABB"
# Output: 5
# Transformations are "ABB", "ABA", "AAB", "AAA", "BBB",
# "BBA", "BAB" and "BAA"
# Maximum weight is of original string 4+1 (One Pair + 1
# character)

def maxWeightTransf(s):
    n = len(s)
    if n == 1 or n == 0:
        return n
    res = [0 for x in range(n)]
    res[0] = 1
    if s[0] == s[1]:
        res[1] = 3
    else:
        res[1] = 4

    for i in range(2,n):
        if s[i] == s[i-1]:
            res[i] = max(res[i-2] + 3, res[i-1] + 1)
        else:
            res[i] = max(res[i-2] + 4, res[i-1] + 1)

    return res[n-1]


# Python3 program to find maximum weight
# transformation of a given string

# Returns weight of the maximum
# weight transformation
def getMaxRec(string, i, n, lookup):
    # Base Case
    if i >= n:
        return 0

    # If this subproblem is already solved
    if lookup[i] != -1:
        return lookup[i]

        # Don't make pair, so
    # weight gained is 1
    ans = 1 + getMaxRec(string, i + 1, n,
                        lookup)

    # If we can make pair
    if i + 1 < n:

        # If elements are dissimilar
        if string[i] != string[i + 1]:
            ans = max(4 + getMaxRec(string, i + 2,
                                    n, lookup), ans)
            # if elements are similar so for
        # making a pair we toggle any of them.
        # Since toggle cost is 1 so
        # overall weight gain becomes 3
        else:
            ans = max(3 + getMaxRec(string, i + 2,
                                    n, lookup), ans)
            # save and return maximum
    # of above cases
    lookup[i] = ans
    return ans


# Initializes lookup table
# and calls getMaxRec()
def getMaxWeight(string):
    n = len(string)

    # Create and initialize lookup table
    lookup = [-1] * (n)

    # Call recursive function
    return getMaxRec(string, 0,
                     len(string), lookup)

print(maxWeightTransf("AAAB"))

