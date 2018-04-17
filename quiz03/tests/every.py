test = {
  'name': 'every',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (every >= '(2 3 4 1))
          (4)
          scm> (every >= '(4 2 3 4))
          (4 4)
          scm> (every = '(4 2 3 4))
          ()
          scm> (every (lambda (x y) (<= (abs (- x y)) 1)) '(4 2 3 4))
          (3)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}