# -*- coding: utf-8 -*-
"""CSE111-7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HDlIJ42ZLLIZLcLN7FxmzTMVohcR_UyF

https://drive.google.com/file/d/1WDgEyrtDHtyazODi8eebD3Q3WEGaeq06/view
"""

#task 1
class Student:
  def __init__(self, name='Just a student', dept='nothing'):
    self.__name = name
    self.__department = dept
  def set_department(self, dept):
    self.__department = dept
  def get_name(self):
    return self.__name
  def set_name(self,name):
    self.__name = name
  def __str__(self):
    return 'Name: '+self.__name+' Department: '+self.__department
#Write this only >>>>>>>>>>
class BBA_Student(Student):
  def __init__(self, name='default', dept='BBA'):
    super().__init__(name, dept)
#<<<<<<<<Upto this point
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

#task 2
class Vehicle:
  def __init__(self):
    self.x = 0
    self.y = 0
  def moveUp(self):
    self.y += 1
  def moveDown(self):
    self.y -= 1
  def moveRight(self):
    self.x += 1
  def moveLeft(self):
    self.x -= 1
  def __str__(self):
    return '('+str(self.x)+' , '+str(self.y)+')'

#Write this only >>>>>>>>>>
class Vehicle2010(Vehicle):
  def moveLowerLeft(self):
    super().moveDown()
    super().moveLeft()
  def moveLowerRight(self):
    super().moveDown()
    super().moveRight()
  def moveUpperLeft(self):
    super().moveUp()
    super().moveLeft()
  def moveUpperRight(self):
    super().moveUp()
    super().moveRight()
  def equals(self, v2):
    return self.x == v2.x and self.y == v2.y
#<<<<<<<<Upto this point

print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))

#task 3
class Tournament:
  def __init__(self,name='Default'):
    self.__name = name
  def set_name(self,name):
    self.__name = name
  def get_name(self):
    return self.__name

#Write this only >>>>>>>>>>
class Cricket_Tournament(Tournament):
  def __init__(self, name= "Default", num= 0, typ= "No Type"):
    super().__init__(name)
    self.num = num
    self.typ = typ
  def detail(self):
    return f"Cricket Tournament Name: {super().get_name()}\nNumber of Teams: {self.num}\nType: {self.typ}"

class Tennis_Tournament(Tournament):
  def __init__(self, name = "Default", num = 0):
    super().__init__(name)
    self.num = num
  def detail(self):
    return f"Tennis Tournament Name: {super().get_name()}\nNumber of Players: {self.num}"

#<<<<<<<<Upto this point

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

#task 4
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+        "Price: "+str(self.__price)
#Write this only >>>>>>>>>>

class Book(Product):
  def __init__(self, id, title, price, isbn, publisher):
    super().__init__(id, title, price)
    self.isbn = isbn
    self.publisher = publisher
  def printDetail(self):
    return f"{super().get_id_title_price()} ISBN: {self.isbn} Publisher: {self.publisher}"
class CD(Product):
  def __init__(self, id, title, price, band, duration, genre):
    super().__init__(id, title, price)
    self.band = band
    self.duration = duration
    self.genre = genre
  def printDetail(self):
    return f"{super().get_id_title_price()} Band: {self.band} Duration: {self.duration} minutes Genre: {self.genre}"

#<<<<<<<<Upto this point
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())

#task 5
class Animal:
    def __init__(self,sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound

class Printer:
    def printSound(self, a):
        print(a.makeSound())

#Write this only >>>>>>>>>>
class Dog(Animal):
  def __init__(self, sound): #or, just write pass instead of creating a seperate init
    super().__init__(sound)
class Cat(Animal):
  def __init__(self, sound): #or, just write pass instead of creating a seperate init
    super().__init__(sound)

#<<<<<<<<Upto this point
d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)

#task 6
class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

#Write this only >>>>>>>>>>
class triangle(Shape):
  def __init__(self, name = "Default", height = 0, base = 0): #you can skip init for this subclass
    super().__init__(name, height, base)
  def calcArea(self):
    return 1/2*self.base*self.height
  def printDetail(self):
    return f"Shape name: {self.name}\n{super().get_height_base()}\nArea: {self.calcArea()}"
class trapezoid(Shape):
  def __init__(self, name = "Default", height = 0, base = 0, side = 0):
    super().__init__(name, height, base)
    self.side = side
  def calcArea(self):
    return 1/2*(self.base+self.side)*self.height
  def printDetail(self):
    return f"Shape name: {self.name}\n{super().get_height_base()}, Side_A: {self.side}\nArea: {self.calcArea()}"
#<<<<<<<<Upto this point

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

#task 7
class SportsPerson:
  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0
  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team
#Write this only >>>>>>>>>>

class Player(SportsPerson):
  def __init__(self, team, name, role, goal, game):
    super().__init__(team, name, role)
    self.earning_per_match = (goal * 1000) + (game * 10)
    self.goal = goal
    self.game = game
  def calculate_ratio(self):
    self.ratio = self.goal/self.game
  def print_details(self):
    print(f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.game}\nGoal Ratio: {self.ratio}\nMatch Earning: {self.earning_per_match}K")
class Manager(SportsPerson):
  def __init__(self, team, name, role, win):
    super().__init__(team, name, role)
    self.win = win
    self.earning_per_match = win * 1000
  def print_details(self):
    print(f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Win: {self.win}\nMatch Earning: {self.earning_per_match}K")
#<<<<<<<<Upto this point
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

#task 7
class SportsPerson:
  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0
  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#Write this only >>>>>>>>>>
class Player(SportsPerson):
  def __init__(self, team, name, role, goal, game):
    super().__init__(team, name, role)
    self.earning_per_match = (goal*1000) + (game*10)
    self.goal= goal
    self.game= game
  def calculate_ratio(self):
    self.ratio= self.goal/self.game
  def print_details(self):
    print(f"{super().get_name_team()} \nTeam Role: {self.role} \nTotal Goal: {self.goal}, Total Played: {self.game} \nGoal Ratio: {self.ratio} \nMatch Earning: {self.earning_per_match}K")
class Manager(SportsPerson):
  def __init__(self, team, name, role, win):
    super().__init__(team, name, role)
    self.earning_per_match = (win*1000)
    self.win= win
  def print_details(self):
    print(f"{super().get_name_team()} \nTeam Role: {self.role}, \nTotal Win: {self.win} \nMatch Earning: {self.earning_per_match}K")
#<<<<<<<<Upto this point
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()