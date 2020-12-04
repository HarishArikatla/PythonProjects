# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:22:41 2020

@author: sis
"""



from covid import Covid

covid = Covid()

print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())

cases = covid.get_status_by_country_name("india") 
for x in cases:
    print(x, ":", cases[x])