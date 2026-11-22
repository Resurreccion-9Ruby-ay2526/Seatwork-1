# ICT 10 Seatwork #1: Understanding Data Type
from pyscript import display # type: ignore


name = 'Khail Matteo'
age = 15
height2 = 177.8
countrieslist_ = ['Korea', 'USA', 'Vietnam']
student_type = False
student_info = {
   "color": 'Purple',
   "car_brand": 'Mitsubishi',
   "shoe_size": 11,
   "best_friend": 'Lucas'
}
favorite_fruits = {'Apple', 'Banana', 'Watermelon', 'Green Mango', 'Orange'}
daysofweek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


display(type(name), target='result')
display(type(age), target='result')
display(type(height2), target='result')
display(type(countrieslist_), target='result')
display(type(student_type), target='result')
display(type(student_info), target='result')
display(type(favorite_fruits), target='result')
display(type(daysofweek), target='result')
