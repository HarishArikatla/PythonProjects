# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:21:30 2020

@author: sis
"""


from pycricbuzz import Cricbuzz
c=Cricbuzz()
matches=c.matches()
for match in matches:
    print(match)
    if(match['mchstate']!='nextlive'):
        print(c.livescore(match['id']))
        