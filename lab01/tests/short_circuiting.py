test = {
  'name': 'Veritasiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          13
          >>> False or 0
          0
          >>> not 10
          False
          >>> not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> True and 1 / 0 and False
          Error
          >>> True or 1 / 0 or False
          True
          >>> True and 0
          0
          >>> False or 1
          1
          >>> 1 and 3 and 6 and 10 and 15
          15
          >>> 0 or False or 2 or 1 / 0
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}