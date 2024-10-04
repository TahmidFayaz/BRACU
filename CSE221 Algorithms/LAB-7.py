# -*- coding: utf-8 -*-
"""221-7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BNJLz4yzs0ofQFxzC2n8yAy5y243ugTA
"""

#Task 1

input_file = open("input1_2.txt" , "r")
output_file = open("output1_2.txt" , "w")

n, m = (map(int, input_file.readline().strip().split(" ")))

person = [None] * n
connect = [1] * n

for i in range(1, n):
  person[i] = i

def find(r, c):
  if person[r] == r:
    return (r,c)
  return find(person[r], c)

for i in range(m):
  u, v = (map(int, input_file.readline().strip().split(" ")))

  a, c1 = find(u, connect[u])
  b, c2 = find(v, connect[v])

  if a != b:
    person[a] = b
    connect[a] += c2
    connect[b] += c1

  output_file.write(str(connect[b]) + "\n")

input_file.close()
output_file.close()

#Task 2

input_file = open("input2_2.txt" , "r")
output_file = open("output2_2.txt" , "w")

n, m = (map(int, input_file.readline().strip().split(" ")))

person = [None] * (n + 1)
lis_of_ver = []
direct = [[i] for i in range(n + 1)]

for i in range(1, n + 1):
  person[i] = i

def find(r):
  if person[r] == r:
    return r
  return find(person[r])

for i in range(m):
    u, v, w = (map(int, input_file.readline().strip().split(" ")))
    lis_of_ver.append((w, u, v))
lis_of_ver.sort()

count = 0
for i in lis_of_ver:
  a = find(i[1])
  b = find(i[2])
  if a != b:
    person[b] = a
    count += i[0]

output_file.write(str(count))

input_file.close()
output_file.close()

#Task 3

input_file = open("input3_4.txt" , "r")
output_file = open("output3_4.txt" , "w")

n = int(input_file.readline())

arr = [-1] * (n+1)

def dist_ways(arr, n):
  if n <= 2:
    return n
  if arr[n] == -1:
    arr[n] = dist_ways(arr, n - 1) + dist_ways(arr, n - 2)
  return arr[n]

freddy = dist_ways(arr, n)
output_file.write(str(freddy))

input_file.close()
output_file.close()

#Task 4

import math

input_file = open("input4_1.txt" , "r")
output_file = open("output4_1.txt" , "w")

n, m = (map(int, input_file.readline().strip().split(" ")))

C_list = list(map(int, input_file.readline().strip().split(" ")))

def C_change(n, c):
  m = [0] * (n + 1)
  for p in range(1, n + 1):
    op = n + 1
    for i in c:
      if i <= p and (1 + m[p-i]) < op:
        op = 1 + m[p-i]

    m[p] = op
  if m[n] > n:
    return -1
  return m[n]

req = C_change(m, C_list)
output_file.write(str(req))

input_file.close()
output_file.close()