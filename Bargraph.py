# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:22:59 2020

@author: sis
"""


import numpy as np
import matplotlib.pyplot as plt



data = {'Amazon':39, 'Walmart':6, 'Ebay':5,'Apple':4}

courses = list(data.keys()) 

values = list(data.values())
fig = plt.figure(figsize = (3, 5)

plt.bar (courses, values, color ='maroon', width = 0.4)

plt.xlabel ("Companies")

plt.ylabel ("Market Captured in Percentage")

plt.title("% Share of US Retail e-commerce")
plt.show()
