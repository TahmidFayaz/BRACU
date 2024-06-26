# -*- coding: utf-8 -*-
"""LAB05_SheikhMdTahmid_22299522.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wEiwmXhOBGR5yb2_ICDxh37sdDghixVp
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
import math

#Run this cell
class Node:
  def __init__(self, elem, next = None):
    self.elem = elem
    self.next = next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

"""***Very Easy***"""

#a)
def recursive_sum(arr1,i=0,sum=0):
  if i==len(arr1):
    return sum
  else:
    if arr1[i]>0 and arr1[i]%2==0:
          sum+=arr1[i]
          recursive_sum(arr1,i+1,sum)
    return  recursive_sum(arr1,i+1,sum)

arr1 = np.array([10,34,-8,1,5,6])
returned_value = recursive_sum(arr1)
print(f'Sum of even positive elements of an array: {returned_value}') # This should print 50
unittest.output_test(returned_value, 50)

#b)
def recursive_multiply(head,product=1):

  if head==None:
    return product
  else:
    if head.elem>0 and head.elem%2!=0:
      product*=head.elem
    return recursive_multiply(head.next,product)


arr1 = np.array([10,3,-9,1,5,6])
head= create_linked_list(arr1)
returned_value = recursive_multiply(head)
print(f'Product of odd positive elements of a linked list: {returned_value}') # This should print 15
unittest.output_test(returned_value, 15)

#c)
def nCr(n,r):
  if r==0 or n==r:
    return 1
  else:
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

print('========1========')
returned_value = nCr(9,6)
print(f'9C6: {returned_value}') # This should print 84
unittest.output_test(returned_value, 84)
print('========2========')
returned_value = nCr(8,2)
print(f'8C2: {returned_value}') # This should print 28
unittest.output_test(returned_value, 28)
print('========3========')
returned_value = nCr(48,1)
print(f'48C1: {returned_value}') # This should print 48
unittest.output_test(returned_value, 48)

#d)
def count_digit_recursive(num,count=0):

  if num%10==num:
    return count+1

  else:
    return count_digit_recursive(num/10,count+1)


returned_value = count_digit_recursive(7508)
print(f'Number of Digits: {returned_value}') # This should print 4
unittest.output_test(returned_value, 4)

#e)
def check_prime_recursive(num,div=0,a=1):
  if div>2:
    return False
  elif num==a:
    return True
  else:
    if num%a==0:
      return check_prime_recursive(num,div+1,a+1)
    else:
      return check_prime_recursive(num,div,a+1)




print('========1========')
returned_value = check_prime_recursive(79)
print(f'Prime: {returned_value}') # This should print True
unittest.output_test(returned_value, True)
print('========2========')
returned_value = check_prime_recursive(391)
print(f'Prime: {returned_value}') # This should print False
unittest.output_test(returned_value, False)

from logging import currentframe
#f)
def recursive_print(head):
  if head==None:
    return
  else:
    recursive_print(head.next)
    print(head.elem,end=" ")

arr1 = np.array([10,20,30,40])
head= create_linked_list(arr1)
recursive_print(head) #This should print 40  30  20  10

"""**Easy**"""

#a)
def dec_to_binary_recursive(n):
  if n==0:
    return ""

  result = n//2
  remainder = n%2
  y=dec_to_binary_recursive(result)

  return str(y)+str(remainder)



print('========1========')
returned_value = dec_to_binary_recursive(35)
print(f'Binary Number: {returned_value}') # This should print 100011
unittest.output_test(returned_value, '100011')
print('========2========')
returned_value = dec_to_binary_recursive(50)
print(f'Binary Number: {returned_value}') # This should print 110010
unittest.output_test(returned_value, '110010')

#b)
#you may use this for decimal to hexadecimal mapping of 0-15
def encoding(dec_number): #0<=dec_number<=15
  return '0123456789ABCDEF'[dec_number]

def dec_to_hexa_recursive(n):

  if n < 16:
    return encoding(n)
  number = encoding(n % 16)
  return dec_to_hexa_recursive(n//16) + number


print('Use of encoding function')
decimal_number = 7
print(f'Hexadecimal Number: {encoding(decimal_number)}')
decimal_number = 13
print(f'Hexadecimal Number: {encoding(decimal_number)}')

print('========1========')
returned_value = dec_to_hexa_recursive(1230)
print(f'Hexadecimal Number: {returned_value}') # This should print 4CE
unittest.output_test(returned_value, '4CE')
print('========2========')
returned_value = dec_to_hexa_recursive(600)
print(f'Hexadecimal Number: {returned_value}') # This should print 258
unittest.output_test(returned_value, '258')

from os import X_OK
#c)
def print_alphabets_recursive(head):
  #To Do
  List=["A","a","I","i","O","o","E","e","U","u"]
  if head.next==None:
    print(head.elem,end=" ")
  else:
    if head.elem in List:
      print(head.elem,end=" ")
      print_alphabets_recursive(head.next)
    else:
      print_alphabets_recursive(head.next)
      print(head.elem,end=" ")

head = create_linked_list(np.array(['b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l']))
print_alphabets_recursive(head) #This will print e a u i u l f t b

#d)
def harmonic_sum(n,x=1,sum=0):
  if x>n:
    return sum
  else:
    if x%2==0:
      return harmonic_sum(n,x+1,sum-1/x)
    else:
      return harmonic_sum(n,x+1,sum+1/x)

print(f'Harmonic Sum(3): {harmonic_sum(3)}') #This should print 0.8333333333333333
print(f'Harmonic Sum(4): {harmonic_sum(4)}') #This should print 0.5833333333333333

"""***Medium***"""

#a)
def hoc_Builder(height,counter=1,cards=0):
  if height==0:
    return 0
  else:
    if counter>height:
      return cards
    elif counter==height:
      return hoc_Builder(height,counter+1,cards+8)
    else:
      return hoc_Builder(height,counter+1,cards+5)

print(f'Cards Needed: {hoc_Builder(4)}') #This should print 23
unittest.output_test(hoc_Builder(4), 23)
print(f'Cards Needed: {hoc_Builder(1)}') #This should print 8
unittest.output_test(hoc_Builder(1), 8)
print(f'Cards Needed: {hoc_Builder(0)}') #This should print 0
unittest.output_test(hoc_Builder(0), 0)

#b)
def reach_goal(n,steps=0):
  if n==1:
    return steps
  else:
    if n%2==0:
      return reach_goal(n/2,steps+1)
    else:
      return reach_goal((n*3)+1,steps+1)

steps=reach_goal(21)
print(f'Number of steps to reach the goal: {steps}')  #This should print 7
unittest.output_test(steps, 7)

"""***Hard***"""

#a)
def print_row(n):
  #To Do
  if n<=0:
    print(n,end=' ')
    return
  else:
    print(n,end=' ')
    print_row(n-5)
    print(n,end=' ')

def print_pattern(n,space=" "):
  if n<=0:
    return
  print(space,end=" ")
  print_row(n)
  print()
  space=space+" "+" "*len(str(n))
  print_pattern(n-5,space)


print('========1========')
n = 16
print_pattern(n)
#This should print

#16 11 6 1 -4 1 6 11 16
#   11 6 1 -4 1 6 11
#      6 1 -4 1 6
#        1 -4 1

print('========2========')
n = 10
print_pattern(n)
#This should print

#10 5 0 5 10
#   5 0 5

#b)
def merge(mid_list, final_list, combined_list, x, y):
    if x>=0 and y>=0:
        if mid_list[x] > final_list[y]:
            combined_list.append(mid_list[x])
            merge(mid_list, final_list, combined_list, x-1, y)
        else:
            combined_list.append(final_list[y])
            merge(mid_list, final_list, combined_list, x, y-1)

    elif x>=0:
        combined_list.append(mid_list[x])
        merge(mid_list, final_list, combined_list, x-1, y)

    elif y>=0:
        combined_list.append(final_list[y])
        merge(mid_list, final_list, combined_list, x, y-1)

    return combined_list

def merge_Lists(mid_list, final_list,combined_list):
    result = merge(mid_list, final_list, [], len(mid_list)-1, len(final_list)-1)

    return result


mid=[5, 7, 14, 20, 24]
final=[10, 12, 25]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [25, 24, 20, 14, 12, 10, 7, 5]

mid=[11, 20, 24, 28]
final=[10, 12]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [28, 24, 20, 12, 11, 10]

"""***Very Hard***"""

def flatten_List(given_list, output_list):

  if len(given_list) < 1:
    return output_list
  else:
    if type(given_list[0]) == list:
       (flatten_List(given_list[0], output_list))
    else:
      output_list.append(given_list[0])
    return (flatten_List(given_list[1:], output_list))


given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flatten_List(given_list, []) # Initial empty list is sent for update
print(output_list)
#This should print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

"""***Bonus Task***"""

def number_of_ways(steps):
  if steps<=1:
    return 1
  elif steps==2:
    return 2
  else:
    return number_of_ways(steps-1)+number_of_ways(steps-2)+number_of_ways(steps-3)

print(f'The number of ways you can climb the stairs: {number_of_ways(3)}') #This should print 4
print(f'The number of ways you can climb the stairs: {number_of_ways(5)}') #This should print 13