# -*- coding: utf-8 -*-
"""Lab06_SheikhMdTahmid_22299522.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1txMBQnjMflARjycYM2-ZqyPXvdzwqU5h
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""Task 1

You will have to complete the vehicleNodes constructor and then

implemenet the __hash_function() and insert_vehicle() methods.
"""

class vehicleNodes:
  def __init__(self, brand, vehicle_type, rent, passenger, next = None):
    #TO DO
    self.brand=brand
    self.vehicle_type=vehicle_type
    self.rent=rent
    self.passenger=passenger
    self.next=next

class VehicleHashTable:
  def __init__(self, size):
    self.vehicleTable = [None]*size
    self.empty_slot = {}
    for i in range(size):
      self.empty_slot[i] = False

  def create_from_vehicle_info_array(self, arr):
    for i in arr:
      self.insert_vehicle(i)

  def print_vehicle_hashtable(self):
    idx = 0
    for i in self.vehicleTable:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(Brand: {head.brand}, Type: {head.vehicle_type}, Rent: {head.rent}, No. of Passengers: {head.passenger})', end = '---->')
        head = head.next
      print('None')
      print()
      idx += 1

  def find_empty_slot(self):
    for k,v in self.empty_slot.items():
      idx = k
      del self.empty_slot[k]
      return idx


  #Do it by yourself
  def __hash_function(self, brand):
      def sum(brand):
          if brand=="":
            return 0
          else:
            return ord(brand[0]) + sum(brand[1:])

      index = sum(brand)% len(vehicle_info)
      if index in self.empty_slot:
          del self.empty_slot[index]
      return index


  #Do it by yourself
  def insert_vehicle(self, vehicle):
        brand, vehicle_type, rent, passenger = vehicle
        n = vehicleNodes(brand, vehicle_type, rent, passenger)
        index = self.__hash_function(brand)


        if self.vehicleTable[index] == None:
            self.vehicleTable[index] = n

        elif self.vehicleTable[index] != None and self.vehicleTable[index].brand !=brand:
          empty_slot = self.find_empty_slot()
          self.vehicleTable[empty_slot] = n

        else:
          if brand==self.vehicleTable[index].brand:
            n.next = self.vehicleTable[index]
          self.vehicleTable[index] = n

    #TO DO

#DRIVER CODE
vehicle_info = [('Toyota', 'Private Car', 500, 4), ('Jeep', 'SUV', 950, 6), ('Lamborghini', 'SUV', 6900, 6), ('Hyundai', 'Bike', 100, 1),
                ('BMW', 'Private Car', 1000, 8), ('Honda', 'Bike', 150, 1), ('Ferrari', 'Private Car', 2500, 4), ('BMW', 'Minivan', 5800, 7)]

vt = VehicleHashTable(len(vehicle_info))

vt.create_from_vehicle_info_array(vehicle_info)
print("============== Printing The HashTable ==============")
vt.print_vehicle_hashtable()

# should print
# 0 : (Brand: Toyota, Type: Private Car, Rent: 500, No. of Passengers: 4)---->None

# 1 : (Brand: Lamborghini, Type: SUV, Rent: 6900, No. of Passengers: 6)---->None

# 2 : (Brand: Hyundai, Type: Bike, Rent: 100, No. of Passengers: 1)---->None

# 3 : (Brand: Honda, Type: Bike, Rent: 150, No. of Passengers: 1)---->None

# 4 : (Brand: Jeep, Type: SUV, Rent: 950, No. of Passengers: 6)---->None

# 5 : (Brand: Ferrari, Type: Private Car, Rent: 2500, No. of Passengers: 4)---->None

# 6 : (Brand: BMW, Type: Minivan, Rent: 5800, No. of Passengers: 7)---->(Brand: BMW, Type: Private Car, Rent: 1000, No. of Passengers: 8)---->None

# 7 : None

"""Task 2

Complete the following methods:

__hash_function()

search_hashtable()
"""

class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    if self.search_hashtable(s) == 'Found':
      print(s,'Already Inserted. Cannot reinsert.')
      print('===============================')
      return
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(key: {head.key}, value: {head.value})', end = '-->')
        head = head.next
      print('None')
      print()
      idx += 1


  #Do it by yourself
  def __hash_function(self, key):
    string=key
    if len(key)%2!=0:
      string=key+"N"
    sum=0
    for i in range(0,len(string),2):
      ASCII = str(ord(string[i])) + str(ord(string[i+1]))
      sum += int(ASCII)

    index=sum%len(self.ht)
    return index

  #Do it by yourself
  def search_hashtable(self, s):
    index = self.__hash_function(s[0])
    if index>len(self.ht):
      return "Not Found"
    temp = self.ht[index]

    while temp:
        if temp.key == s[0]:
          return "Found"
        temp = temp.next

    return "Not Found"

#Driver Code
arr = [('Colt', 360), ('Cordelius', 730), ('Shelly', 300), ('Doug', 1200), ('Emz', 520), ('Bo', 580)]
ht = Hashtable(5)
ht.create_from_array(arr)
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Doug', 1200))
unittest.output_test(result, 'Found')
print(f'(Doug, 1200) {result}')

print('======================')
ht.insert(('Doug', 1200))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Not Found')
print(f'(Edgar, 320) {result}')

print('======================')
ht.insert(('Edgar', 320))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Found')
print(f'(Edgar, 320) {result}')

"""Task 3

Implement the __hash_function() and insert() methods
"""

class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()


  #Do it by yourself
  def __hash_function(self, key):
    sum=0
    if len(key)%2!=0:
      for i in range(1,len(key),2):
        sum+=ord(key[i])
    else:
      for i in range(0,len(key),2):
        sum+=ord(key[i])

    index=sum%len(self.ht)
    return index


  #Do it by yourself
  def insert(self, key, value):
        n = Node((key, value))
        index = self.__hash_function(key)
        if self.ht[index].value == None:
            self.ht[index] = n
        else:
            prev = None
            current = self.ht[index]
            while current != None:
                if current.value[1] < value:
                    if prev == None:
                        n.next = current
                        self.ht[index] = n
                    else:
                        prev.next = n
                        n.next = current
                    return
                prev = current
                current = current.next
            prev.next = n

#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->

"""Task 4

Implement the __hash_function() and remove() methods
"""

class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'({head.key}, {head.value})', end = '-->')
        head = head.next
      print('None')
      idx += 1


  #Do it by yourself
  def __hash_function(self, key):
    index=(key+3)%6
    return index

  #Do it by yourself
  def remove(self, key):
        index = self.__hash_function(key)
        prev = None
        current = self.ht[index]

        while current != None:
            if current.key == key:
                if prev == None:
                    self.ht[index] = current.next
                else:
                    prev.next = current.next
                return self.ht
            prev = current
            current = current.next

        return self.ht

#Driver Code
arr=[(34, 'Abid') , (4, 'Rafi'), (6, 'Karim'), (3, 'Chitra'), (22, 'Nilu')]
ht = Hashtable(6)
ht.create_from_array(arr)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(9)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')
print('======================')

ht.remove(4)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

