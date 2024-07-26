""" Homework 3: Recursion and Tree Recursion"""

HW_SOURCE_FILE = 'hw03.py'

#####################
# Required Problems #
#####################

def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'number_of_six',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return int(n == 6)

    return int((n % 10) == 6) + number_of_six(n//10)

def rev_times(n):
    '''helper function for pingpong, return the num of numbers change direction'''
    if n == 1:
        return 0

    return rev_times(n - 1) + (1 if (number_of_six(n) > 0 or n % 6 == 0) else 0)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    5
    >>> pingpong(8)
    4
    >>> pingpong(15)
    3
    >>> pingpong(21)
    5
    >>> pingpong(22)
    6
    >>> pingpong(30)
    10
    >>> pingpong(68)
    0
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    -1
    >>> pingpong(72)
    -2
    >>> pingpong(100)
    6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    # # iterative version
    # ans = 1
    # incr = True
    # for i in range(2, n + 1):
    #     ans += 1 if incr else -1
    #
    #     if i % 6 == 0 or number_of_six(i) > 0:
    #         incr = not incr
    #
    # return ans

    # recursion version: backward recursion with the global helper function `rev_times`
    if n == 1:
        return 1

    return (-1 if rev_times(n - 1) & 1 else 1) + pingpong(n - 1)

    # # recursion version: forward recursion with the local helper function
    # # referred from https://github.com/jjl9807/fall-2021-nju-sicp/blob/main/Homework/hw03-Solution.py
    # # however, this referred solution is not that elegant.
    # def solve(k, result, direct):
    #     if k == n:
    #         return result
    #
    #     if k % 6 == 0 or number_of_six(k) > 0:
    #         return solve(k + 1, result - direct, -direct)
    #     else:
    #         return solve(k + 1, result + direct, direct)
    #
    # return solve(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0

    last_digit = n % 10
    last_but_one_digit = n // 10 % 10

    return ((last_digit - last_but_one_digit - 1) if last_digit - last_but_one_digit > 1 else 0) + missing_digits(n // 10)


def count_change(total, next_money):
    """Return the number of ways to make change for total,
    under the currency system described by next_money.

    >>> def chinese_yuan(money):
    ...     if money == 1:
    ...         return 5
    ...     if money == 5:
    ...         return 10
    ...     if money == 10:
    ...         return 20
    ...     if money == 20:
    ...         return 50
    ...     if money == 50:
    ...         return 100
    >>> def us_cent(money):
    ...     if money == 1:
    ...         return 5
    ...     elif money == 5:
    ...         return 10
    ...     elif money == 10:
    ...         return 25
    >>> count_change(15, chinese_yuan)
    6
    >>> count_change(49, chinese_yuan)
    44
    >>> count_change(49, us_cent)
    39
    >>> count_change(49, lambda x: x * 2)
    692
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def solve(remain, min):
        if remain == 0:  # as recursion depth grows ↑, the `min` grows ↑
            return 1
        if remain < 0:
            return 0
        if min == None or min > remain: # as recursion depth grows ↑, the `min` grows ↑
            return 0

        return solve(remain - min, min) + solve(remain, next_money(min))

    return solve(total, 1)

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def get_mid(start, end):
    '''helper function for move_stack'''
    for i in range(1, 4):
        if start != i and end != i:
            return i


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
        return

    move_stack(n - 1, start, get_mid(start, end))
    print_move(start, end)
    move_stack(n - 1, get_mid(start, end), end)



def multiadder(n):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    >>> from construct_check import check
    >>> # Make sure multiadder is a pure function.
    >>> check(HW_SOURCE_FILE, 'multiadder',
    ...       ['Nonlocal', 'Global'])
    True
    """
    "*** YOUR CODE HERE ***"
    def make_order_func(order, sum):
        def func(x):
            if order == 1:
                return sum + x
            else:
                return make_order_func(order - 1, sum + x)

        return func

    # Note that as recursion depth grows ↑, the order `n` growss ↓ until 1,
    # and the sum of args sequence `sum` grows ↑ from 0
    return make_order_func(n, 0)

##########################
# Just for fun Questions #
##########################


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return Y(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))
    # return lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n - 1)))



Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
fib_maker = lambda f: lambda r: 0 if r == 0 else (1 if r == 1 else (f(r - 1) + f(r -2)))
number_of_six_maker = lambda f: lambda r: int(r == 6) if r < 10 else (int((r % 10) == 6) + number_of_six(r//10))

my_fib = Y(fib_maker)
my_number_of_six = Y(number_of_six_maker)

# This code sets up doctests for my_fib and my_number_of_six.

my_fib.__name__ = 'my_fib'
my_fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

>>> my_fib(0)
0
>>> my_fib(1)
1
>>> my_fib(2)
1
>>> my_fib(3)
2
>>> my_fib(4)
3
>>> my_fib(5)
5
"""

my_number_of_six.__name__ = 'my_number_of_six'
my_number_of_six.__doc__="""Return the number of 6 in each digit of a positive integer n.

>>> my_number_of_six(666)
3
>>> my_number_of_six(123456)
1
"""
