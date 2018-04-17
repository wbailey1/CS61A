;; Scheme ;;

; Q2
(define (cube x)
  (* x x x)
)


; Q3
(define (over-or-under x y)
  (if (< x y)
  	-1
  	(if (= x y)
  		0
  		1))
)


; Q4
(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
)
  

; Q5
(define (remove item lst)
  (cond
  	((null? lst) '())
  	((= item (car lst)) (remove item (cdr lst)))
  	(else (cons (car lst) (remove item (cdr lst))))
  )
)

;;; Tests

(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


; Q6
(define (filter f lst)
    (if (null? lst)
        nil
        (begin
            (define first (car lst))
            (define rest (cdr lst))
            (cond
                ((f first) (cons first (filter f rest)))
                (else (filter f rest))
            )
        )
    )
)


; Q7
(define (make-adder num)
  (lambda (x) (+ x num))
)


; Q8
(define (composed f g)
  (lambda (x)
    (f (g x))
  )
)

