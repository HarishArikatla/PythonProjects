1
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:01:20 2020

@author: sis
"""


while True:
    balance=10000
    print("ATM")
    print("""
    1)balance
    2)withdraw
    3)deposit
    4)Quit """)
    try:
        option=int(input("enter option:"))
    except Exception as e:
        print("Error:",e)
        print("enter 1,2,3 or 4 only")
        continue
    if option==1:
        print("Balance $ ",balance)
    if option==2:
        print("Balance $ ",balance)
        withdraw=float(input("Enter withdraw amount $"))
        if Withdraw>0:
            forewardbalance=(balance-Withdraw)
            print("foreward balance $ ",forewardbalance)
        elif Withdraw>balance:
            print("no fuds in account")
    if option==3:
        print("Balance $ ",balance)
        Deposit=float(input("enter deposit amount $ "))
        if Deposit>0:
            forwardbalance=(balance+deposit)
        else:
            print("none deposit made")
    if option==4:
        exit()
