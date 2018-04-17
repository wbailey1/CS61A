test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2))
          0
          """,
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3 . 4))
          1
          """,
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 (3 . 5)))
          1
          """,
        },
        {
          'code': r"""
          scm> (how-many-dots '(6 . (6 . (6))))
          0
          """,
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) . 3))
          2
          """,
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) (3 . 4) 5 . 6))
          3
          """,
        },
      ],
      'setup': r"""
      scm> (load 'quiz03)
      """,
    },
  ]
}