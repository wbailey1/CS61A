;; Extra Scheme Questions ;;

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
)


; Q10
(define (num-leaves tree)
  'YOUR-CODE-HERE
)

; Q11
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      'YOUR-CODE-HERE
  )
)


; Binary Tree ADT
(define (make-btree entry left right)
  (cons entry (cons left right)))

(define (entry tree)
  (car tree))

(define (left tree)
  (car (cdr tree)))

(define (right tree)
  (cdr (cdr tree)))

(define test-tree
  (make-btree 2
              (make-btree 1
                          nil
                          nil)
              (make-btree 4
                          (make-btree 3
                                      nil
                                      nil)
                          nil)))

; test-tree:
;     2
;    / \
;   1   4
;      /
;     3
