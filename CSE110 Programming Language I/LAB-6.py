# -*- coding: utf-8 -*-
"""CSE110-6prac.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15pbGzj0CXGbVKM_pj9vsUl2UwUuEiMAG
"""

#task 1
a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717, [1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))
print(a_tuple[3][3])

#task 2
x= input()[1:-1]
l1= x.split(", ")
for i in range(len(l1)):
  l1[i]= int(l1[i])
print(tuple(l1[2:-2]))

#task 3
book_info = (
("Best Mystery & Thriller","The Silent Patient",68,821),
("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),
("Best Fiction","The Testaments",98,291)
)
a,b,c,d= book_info
print("Size of the tuple is:", len(book_info))
print(f"{a} \n{b} \n{c} \n{d}")

#task 4
book_info = (("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291))
for i in book_info:
  a,b,c= i
  print(f"{b} won the '{a}' category with {c} votes")

#task 5
Given_tuple= (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
count= 0
y= int(input())
for i in Given_tuple:
  if i==y:
    count+=1
print(f"{y} appears {count} times in the tuple")

#task 6
x1= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
x2= []
for i in range(len(x1)-1,-1,-1):
  x2.append(x1[i])
print(tuple(x2))

#task 7
d1= {'Harry':15, 'Draco':8, 'Nevil':19}
d2= {'Ginie':18, 'Luna': 14}
d3= {}
d3.update(d1)
d3.update(d2)
print(d3)

#task 8
d1= {}
x= input().split(", ")
count= 0
sum= 0
for i in x:
  i= x.index(i)
  x[i]= x[i].split(":")
  d1.update({x[i][0]: int(x[i][1])})
  count += 1
  sum += d1[x[i][0]]
print("Average is:", sum//count)

#task 9
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165,
              'Pierre Cox': 190}
d= {}
x= int(input())
for i in exam_marks:
  if exam_marks[i] >= x:
    d.update({i: exam_marks[i]})
print(d)

#task 10
dict1= {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
dict1_values= list(dict1.values())
dict1_keys= list(dict1.keys())
max= dict1_values[0]
for i in dict1.values():
  if i > max:
    max = i
print(f"The highest selling book genre is '{dict1_keys[dict1_values.index(max)]}' and the number of books sold are {max}.")

#task 11
input1= input()[1:-1]
s= ""
dict1= {}
for i in input1.lower():
  if i != " ":
    if i not in dict1:
      dict1[i] = 1
    else:
      dict1[i] += 1
print(dict1)

#task 12
dict1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count= 0
for i in dict1:
  for j in dict1[i]:
    count += 1
print(count)

#task 13
list1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dict1= {}
for i in list1:
  if i[0] not in dict1:
    dict1[i[0]] = [i[1]]
  else:
    dict1[i[0]].append(i[1])
print(dict1)

dict1 = {'a':59 , 'b':-82 , 'c':5 , 'd':-81 , 'e':53}
for i in dict1:
    j = 0
    k = 22
    while j < 5:
        if j % 2 == 0:
            k = dict1[i] + j - (8 + k % 6) / 3
            print("loop k", k)
            dict1[i] = dict1[i]+ int(k)
        else:
            k = dict1[i] + j - (6 - k % 8) * 3
            dict1[i] = dict1[i] - int(k)
        j += 1
    print(int(k))
    print(i + " -> " + str(dict1[i]))

d1={1:[2,3,4], 2:[4,5,6], 3:[15]}
d2= d1
d3= d2.copy()

for i in d1:
  for j in range(len(d1[i])):
    if(j==0):
      d2[i][j]= d1[i][j]+d3[i][j]
      print(d2[i][j])
    if (j>0):
      d3[i][j]= d1[i][j-1] - d2[i][j]
    else:
      d3[i][j]= d1[i][j] - d2[i][j]
    print(d3[i][j])
  print(i+d1[i][0]+len(d3))

d1= {"0": (3, 4), "1": (2, 3), "2": (1,2), "3": (1, 0), "5": (1, 6), "6": (1, 5), "7": (2, 1)}
order = 0
num = ""
for order in range(0, len(d1), 1):
  for i in d1:
    if(d1[i][1] == order):
      num += i*d1[i][0]
print(num)