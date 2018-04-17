test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          (5 4 2)
          """
        },
        {
          'code': r"""
          scm> (no-repeats '(1 2 3 4))
          (1 2 3 4)
          """,
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 3 3 5 5))
          (1 3 5)
          """,
        },
        {
          'code': r"""
          scm> (no-repeats '(3 2 1 2 3))
          (3 2 1)
          """,
        },
        {
          'code': r"""
          scm> (no-repeats '(4 2 4 5))
          (4 2 5)
          """,
        },
      ],
      'setup': r"""
      scm> (load 'quiz03)
      """,
    },
  ]
}
