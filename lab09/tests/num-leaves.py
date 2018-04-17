test = {
  'name': 'num-leaves',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (num-leaves nil)
          3e92404229d40b73cf8dd05dcfa23ea9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves test-tree)
          242a6d3d4ed1b1d1292acd307083f4e0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves (right test-tree))
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves (left test-tree))
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}