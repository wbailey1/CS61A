test = {
  'name': 'double',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from options where meal != "snack";
          breakfast|2|La Val's, Sliver
          lunch|4|Emilia's, La Val's, Pizzahhh, Sliver
          dinner|3|Cheeseboard, La Val's, Sliver
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read quiz04.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}