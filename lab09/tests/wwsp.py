test = {
  'name': 'What would Scheme print?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 3 5)
          8
          scm> (- 10 4)
          6
          scm> (* 7 6)
          42
          scm> (/ 28 2)
          14
          scm> (+ 1 2 3 4)
          10
          scm> (/ 8 2 2)
          2
          scm> (quotient 29 5)
          5
          scm> (remainder 29 5)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (= 1 3)      ; True or False?
          False
          scm> (> 1 3)
          False
          scm> (< 1 3)
          True
          scm> (<= -1 -1)
          True
          scm> (or True False)
          True
          scm> (and True True)
          True
          scm> (and True False (/ 1 0))     ; Short-circuiting
          False
          scm> (not True)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 3)      ; Defining variables
          x
          scm> x
          3
          scm> (define y (+ x 4))
          y
          scm> y
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}