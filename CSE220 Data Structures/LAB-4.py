# -*- coding: utf-8 -*-
"""Lab04_Sheikh Md Tahmid_22299522.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B8cnLtheNWOUyuWH5o1xEGkpIV10XXXo
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""**Assignment Part 1: Doubly Linked List**

For Assignment Part 1, you should write your full code in the following cells along with your driver codes on your own.
"""

#Assignment Part 1

class Patient:
  def __init__(self, id, name, age, bloodgroup):
    self.id = id
    self.name = name
    self.age = age
    self.blood = bloodgroup
    self.next = None
    self.prev = None

class WRM:

  def __init__(self):
    dh = Patient(None, None, None, None)
    dh.next = dh
    dh.prev = dh
    self.head = dh

  def RegisterPatient(self, id, name, age, bloodgroup):
    p = Patient(id, name, age, bloodgroup)
    checkID = True
    h = self.head.next
    while( h != self.head):
      if h.id == id:
        checkID = False
        break
      h = h.next
    if checkID:
      last = self.head.prev
      p.next = self.head
      p.prev = last
      last.next = p
      self.head.prev = p
      print("\nPatient Added Successfully.\n")
    else:
      print("\nUnsuccessful! ID already taken.\n")

  def ServePatient(self):
    if self.head.next == self.head:
        print('\nNo.patient left to serve\n')
    else:
        p = self.head.next
        print(f'\nPatient Name: {p.name} is served.\n')
        secnext = p.next
        secnext.prev = self.head
        self.head.next = secnext
        del p

  def CancelAll(self):
    if self.head.next == self.head:
        print('\nNo appointment left to be cancelled.\n')
        return
    h = self.head.next
    while h != self.head:
        t = h.next
        del h
        h = t
    self.head.next = self.head
    self.head.prev = self.head
    print('\nAll appointments are cancelled successfully. Doctor can go to lunch.\n')

  def CanDoctorGoHome(self):
    if self.head.next == self.head:
        return True
    else:
        return False

  def ShowAllPatient(self):
    if self.head.next == self.head:
        print("No Patient in WRM")
    h= self.head.next
    print("\nAll Patient's Name:")
    while(h != self.head):
        print(f"{h.name}")
        h = h.next

  def reverseTheLine(self):
    h = self.head.next
    while(h != self.head):
      temp=h.next
      h.next=h.prev
      h.prev= temp
      h=temp
    temp=h.next
    h.next=h.prev
    h.prev=temp

#Write a Tester Code in this cell
def Tester_Code():
  print("** Waiting Room Management System**")
class WRM:
  w = WRM()
  while(True):
    print('Choose an option: (1,2,3... pick a number)\n')
    print('1 - Register a patient.')
    print('2 - Serve a patient.')
    print('3 - Cancel all apointment')
    print('4 - Check if doc can go home')
    print('5 - Show all patient.')
    print('6 - Reverse the LIne.')
    print('7 - To Exit.')

    n = input("\nEnter your choice: \n")

    if int(n) == 1:
      print("\nexecuting RegisterPatient()......\n")
      id = input('Enter ID: ')
      name = input('Enter Name: ')
      age = input('Enter Age: ')
      bloodgroup = input('Enter Blood Group: ')
      w.RegisterPatient(id, name, age, bloodgroup)
    elif int(n) == 2:
      w.ServePatient()
    elif int(n) == 3:
      w.CancelAll()
    elif int(n) == 4:
      if w.CanDoctorGoHome():
        print("\nYes, doctor can go home.\n")
      else:
        print("\nNo doctor cannot go home.\n")
    elif int(n) == 5:
      w.ShowAllPatient()
    elif int(n) == 6:
      w.reverseTheLine()
      print("\nreversing the line suppccesfull\n")
    elif int(n) == 7:
      print("\nThank you for using Waiting Room Management System\n")
      break
    else:
      print('\nInvalid option.\n')
      continue


Tester_Code()

"""**Assignment Part 2: Stack**

Linked List based Stack is implemented in the following cell.
"""

class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None

#You can run this driver code cell to understand the methods of Stack class
st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)

print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print(st.isEmpty())

"""You can print your stack using this code segment"""

def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
# print_stack(st)
# print('------')

"""Task 1: Diamond Count"""

def diamond_count(stack,string):
  DC=0
  for i in string:
    if i=="<":
      stack.push(i)
    elif i==">":
      if not stack.isEmpty():
        stack.pop()
        DC+=1
  return DC



print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')

"""Task 2: Tower of Blocks"""

def remove_block(stack, n):
  new_Stack=Stack()
  count=1

  while not st.isEmpty():
    if count!=n:
      new_Stack.push(st.pop())
      count+=1
    else:
      st.pop()
      break

  while not new_Stack.isEmpty():
    st.push(new_Stack.pop())

  return st


print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

"""Task 3: Stack Reverse"""

def conditional_reverse(stack):
  temp=Stack()

  while not st.isEmpty():
    if st.peek()!=temp.peek():
      temp.push(st.pop())
    else:
      st.pop()

  return temp



print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')