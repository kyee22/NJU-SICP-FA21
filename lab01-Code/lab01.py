def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1 # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    # pass  # YOUR CODE HERE

    # recursive version
    # if n == 1:
    #     return 1
    # else:
    #     return factorial(n - 1) * n

    # iter version
    k, ans = 1, 1
    while k <= n:
        ans *= k
        k += 1

    return ans


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    # pass  # YOUR CODE HERE

    return (a + b > c) and (a + c > b) and (b + c > a)

def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    # pass  # YOUR CODE HERE
    tot = 0
    while n > 0:
        tot += int(n % 10 == 6)
        n //= 10

    return tot

def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    # pass  # YOUR CODE HERE
    ans = x % 10
    while x > 0:
        ans = max(ans, x % 10)
        x //= 10
    return ans