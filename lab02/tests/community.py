test = {
  'name': 'Community',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def troy():
          ...     abed = 0
          ...     while abed < 3:
          ...         britta = lambda: abed
          ...         print(abed)
          ...         abed += 2
          ...     annie = abed
          ...     annie += 1
          ...     abed = 6 # seasons and a movie
          ...     return britta
          >>> jeff = troy()
          b33f256984c474b4181f5512601c4a70
          dcbe12f5edfd80d067e49a65db66d0b1
          # locked
          >>> shirley = lambda: jeff
          >>> pierce = shirley()
          >>> pierce()
          13e9492c801fddcd5c1330b411f26ac8
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}