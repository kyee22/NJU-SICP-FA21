""" Homework 07: Special Method, Linked List and Tree"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, lst):
        self.coes = list(lst)
        i = len(self.coes) - 1
        while not self.coes[i] and i != 0:
            self.coes.pop(i)
            i -= 1

    def __repr__(self):
        return f'Polynomial({str(self.coes)})'

    def __str__(self):
        string = str(self.coes[0])

        for expo, coe in enumerate(self.coes[1:], 1):
            string += f' + {coe}*x^{expo}'

        return string

    def __add__(self, other):
        if len(self.coes) > len(other.coes):
            self, other = other, self

        new_coes = list(other.coes)
        for i in range(len(self.coes)):
            new_coes[i] += self.coes[i]

        return Polynomial(new_coes)

    def __mul__(self, other):
        l1, l2 = len(self.coes), len(other.coes)
        new_coes = [0 for _ in range(l1 + l2 - 1)]

        for expo1, coe1 in enumerate(self.coes):
            for expo2, coe2 in enumerate(other.coes):
                new_coes[expo1 + expo2] += coe1 * coe2

        return Polynomial(new_coes)



def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    "*** YOUR CODE HERE ***"

    while lnk is not Link.empty:
        while lnk.rest is not Link.empty and lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        lnk = lnk.rest


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    # recursion base case
    if link is Link.empty:
        return

    # deep-map `first`
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)

    # deep-map `rest` recursively
    deep_map_mut(fn, link.rest)


def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    "*** YOUR CODE HERE ***"
    def do_reverse(prev, lnk):
        if lnk.rest is Link.empty:
            lnk.rest = prev
            return lnk

        tail = do_reverse(lnk, lnk.rest)
        lnk.rest = prev
        return tail

    return do_reverse(Link.empty, lnk)


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self, other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        "*** YOUR CODE HERE ***"
        if self.label != other.label:
            return False

        b1, b2 = self.branches, other.branches
        l1, l2 = len(b1), len(b2)
        if l1 != l2:
            return False
        else:
            # # this is ok!
            # return all([b1[i] == b2[i] for i in range(l1)])
            # this is also ok!!
            return all((b1[i] == b2[i] for i in range(l1)))
            # # this is still ok!!!
            # return all(b1[i] == b2[i] for i in range(l1))



def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield [t.label]

    # although we dealt the 'base case'(seemingly like), we go on deeper search,
    # i.e., there is no 'return'-like statement

    for b in t.branches:
        for lst in generate_paths(b, value):
            yield [t.label] + lst



def funcs(link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> func_generator = funcs(Link.empty) # get root label
    >>> f1 = next(func_generator) 
    >>> f1(t)
    1
    >>> func_generator = funcs(Link(2)) # get label of third branch
    >>> f1 = next(func_generator)
    >>> f2 = next(func_generator)
    >>> f2(f1(t))
    4
    >>> # This just puts the 4 values from the iterable into f1, f2, f3, f4
    >>> f1, f2, f3, f4 = funcs(Link(0, Link(1, Link(0))))
    >>> f4(f3(f2(f1(t))))
    8
    >>> f4(f2(f1(t)))
    6
    """
    "*** YOUR CODE HERE ***"
    while True:

        if link is Link.empty:
            yield (lambda t: t.label)
            break
        else:
            '''1: Wrong!!'''
            # Python 的 lambda 表达式在创建时不会立即计算其中的变量，而是会在真正调用时再进行计算。这意味着
            # lambda 表达式中的 link.first 会在 lambda 表达式被调用时，使用 link 的当前值，而不是创建 lambda 表达式时的值。
            # yield lambda t: t.branches[link.first]

            '''2: Correct!!!!'''
            # 2 和 1 不一样的地方在于, 1 只是一个函数定义, 但 2 这里有一个函数调用。
            # 外部的 lambda 表达式会被立即调用, 其中 i 的值被绑定为 link.first 的当前值。
            # yield (lambda i: lambda t: t.branches[i])(link.first)

            '''3: Wrong!!'''
            # # 原因和 1 一样, 等到被调用时 tmp 的绑定已经发生了变化
            # tmp = link.first
            # yield lambda t: t.branches[tmp]

            '''4: Correct!!!'''
            # 下面这种方式的绑定不会丢失是因为默认参数在函数定义时就已经计算并绑定了当前的值，
            # 而不是在函数调用时才计算。这就避免了延迟绑定问题。
            tmp = link.first
            yield lambda t,tmp=tmp: t.branches[tmp]


            link = link.rest




def count_coins(change, denominations):
    """
    Given a positive integer change, and a list of integers denominations,
    a group of coins makes change for change if the sum of the values of 
    the coins is change and each coin is an element in denominations.
    count_coins returns the number of such groups. 
    """
    if change == 0:
        return 1
    if change < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(change, denominations[1:])
    with_current = count_coins(change - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(change, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since no ways to make change wuth no denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # The tree that shows the recursive calls that result
    >>> # in the 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    "*** YOUR CODE HERE ***"
    if change == 0:
        return Tree('1')
    if change < 0:
        return None
    if len(denominations) == 0:
        return None

    without_current = count_coins_tree(change, denominations[1:])
    with_current    = count_coins_tree(change - denominations[0], denominations)

    if (without_current is not None) and (with_current is not None):
        return Tree(str(change) + ', ' + str(denominations), [without_current, with_current])
    elif (without_current is None) and (with_current is not None):
        return Tree(str(change) + ', ' + str(denominations), [with_current])
    elif (without_current is not None) and (with_current is None):
        return Tree(str(change) + ', ' + str(denominations), [without_current])
    else:
        return None


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    "*** YOUR CODE HERE ***"
    def add_weight(t, delta):
        t.label += delta

    def do_balance(t):
        if t.is_leaf():
            return t.label

        weights = [do_balance(b)  for b in t.branches]
        max_weight = max(weights)
        for i,w in enumerate(weights):
            add_weight(t.branches[i], max_weight - w)

        return max_weight * len(weights) + t.label

    do_balance(t)


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"
    # conclusion and proof:
    # see https://oi-wiki.org/misc/two-pointer/#%E5%9C%A8%E5%8D%95%E5%90%91%E9%93%BE%E8%A1%A8%E4%B8%AD%E6%89%BE%E7%8E%AF

    fast, slow = lnk, lnk
    while slow is not Link.empty \
            and slow.rest is not Link.empty\
            and fast is not Link.empty \
            and fast.rest is not Link.empty \
            and fast.rest.rest is not Link.empty:

        slow = slow.rest
        fast = fast.rest.rest

        if slow is fast:
            return True

    return False


def install_camera(t):
    """Calculates the minimum number of cameras that need to be installed.

    >>> t = Tree(0, [Tree(0, [Tree(0), Tree(0)])])
    >>> install_camera(t)
    1
    >>> t = Tree(0, [Tree(0, [Tree(0, [Tree(0)])])])
    >>> install_camera(t)
    2
    """
    "*** YOUR CODE HERE ***"
    res = 0
    def solve(t):
        nonlocal res

        for b in t.branches:
            solve(b)

        if any(b.label == 0 for b in t.branches):
            t.label = 1
            res += 1
        elif any(b.label == 1 for b in t.branches):
            t.label = 2

    solve(t)
    return res + int(t.label == 0)



#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
