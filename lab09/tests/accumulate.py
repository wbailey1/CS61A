test = {
  'name': 'accumulate',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate + 0 4 square)
          8a1df3cf221256374ccf6cefb730a46e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09_extra)
      scm> (define (square x) (* x x))
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate * 3 3 identity)
          130586a2ba9e2882c4a61e11881a9612
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09_extra)
      scm> (define (identity x) x)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate + 1 5 add-one)
          7d0935e9b0eb4047d5cea4f7a2d102b7
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09_extra)
      scm> (define (add-one x) (+ x 1))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}