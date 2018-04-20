#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:39:56 2018

@author: noviayou
"""

#2
#a
import pandas as pd
data = {"Year" : [0,1,2,3,4,5,6,7,8,9,10,11], "CF" : [-2960,740,740,740,740,740
        ,740,740,740,740,740,740]}
cft = pd.DataFrame(data, columns=["Year", "CF"])

N = cft.iloc[0]["CF"]/740

#i = 0
#unpaid = cft.iloc[0]["CF"]
#while unpaid < 0:
#    unpaid = cft.iloc[i]["CF"] + cft.iloc[i+1]["CF"]
#    if unpaid < cft.iloc[i+2]["CF"]:
#        leftunpaid = -unpaid/cft.iloc[i+2]["CF"]
#        break
#    i = i + 1
#    
#noyears = i + 1
#payback = noyears + leftunpaid
print ("2a. Payback year is", "{:,.2f}".format(-N))

#b
data2 = {"Year2" : [0,1,2,3,4,5,6,7,8,9,10,11], "CF2" : [-4366,740,740,740,740,
         740,740,740,740,740,740,740]}
cft2 = pd.DataFrame(data2, columns=["Year2", "CF2"])

N = cft2.iloc[0]["CF2"]/740
#i = 0
#unpaid2 = cft2.iloc[0]["CF2"]
#while unpaid2 < 0:
#    unpaid2 = cft2.iloc[i]["CF2"] + cft2.iloc[i+1]["CF2"]
#    if unpaid2 < cft2.iloc[i+2]["CF2"]:
#        leftunpaid2 = -unpaid2/cft2.iloc[i+2]["CF2"]
#        break
#    i = i + 1
#    
#noyears2 = i + 1
#payback2 = noyears2 + leftunpaid2
print ("2b. Payback year is", "{:,.2f}".format(-N))   

#c
data3 = {"Year3" : [0,1,2,3,4,5,6,7,8,9,10,11], "CF3" : [-8880,740,740,740,740,
         740,740,740,740,740,740,740]}
cft3 = pd.DataFrame(data3, columns=["Year3", "CF3"])

N = cft3.iloc[0]["CF3"]/740
#i = 0
#unpaid3 = cft3.iloc[0]["CF3"]
#while unpaid3 < 0:
#    unpaid3 = cft3.iloc[i]["CF3"] + cft3.iloc[i+1]["CF3"]
#    if unpaid3 < cft3.iloc[i+2]["CF3"]:
#        leftunpaid3 = -unpaid3/cft3.iloc[i+2]["CF3"]
#        break
#    i = i + 1
#    
#noyears3 = i + 1
#payback3 = noyears3 + leftunpaid3
print ("2c. Payback year is", "{:,.2f}".format(-N))    


#3
data4 = {"Year4" : [0,1,2,3,4], "CF4" : [-7000,4200,5300,6100,7400]}
cft4 = pd.DataFrame(data4, columns = ["Year4","CF4"])
R = 0.14
i = 0
unpaid4 = cft4.iloc[0]["CF4"]
while unpaid4 < 0:
    unpaid4 = cft4.iloc[i]["CF4"]/((1+R)**i) + cft4.iloc[i+1]["CF4"]/((1+R)**(i+1))
    if unpaid4 <  cft4.iloc[i+2]["CF4"]/((1+R)**(i+2)):
        leftunpaid = 


  
















