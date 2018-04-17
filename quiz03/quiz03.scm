; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

; Filter (from lab) takes a predicate procedure f and a list s. It returns a
; new list containing only elements x in s for which (f x) is a true value.
(define (filter f s)
    (cond ((null? s) '())
          ((f (car s)) (cons (car s) (filter f (cdr s))))
          (else (filter f (cdr s))))
)

; All takes a predicate procedure f and a list s. It returns whether (f x) is
; a true value for every element x in s.
(define (all f s)
  (cond
    ((null? s) True)
    ((and (f (car s)) (all f (cdr s))) True)
    (else False)
  )
)

; Every takes a two-argument predicate g and a list s. It returns a new list
; containing only elements x in s for which (g x y) is true for every y in s.
(define (every g s)
  (define (gs y)
    (define (h x)
      (g (car y) x)
    )
    (cond
      ((null? y) nil)
      ((all h s) (cons (car y) (gs (cdr y))))
      (else (gs (cdr y)))
    )
  )
  (gs s)
)

; Return a minimum card.
(define (min hand) (car (every <= hand)))

; Fimp returns the card played under the fimping strategy in Cucumber.
(define (fimp hand highest)
  (define (f hand)
    (define (higher x)
      (>= x highest)
    )
    (filter higher hand)
  )
  (if (not (null? (f hand)))
    (min (f hand))
    (min hand)
  )
)


; Legal returns pairs of (card . control) for all legal plays in Cucumber.
(define (legal hand highest)
  (define least (min hand))
  (define (result hand)
    (if (null? hand)
      nil 
      (begin
        (define card (car hand))
        (if (>= card highest)
          (cons (cons card True) (result (cdr hand)))
          (if (eq? card least)
            (cons (cons card False) (result (cdr hand)))
            (result (cdr hand))
          )
        )
      )
    )
  )
  (result hand)
)


