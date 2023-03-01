#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

if -1 <= x1 - x3 <= 1 and -1 <= x2 - x4 <= 1:
    print('YES')
else:
    print('NO')

