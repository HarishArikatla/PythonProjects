# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:45:07 2020

@author: sis
"""



import socket 


hostname = socket.gethostname() 

IPAddr = socket.gethostbyname(hostname) 


print("Your Computer Name is:" + hostname) 


print("Your Computer IP Address is:" + IPAddr) 