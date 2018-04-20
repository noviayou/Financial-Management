#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:07:01 2018

@author: noviayou
"""

import numpy as np
#01
C = 0.06  #coupon rate
N = 14  #number of years
I = 0.1
Par = -1000
pv=np.pv(rate=I,nper=N,pmt=C*Par,fv=Par)  #present value of given pmt
print ("1.The current bond price is","{:,.2f}".format(pv))

#02
C = 0.09  #coupon rate
N = 14
Pv = 850.46   #current bond price
Par = -1000
rate=np.rate(nper=N,pmt=C*Par,pv=Pv,fv=Par)  #interest rate function
print ("2.The rate is","{:,.2f}".format(rate*100),"%")

#03
N = 6 
Pv = 970   # current bond price 
I = 0.099   #YTM
Par = -1000 
pmt=np.pmt(rate=I,nper=N,pv=Pv,fv=Par)  #pmt function
C = pmt/Par
print ("3.The coupon rate should be","{:,.2f}".format(C*100),"%")

#04
N = 19*2  #number of years with semiannual payment
C = 0.094/2  #coupon rate 
Pv = 1020  #current bond price
Par = -1000
rate = np.rate(nper=N,pmt=C*Par,pv=Pv,fv=Par)  #interest rate function
YTM = rate*2
print ("4.The YTM is","{:,.2f}".format(YTM*100),"%")

#05
Realr = 0.055
Infr = 0.02
TR = ((1+Infr)*(1+Realr))-1  #Fisher Equation to get the treasury bill rate
print ("5.The Treasury bill rate should be","{:,.2f}%".format(TR*100))


#06
Totrate = 0.095
Infr = 0.05
Realr = ((1+Totrate)/(1+Infr)-1)  #Fisher Equation
print ("6.The real interest rate should be","{:,.2f}%".format(Realr*100))


#07
CJ = 0.05/2
CK = 0.11/2
N = 7*2
I = 0.07/2
Par = -1000
pvJ=np.pv(rate=I,nper=N,pmt=CJ*Par,fv=Par)  #current bond price for Bond J
pvK=np.pv(rate=I,nper=N,pmt=CK*Par,fv=Par)  #current bond price for Bond K

#a&b
I1 = (0.07+0.02)/2
pvJ1=np.pv(rate=I1,nper=N,pmt=CJ*Par,fv=Par)  #current bond price for Bond J with increasing rate
pvK1=np.pv(rate=I1,nper=N,pmt=CK*Par,fv=Par)  #current bond price for Bond K with increasing rate 

print ("7a.The precentage price change of Bond J is","{:,.2f}".format((pvJ1-pvJ)/pvJ
       *100),"%")
print ("7b.The precentage price change of Bond K is","{:,.2f}".format((pvK1-pvK)/pvK
       *100),"%")
#c&d
I2 = (0.07-0.02)/2
pvJ2=np.pv(rate=I2,nper=N,pmt=CJ*Par,fv=Par)  #current bond price for bond J with decreasing rate
pvK2=np.pv(rate=I2,nper=N,pmt=CK*Par,fv=Par)  #current bond price for bond K with decreasing rate
print ("7c.The precentage price change of Bond J is","{:,.2f}".format((pvJ2-pvJ)/pvJ
       *100),"%")
print ("7d.The precentage price change of Bond K is","{:,.2f}".format((pvK2-pvK)/pvK
       *100),"%")

#08
C = 0.104/2 # Coupon rate
Pv = -1013.04 # Selling Price
Par = 1000 # Par Value
N = 11*2 # Number
rate=np.rate(nper=N,pmt=C*Par,pv=Pv,fv=Par)  #YTM function
pmt=np.pmt(rate=rate,nper=N,pv=Par,fv=Par)   #use the YTM to get new PMT
Coupon = -pmt/Par  #get the coupon payment
print ("8.The coupon rate is","{:,.2f}%".format(Coupon*100))

#09
C = 0.076/2 #Coupon Rate
CP = 1180 # Clean Price
Par = 1000 # Par Value
AI = (C*Par)*(4/6) # Accrued Interest
IP = CP+AI
print ("9.Invoice Price should be ${:,.2f}".format(IP))

#10
C = 5
EAR = 0.114
Month = 52 #1 year for 52 weeks
N = 32 # Number of Year
Growth=0.036 # Growth rate & Inflation rate
realr = ((1+EAR)/(1+Growth)) - 1 # Real Return Weekly Rate
APR = ((1+realr)**(1/Month)-1)*Month # Yearly Interest Rate
WeeklyR = APR/Month # Weekly Interest Rate
pv = np.pv(rate=WeeklyR,nper=N*Month,pmt=-C,fv=0)
print ("10.Present Value of Comitment should be $","{:,.2f}".format(pv))

