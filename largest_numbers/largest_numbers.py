#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f_m = -1
s_m = -1
n = int(input())

for _ in range(n):
    a = int(input())
    if a > f_m:
        s_m = f_m
        f_m = a
    elif a > s_m:
        s_m = a
print(f_m, s_m, sep='\n')

