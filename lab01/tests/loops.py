test = {
  'name': 'Loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0: # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> n = 4
          >>> while n > 0: # If this loops forever, just type Infinite Loop
          ...     n += 1
          ...     print(n)
          Infinite Loop
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def go(n):
          ...     if n % 2 != 0:
          ...         print(n / 2)
          ...         return
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4) # If this loops forever, just type Infinite Loop
          4
          2
          1
          >>> go(5) # If this loops forever, just type Infinite Loop
          2.5
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