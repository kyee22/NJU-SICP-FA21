# Note



##  Call Expressions 和 Special Forms

如下交互结果所示：

```scheme
scm> (define foo (lambda (x y z) (if x y z)))
foo
scm> (foo 1 2 (print 'hi))
hi
2
scm> (if 1 2 (print 'hi))
2
```

*   `(foo 1 2 (print 'hi))`  属于 Call Expression，就算 `1` 真值为真，也会 evaluate `(print 'hi)`；
*   `(if 1 2 (print 'hi))` 属于 Special Form，`1` 真值为真，则不会 evaluate `(print 'hi)`。



## no-repeats

**Algorithm in Python: **

def no_repeats(lnk):

1.   若 $\rm lnk$ 为空链表，则返回空链表；

     ```python
     if lnk is Link.empty:
         return Link.empty
     ```

2.   否则，保留 $\rm lnk.first$；

3.   并去掉 $\rm lnk.rest$ 中与 $\rm lnk.first$ 相同的那些节点，得到 $\rm lnk'$；

     ```python
     filter(lambda x: x != lnk.first, lnk.rest)
     ```

3.   对 $\rm lnk'$ 递归地重复步骤 1-3。

     ```python
     no_repeats(lnk.rest)
     ```

由于 **Scheme** 中不存在 **语句**，也不存在 **可变对象**。所以上面提到的 “保留”“去掉”等动作其实都需要一个等效的 creat a new list 动作。

