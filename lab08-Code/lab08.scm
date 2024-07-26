;;; Lab08: Scheme

;;version1:
;(define (over-or-under a b)
;  (if (< a b) -1
;              (if (= a b) 0 1
;                )
;    )
;)

;version1:
(define (over-or-under a b)
  (cond
    ((< a b) -1)
    ((= a b) 0)
    (else 1)
    )
)


;;version1:
;(define (make-adder n)
;  (lambda (x) (+ x n))
;)

;version2:
(define (make-adder n)
  (define (foo x) (+ x n))
  foo
)

;;verison1:
;(define (composed f g)
;  (lambda (x) (f (g x)))
;)

;verison2:
(define (composed f g)
  (define (foo x) (f (g x)))
  foo
)

;;;; solution of python version
;  def gcd(a, b):
;    if b == 0:
;        return a
;    return gcd(b, a % b)
;;;;


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0) a
              (gcd b (remainder a b))
    )
)


(define lst
  (cons (cons 1)
        (cons 2 (cons
                  (cons 3 (cons 4))
                  (cons 5)
                  )
          )
    )
)

;def solve(lnk):
;  if link.rest is Link.empty:
;    return True
;  else:
;    if solve(prev.rest):
;      return link.first > link.rest.first
;    else:
;      return false

(define (ordered s)
  (define (solve s)
    (cond

      ((null? (cdr s)) #t)
      ((solve (cdr s))
            (if (not (> (car s) (car (cdr s)))) #t #f)
        )
      (else #f)

      )
    )

  (solve s)
)
