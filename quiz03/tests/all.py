test = {
  'name': 'all',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (all number? '(1 2 3 4))     ; True or False
          True
          scm> (all list? '(1 2 3 4))       ; True or False
          False
          scm> (all list? '((1 2) (3 4))))  ; True or False
          True
          scm> (all list? '((1 2 3) 4))     ; True or False
          False
          scm> (all (lambda (x) (> x 5)) '(7 8 3 9))
          False
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