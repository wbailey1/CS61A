test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_car.model
          'Tesla'
          >>> johns_car.gas = 10
          >>> johns_car.drive()
          'Tesla goes vroom!'
          >>> johns_car.drive()
          'Tesla cannot drive!'
          >>> johns_car.fill_gas()
          Your car is full.
          >>> johns_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> Car.headlights
          2
          >>> johns_car.headlights
          2
          >>> Car.headlights = 3
          >>> johns_car.headlights
          3
          >>> johns_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_car.wheels = 2
          >>> johns_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> johns_car.drive()
          'Tesla cannot drive!'
          >>> Car.drive()
          Error
          >>> Car.drive(johns_car)
          'Tesla cannot drive!'
          >>> MonsterTruck.drive(johns_car)
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> sumukhs_car = MonsterTruck('Batmobile')
          >>> sumukhs_car.drive()
          Vroom! This Monster Truck is huge!
          'Batmobile goes vroom!'
          >>> Car.drive(sumukhs_car)
          'Batmobile goes vroom!'
          >>> MonsterTruck.drive(sumukhs_car)
          Vroom! This Monster Truck is huge!
          'Batmobile goes vroom!'
          >>> Car.rev(sumukhs_car)
          Error
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