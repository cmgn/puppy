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
; or alternatively, they can be written as
>>> (map (x -> (+ x 1)) [1 2 3])
[2.0, 3.0, 4.0]

; variables can be defined as follows
>>> (define add-one (+ 1))
>>> (add-one 4)
5
``` 

## Todo
- document stdlib.py
- unit tests for lib.py and parse.py 
- re-make lexer and re-assign duties such as expanding lambdas to the parser