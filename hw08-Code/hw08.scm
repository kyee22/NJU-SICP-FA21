;;; HW08: Scheme

;;; Required Problems

(define (square x) (* x x))

;;solution of python version:
;def pow(base, exp):
;  if exp == 1:
;    return base
;  elif even(exp):
;    return square(pow(base, exp // 2))
;  else:
;    return mul(x pow(base, exp - 1))
(define (pow base exp)
  (cond

    ((= 1 exp) base)
    ((even? exp) (square (pow base (quotient exp 2))))
    (else (* base (pow base (- exp 1))))

    )
)

;solution of python version:
;def solve(fn, lst):
;  if lst is null:
;    return list()
;  elif fn(lst.first):
;    return list(lst.first, solve(fn, lst.rest))
;  else:
;    return solve(fn, lst.rest)

(define (filter-lst fn lst)
  (cond

    ((null? lst) nil)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst fn (cdr lst)))

    )
)

;;filter-func of python solution:
;if lnk.rest is null:
;  return True
;elif lnk.first != lnk.rest.first:
;  return True
;else:
;  return False

;; Wrong!! function `fn` should apply to link.first (i.e., a int value or else),
;; but `filter` below apply to a link itself (i.e., a list).
;(define (no-repeats s)
;
;  (define (filter lnk)
;    (cond
;
;      ((null? (cdr lnk)) #t)
;      ((not (=  (car lnk) (car (cdr lnk)) ))   #t)
;      (else #f)
;
;      )
;    )
;
;  (filter-lst filter s)
;)
(define (no-repeats s)
  (cond

    ((null? s) nil)
    (else

      (cons
        (car s)
        (no-repeats
          (filter-lst
            (lambda (x) (not (= x (car s))))
            (cdr s)
            )
          )
        )


      )

    )
  )



(define (substitute s old new)
  (cond

    ((null? s) nil)
    ((pair? (car s))

       (cons
             (substitute (car s) old new)
             (substitute (cdr s) old new)
             )
      )


    (else

      (if (eq? (car s) old)

        (cons
            new
            (substitute (cdr s) old new)
          )
        (cons
            (car s)
            (substitute (cdr s) old new)
          )

        )
      )

    )
)


(define (sub-all s olds news)
  (cond


    ((null? olds) s)
    (else
      (sub-all
        (substitute s (car olds) (car news))
        (cdr olds)
        (cdr news)
        )
      )


    )
)


;abstraction barrier!!
; the 4 functions below are the underwater implementation,
; preparing abstraction interface for later application.
(define (tree label branches)
  (cons
    label
    branches
    )
)

(define (label t)
  (car t)
)

(define (branches t)
  (cdr t)
)

(define (is-leaf t)
  (null? (branches t))
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
          (tree 6 (list
            (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))

;abstraction barrier!! - here always see lnk as a Linked List
(define (lnk-map-sum lnk fn)
  (cond
    ((null? lnk) 0)
    (else (+
            (fn (car lnk))
            (lnk-map-sum (cdr lnk) fn)
            ))

    )
)


;abstraction barrier!! - here always see t as a Tree

; version1: use self-defined function `lnk-map-sum`
; (a combination of `reduce` and `map` applying to a linked list)
(define (label-sum t)
  (cond

    ((is-leaf t) (label t))
    (else(+
           (label t)
           (lnk-map-sum (branches t) label-sum)
           ))

    )
)


;; version2: use built-in functions `reduce` and `map`
;(define (label-sum t)
;  (cond
;
;    ((is-leaf t) (label t))
;    (else(+
;           (label t)
;           (reduce + (map label-sum (branches t)))
;           ))
;
;    )
;)


;;; Just for fun Problems

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))
(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  (make-sum
    (derive (first-operand expr) var)
    (derive (second-operand expr) var)
    )
)

(define (derive-product expr var)
  (make-sum

    (make-product
        (derive (first-operand expr) var)
        (second-operand expr)
      )

    (make-product
        (first-operand expr)
        (derive (second-operand expr) var)
      )

    )
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond ((=number? exponent 0) 1)
        ((=number? exponent 1) base)
        ((number? base) (pow base exponent))
        (else (list '^ base exponent)))
)

(define (exp? exp)
    (and (list? exp) (eq? (car exp) '^))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (make-product
    (second-operand exp)
    (make-exp
          (first-operand exp)
          (- (second-operand exp) 1)
      )
    )
)
