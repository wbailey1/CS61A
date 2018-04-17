test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          True
          >>> not '' or not 0 and False
          True
          >>> 13 and False
          False
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