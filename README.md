# Puppy

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
[3.0, 4.0, 5.0, 6.0]
; the interpreter has some magic that will
; automatically interpret this as a list, so
; there is no good reason to use the previously
; mentioned syntax
>>> [3 4 5 6]
[3.0, 4.0, 5.0, 6.0]

; there are a small number of built in functions
; to perform repetitive list operations
>>> (map (+ 1) [1 2 3 4 5])
[2.0, 3.0, 4.0, 5.0, 6.0]
; + is just a normal function so it can be used anywhere
; where a normal function could be
>>> (fold + [1 2 3 4 5])
15.0
>>> (fold * [1 2 3 4 5])
120.0
>>> (filter (< 2) [1 2 3 4 5])
[3.0, 4.0, 5.0]

; lambda expressions are defined as follows
>>> (map (lambda x (+ x 1)) [1 2 3])
[2.0, 3.0, 4.0]
; currently they can only take one argument, thus
; any functions requiring more than one argument must 
; make use of nested lambdas
; I am looking to provide mechanism by which a lambda
; can be declared with more than one argument, which the
; interpreter will transform into a nested series of lambdas,
; however this is a long way away.

; and that's about it
``` 

## Todo
- document stdlib.py
- better error handling
- unit tests for lib.py and parse.py 
