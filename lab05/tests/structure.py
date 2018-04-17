test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The tree structure for the following is:
              1
            / | \
           2  3  4
             /
            5
          """
        },
        {
          'answer': '1, 6, 5, 4',
          'choices': [
            '1, 6, 5',
            '1, 6, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}