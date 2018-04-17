test = {
  'name': 'double',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from double where name="La Val's";
          breakfast|dinner|La Val's
          breakfast|snack|La Val's
          lunch|snack|La Val's
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read quiz04.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}