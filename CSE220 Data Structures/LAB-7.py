# -*- coding: utf-8 -*-
"""Lab07_SheikhMdTahmid_22299522.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UE7JLJILf2gqH02QfjC2YthraHAsdhb2
"""

class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)

def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)

"""Task 1"""

def convert_mirror(root):

  if root==None:
    return root

  else:

    x = BTNode(root.elem)

    x.left=convert_mirror(root.right)
    x.right=convert_mirror(root.left)

    return x



#DRIVER CODE
root = BTNode(10)
n1 = BTNode(20)
n2 = BTNode(30)
n3 = BTNode(40)
n4 = BTNode(60)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  40 20 60 10 30
print()

root2 = convert_mirror(root)
print('Mirrored Tree Inorder Traversal: ', end = ' ')
inorder(root2) #Mirrored Tree Inorder Traversal:  30 10 60 20 40

"""Task 2"""

def smallest_level(root,D={},level=0):

  if root==None:
    return D

  if level not in D or root.elem < D[level]:
    D[level]=root.elem

  smallest_level(root.left,D,level=level+1)
  smallest_level(root.right,D,level=level+1)

  return D


#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 -5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}

"""Task 3"""

def inorder_predecessor(root, x):

  if root == None:
    return None
  if root.elem >= x.elem:
    return inorder_predecessor(root.left, x)
  if root.elem < x.elem:
    pre = inorder_predecessor(root.right, x)
    if pre == None:
      return root
    else:
      return pre




#DRIVER CODE
root = BTNode(20)
n1 = BTNode(8)
n2 = BTNode(22)
n3 = BTNode(4)
n4 = BTNode(12)
n5 = BTNode(10)
n6 = BTNode(14)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n4.left = n5
n4.right = n6

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  4 8 10 12 14 20 22
print()

x = root
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 20: 14

"""Task 4"""

def LCA(root, x, y):
  if root == None:
    return None
  if x == root.elem or y == root.elem:
    return root.elem
  if x < root.elem and y < root.elem :
    return LCA(root.left, x, y)
  elif x > root.elem and y > root.elem:
    return LCA(root.right, x, y)
  else:
    return root.elem


#DRIVER CODE
#Write by yourself from the given tree
root = BTNode(15)
n1 = BTNode(10)
n2 = BTNode(25)
n3 = BTNode(8)
n4 = BTNode(12)
n5 = BTNode(20)
n6 = BTNode(30)
n7 = BTNode(6)
n8 = BTNode(9)
n9 = BTNode(18)
n10 = BTNode(22)

root.left=n1
root.right=n2

n1.left=n3
n1.right=n4

n2.left=n5
n2.right=n6

n3.left=n7
n3.right=n8

n5.left=n9
n5.right=n10

#check all the sample inputs given
print(LCA(root,6,12))
print(LCA(root,20,6))
print(LCA(root,18,22))
print(LCA(root,20,25))
print(LCA(root,10,12))

"""Task 5"""

def sumTree(root):

  return LevelSum(root)

def LevelSum(root,level=0):

  if root==None:
    return 0
  else:
    if level==0:
      sum = root.elem
    else:
      sum = root.elem % level

    sum += LevelSum(root.left,level+1)
    sum += LevelSum(root.right,level+1)

    return sum


# To DO
#you can declare as many helper function with extra parameters as you need .
#You can not modify the parameters of sumTree or modify any part of the given code.

#Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15

"""Task 6"""

def swap_child(root, level, M):

  if root==None or level > M:
    return root

  if level < M:
    root.left,root.right = root.right, root.left

  left = swap_child(root.left,level+1,M)
  right = swap_child(root.right,level+1,M)

  return root

#Driver Code
root=BTNode("A")
n1=BTNode("B")
n2=BTNode("C")
n3=BTNode("D")
n4=BTNode("E")
n5=BTNode("F")
n6=BTNode("G")
n7=BTNode("H")
n8=BTNode("I")
n9=BTNode("J")

root.left=n1
root.right=n2

n1.left=n3
n1.right=n4

n2.right=n5

n3.left=n6
n3.right=n7

n4.left=n8


n5.left=n9


#Write other nodes by yourself from the given tree of Doc File


print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H

"""Task 7"""

def sum(root):
  if root==None:
    return 0
  else:
    LS=sum(root.left)
    RS=sum(root.right)

    return LS + RS +root.elem

def subtract_summation(root):
  if root==None:
    return 0
  else:
    LSubtree=sum(root.left)
    RSubtree=sum(root.right)

  return LSubtree - RSubtree



#Driver Code
root=BTNode(71)
n2=BTNode(27)
n3=BTNode(62)
n4=BTNode(80)
n5=BTNode(75)
n6=BTNode(41)
n7=BTNode(3)
n8=BTNode(87)
n9=BTNode(56)
n10=BTNode(19)
n11=BTNode(89)

root.left=n2
root.right=n3

n2.left=n4
n2.right=n5

n3.left=n6
n3.right=n7

n4.left=n8
n4.right=n9

n7.left=n10
n7.right=n11


#Write other nodes by yourself from the given tree of Doc File

print(subtract_summation(root)) #This should print 111

"""Bonus Task"""

def level_sum(root):
  #To Do
  result = calculate_sum(root,1)

  return result
def calculate_sum(root,level=0):

  if root==None:
    return 0
  else:
    if level %2 != 0:
      return -root.elem + calculate_sum(root.left,level+1)+ calculate_sum(root.right,level+1)
    else:
      return root.elem + calculate_sum(root.left,level+1)+ calculate_sum(root.right,level+1)


root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8

print(level_sum(root)) #This should print 4

def max(x,y):
  if x>y:
    return x
  else:
    return y

def height(node):
  if node == None:
    return 0

  LHeight = height(node.left)
  RHeight = height(node.right)
  return max(LHeight+RHeight)+1