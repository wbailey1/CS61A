test = {
  'name': 'HOF',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def first(x):
          ...     x += 8
          ...     def second(y):
          ...         print('second')
          ...         return x + y
          ...     print('first')
          ...     return second
          >>> f = first(15)
          first
          >>> f
          Function
          >>> f(16)
          second
          39
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> stevphen = lambda x: x
          >>> stewart = even(stevphen)
          >>> stewart
          Function
          >>> stewart(61)
          61
          >>> stewart(-4)
          4
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