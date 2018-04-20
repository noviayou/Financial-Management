#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:12:17 2018

@author: noviayou
"""

#1a
D=1.32 #dividend paid at T0
G=0.06 #constant growth rate
R=0.1  #require rate of reture
P0=D*((1+G)/(R-G))
print ("1a: The current price is ","${:,.2f}".format(P0))

#1b
P10=D*((1+G)**11/(R-G))
print ("1b: The price in 10 years is ","${:,.2f}".format(P10))

#2
D1=4.55  #dividend ar time 1
G=0.03  #constant groth rate
PV=40  #current stock price
R=D1/PV+G
print ("2: The requrie rate of return is","{:,.2f}".format(R*100),"%")

#3
D1=4.90
G=0.043
R=0.079
PV=D1/(R-G)
print ("3: The company's current price is","${:,.2f}".format(PV))

#4
PV=90
R=0.1
Dyield=0.5*R #the total return on the stock is evenly divided between a capital gains yield and a dividend yield
D1=PV*Dyield  #dividend for next year is the stock price times dividend yield
D0=D1/(1+Dyield)#dividend this year
print ("4: The current dividend is","${:,.2f}".format(D0))

#5
import numpy as np
D=-25  #dividend as pmt
N=7
I=0.1
PV=np.pv(rate=I,nper=N,pmt=D)
print ("5: The current stock price is","${:,.2f}".format(PV))

#6
D1=1.4
G=0.06
Ired=0.089  #the require rate of return for Red company
Iyellow=0.119  #the require rate of return for Yellow company
Iblue=0.153    #the require rate of return for Blue company
#a 
PRed=D1/(Ired-G) 
print ("6a: The stock price for Red Inc., is","${:,.2f}".format(PRed))
#b
PYellow=D1/(Iyellow-G)
print ("6b: The stock price for Yellow Inc., is","${:,.2f}".format(PYellow))
#c
PBlue=D1/(Iblue-G)
print ("6c: The stock price for Blue Inc., is","${:,.2f}".format(PBlue))

#7
D1=11
n=15  
G=0.04   
R=0.12
P15=D1/(R-G)  #calculate value at t=15
PV=np.pv(rate=R,nper=n,pmt=0,fv=-P15)  #discount back value at n=15
print ("7: The current price is","${:,.2f}".format(PV))

#8
D1=13
D2=11
D3=9
D4=5
G=0.08
R=0.17
P5=D4*((1+G)/(R-G))  #calculate value at t=5
PV5=np.pv(rate=R,nper=5,pmt=0,fv=-P5)   #discount back value at t=5 to t0
PV4=np.pv(rate=R,nper=4,pmt=0,fv=-D4)   #discount D4 back to t0
PV3=np.pv(rate=R,nper=3,pmt=0,fv=-D3)   #discount D3 back to t0
PV2=np.pv(rate=R,nper=2,pmt=0,fv=-D2)
PV1=np.pv(rate=R,nper=1,pmt=0,fv=-D1)
PV=PV5+PV4+PV3+PV2+PV1                  #add discounted future cash flow
print ("8: The current price is", "${:,.2f}".format(PV))

#9
G1=0.18
n=3
G2=0.04
R=0.07
D=1.60
D1=D*(1+G1)
D2=D*((1+G1)**2)     #calculate Dividend at t2
D3=D*((1+G1)**3)     #calculate dividend at t3
D4=D3*(1+G2)        #calculate dividend at t4
P4=(D4*(1+G2))/(R-G2)      #value at t4
PV4=np.pv(rate=R,nper=4,pmt=0,fv=-P4)
PV3=np.pv(rate=R,nper=3,pmt=0,fv=-D3)
PV2=np.pv(rate=R,nper=2,pmt=0,fv=-D2)
PV1=np.pv(rate=R,nper=1,pmt=0,fv=-D1)   #discounct back future cash flow
PV=PV4+PV3+PV2+PV1+D
print ("9: The current price is", "${:,.2f}".format(PV))

#10
D=18
R=0.19
G=-0.12
PV=D*(1+G)/(R-G)
print ("10: Today,you will pay","${:,.2f}".format(PV))

#11
PV=75
R=0.11
G=0.05
div=(PV*(R-G))/(1+G)
print ("11: The current dividend is","${:,.2f}".format(div))

#12
D=14
R=0.07
P5=D/R
PV=np.pv(rate=R,nper=5,pmt=0,fv=-P5)   #discount back future cash flow
print ("12: The current stock price is","${:,.2f}".format(PV))

#13
D=1.30
G1=0.35
G2=0.05
R=0.14
N=9
P1=(D*(1+G1)/(R-G1))*(1-((1+G1)/(1+R))**N)   #the first part of cash flow
P2=(((1+G1)/(1+R))**N)*(D*(1+G2)/(R-G2))   #discount back growth rate future cash flow
print ("13: Price of Stock Today is","${:,.2f}".format(P1+P2))



