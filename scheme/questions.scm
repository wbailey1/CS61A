(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (cond
  	((eq? items nil) nil)
  	((eq? (cdr items) nil) (cons (proc (car items)) nil))
  	(else (cons (proc (car items)) (map proc (cdr items))))
  )
)

(define (cons-all first rests)
  (cond
  	((eq? rests nil) nil)
  	((eq? (cdr rests) nil) (cons (cons first (car rests)) nil))
  	(else (cons (cons first (car rests)) (cons-all first (cdr rests))))
  )
)

(define (contains? l i)
  (if (null? l)
  	#f
  	(or
  		(eq? (car l) i) (contains? (cdr l) i)
  	)
  )
)

(define (zip pairs)
  (cond
  	((null? pairs) (list nil nil))
  	((contains? (map null? pairs) True) nil)
  	(else (cons (map car pairs) (zip (map cdr pairs))))
  )
)

;; Problem 18
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN Question 18
  (define (helper count s)
  	(cond
  		((eq? s nil) nil)
  		((eq? (cdr s) nil) (cons (cons count (cons (car s) nil)) nil))
		(else (cons (cons count (cons (car s) nil)) (helper (+ 1 count) (cdr s))))
  	)
  )
  (helper 0 s)
)
  ; END Question 18

;; Problem 19
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN Question 19
  (cond
  	((= total 0) (list nil))
  	((or (eq? denoms nil) (< total 0)) nil)
  	(else 
  		(define using_m (list-change (- total (car denoms)) denoms))
  		(append (cons-all (car denoms) using_m) (list-change total (cdr denoms)))
  	)	
  )
)
  ; END Question 19

;; Problem 20
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (analyze expr)
  (cond ((atom? expr)
         ; BEGIN Question 20
         expr
         ; END Question 20
         )
        ((quoted? expr)
         ; BEGIN Question 20
         expr
         ; END Question 20
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
          (append (cons form (cons params nil)) (map analyze body))
           ; END Question 20
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
          (define zipvalues (zip (map analyze values)))
          (append (list (cons 'lambda (cons (car zipvalues) (cons (car (map analyze body)) nil)))) (cadr zipvalues))
           ; END Question 20
           ))
        (else
         ; BEGIN Question 20
		(map analyze expr)
         )
         ; END Question 20
         ))

;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'REPLACE-THIS-LINE
  )
  ; END Question 21

