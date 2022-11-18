
def binary_gap(z):
    """Function to find the longest binary gap for a given int"""
    first = bin(z)
    sec = list(first)
    thi = sec[2:]
    a = [i for i, n in enumerate(thi) if n == '1']
    a = list(reversed(a))
    b = []
    if len(a) > 1:
        for x, num in enumerate(a):
            if x <= len(a) - 2:
                b.append(a[x] - a[x+1] - 1)
        return max(b)
    else:
        return 0


def cyclic_rotation(a, k):
    """Rotate an array A a given number of times as specified by K"""
    if len(a) > 0:
        for i in range(k):
            a.insert(0, a[(len(a) - 1)])
            a.pop()
        return a
    else:
        return a


def odd_instance(a):
    """Find unpaired element in an array"""
    if len(a) == 1:
        return a[0]
    a = sorted(a)
    for i in range(0, len(a), 2):
        if a[i+1] == len(a):
            return a[i]
        if a[i] != a[i]+1:
            return a[i]


def frog_jump(x, y, d):
    """Calculate the minimum number of steps to get from x to y travelling by intervals of distance d"""
    a = y - x
    if x == y:
        return 0
    ans = a // d
    if a / d != a // d:
        return int(ans) + 1
    return ans


def permutation(a):
    """Check if array a is a permutation"""
    if max(a) > 100000:
        return 0
    count = [0] * (max(a) + 1)
    count[0] = 1
    for i in a:
        count[i] += 1
    if max(count) > 1:
        return 0
    if min(count) < 1:
        return 0
    return 1


def missing_int(a):
    """Finds the smallest possible positive integer missing from array"""
    a.sort()
    c = [False] * max(a)
    c.append(True)
    if max(a) <= 0:
        return 1
    for e in a:
        if e > 0:
            c[e - 1] = True
            if c[e - 2] == False:
                return c.index(False) + 1
    return max(a) + 1


def passing_cars(a):
    """Returns the number of pairs of passing cars iven a non-empty array a, where 0 represents a car travelling
    east and 1 represents a car travelling west"""
    z = 0
    ans = 0
    ind = 0
    if max(a) == min(a):
        return 0
    while ans <= 1000000001 and ind <= (len(a) - 1):
        if a[ind] == 0:
            z += 1
        if a[ind] == 1:
            ans += (1 * z)
        ind += 1
    if ans >= 1000000001:
        return -1
    return ans


def solution(A, B, K):
    # write your code in Python 3.8.10
    count = A
    ans = 0
    while count <= B:
        if count % K != 0:
            count += 1
        if count % K == 0:
            if A % 2 != 0 and B % 2 != 0:
                ans += (B - A) // K
            else:
                ans += (1 + (B - A)//K)
            break
    return ans


def distinct_array(a):
    """Returns the number of distinct integers in an array"""
    a.sort()
    if len(a) == 0:
        return 0
    ans = 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            ans += 1
    return ans


def triangle(A):
    """An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

    A[P] + A[Q] > A[R],
    A[Q] + A[R] > A[P],
    A[R] + A[P] > A[Q].

    Returns 1 if triangular, 0 if not"""

    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A) - 2):
        if (A[i] + A[i + 1]) > A[i + 2] and (A[i] + A[i + 2]) > A[i + 1] and (A[i + 2] + A[i + 1]) > A[i]:
            return 1
    return 0


