test = {
  'name': 'fimp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (fimp '(5 2 4 3) 4)
          4
          scm> (fimp '(5 2 4 4 3) 4)
          4
          scm> (fimp '(5 2 4 4 3) 5)
          5
          scm> (fimp '(5 2 4 4 3) 6)
          2
          scm> (fimp '(5 4 4) 3)
          4
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