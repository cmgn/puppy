# Puppy
<<<<<<< HEAD

Simple like a puppy

#### Examples
```lisp
; partial function application
>>> ((+ 1) 2)
3.0
; the parser will convert this expression
; into the above expression automatically,
; so no need to go on a bracket rampage
>>> (+ 1 2)

3.0
; lists can be constructed like so
>>> ((list 3) ((list 4) ((list 5) 6)))
(3.0, (4.0, (5.0, 6.0)))
; the interpreter has some magic that will
; automatically interpret this as a list, so
; there is no good reason to use the previously
; mentioned syntax
>>> [3 4 5 6]
(3.0, (4.0, (5.0, 6.0)))

; there are a small number of built in functions
; to perform repetitive list operations
>>> (map (+ 1) [1 2 3 4 5])
(2.0, (3.0, (4.0, (5.0, 6.0))))
; + is just a normal function so it can be used anywhere
; where a normal function could be
>>> (fold + [1 2 3 4 5])
15.0
>>> (fold * [1 2 3 4 5])
120.0
>>> (filter (< 2) [1 2 3 4 5])
(3.0, (4.0, 5.0))

; and that's about it
```
=======
>>>>>>> cdd993999523af1629ab8a45b4730590046abd7c
