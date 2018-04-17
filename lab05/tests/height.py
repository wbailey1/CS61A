test = {
  'name': 'Height',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab05 import *
          >>> def height(t):
          ...     if is_leaf(t):
          ...         return 0
          ...     return 1 + max([height(b) for b in branches(t)])
          >>> t = tree(1, [tree(2, [tree(3)])])
          >>> height(t)
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])
          >>> height(t)
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)])])
          >>> height(t)
          2
          >>> t = tree(1)
          >>> height(t)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab05 import *
          >>> def height(t):
          ...     if is_leaf(t):
          ...         current_height = 0
          ...     else:
          ...         current_height = 1 + max([height(subtree) for subtree in subtrees(t)])
          ...     print(current_height)
          ...     return current_height
          >>> t = tree(1, [tree(2, [tree(3)])])
          >>> height(t)
          0
          1
          2
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])
          >>> height(t)
          0
          0
          1
          0
          2
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)])])
          >>> height(t)
          0
          0
          1
          2
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