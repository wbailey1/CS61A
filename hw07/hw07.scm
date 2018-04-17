(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0)
  )
)


(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) b)
    ((= (remainder n 2) 0) (square (pow b (/ n 2))))
    (else (* b (pow b (- n 1))))
  )
)


(define (ordered? s)
  (define (helper s max)
    (cond
      ((null? (cdr s)) True)
      ((and (>= (car (cdr s)) (car s)) (>= (car (cdr s)) max)) (helper (cdr s) (car (cdr s))))
      (else False)
    )
  )
  (helper s 0)
)

(define (nodots s)
  (if (pair? (car s))
    (cond
      ((null? (cdr s)) (cons (nodots(car s)) nil))
      ((integer? (cdr s)) (cons (nodots(car s)) (cons (cdr s) nil)))
      (else (cons (nodots (car s)) (nodots (cdr s))))
    )
    (cond
      ((null? (cdr s)) (cons (car s) nil))
      ((integer? (cdr s)) (cons (car s) (cons (cdr s) nil)))
      (else (cons (car s) (nodots (cdr s))))
    )
  ) 
)



; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
  (cond
    ((empty? s) False)
    ((= (car s) v) True)
    (else (contains? (cdr s) v))
  )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
  (cond 
    ((empty? s) (list v))
    ((contains? s v) s)
    ((> (car s) v) (cons v s))
    (else (cons (car s) (add (cdr s) v)))
  )
)

(define (intersect s t)
  (cond 
    ((or (empty? s) (empty? t)) nil)
    ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
    ((< (car s) (car t)) (intersect (cdr s) t))
    ((> (car s) (car t)) (intersect s (cdr t)))
  )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  (cond
    ((empty? s) t)
    ((empty? t) s)
    ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
    ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
    ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
  )
)


