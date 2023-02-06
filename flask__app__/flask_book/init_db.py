from datetime import date
from app import db, Employee

db.drop_all()
db.create_all()

e1 = Employee(id='id',
              title='title',
              description='description',
              price='price',
              date_add='date_add',
              status='404'
              )

e2 = Employee(id='id2',
              title='title2',
              description='description2',
              price='price2',
              date_add='date_add2',
              status='404'
              )

e3 = Employee(id='id3',
              title='title3',
              description='description3',
              price='price3',
              date_add='date_add3',
              status='404'
              )

e4 = Employee(id='id4',
              title='title4',
              description='description4',
              price='price4',
              date_add='date_add4',
              status='404'
              )

e5 = Employee(id='id5',
              title='title5',
              description='description5',
              price='price5',
              date_add='date_add5',
              status='404'
              )

e6 = Employee(id='id6',
              title='title6',
              description='description6',
              price='price6',
              date_add='date_add6',
              status='404'
              )

e7 = Employee(id='id7',
              title='title7',
              description='description7',
              price='price7',
              date_add='date_add7',
              status='404'
              )

e8 = Employee(id='id8',
              title='title8',
              description='description8',
              price='price8',
              date_add='date_add8',
              status='404'
              )

e9 = Employee(id='id9',
              title='title9',
              description='description9',
              price='price9',
              date_add='date_add9',
              status='404'
              )

db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9])

db.session.commit()
