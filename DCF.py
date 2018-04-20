#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:20:00 2018

@author: noviayou
"""

#1
import numpy as np
import math
pva="-31000" #present value 
n=14  #the year
r=0.0625  #the discount rate
pmt=np.pmt(rate=r,nper=n,pv=int(pva),fv=0)
print ("Annual cash flow is" , "{:,.2f}".format(pmt))

#2
pmt=1200  #the PMT
pv=61000  #the present value
r=int(pmt)/int(pv)  #the formula for interest rate
print ("interest rate per month :","{:,.2f}".format(r*100),"%")

#3
import numpy as np
pva=-100  #present value
fva=300  #future value
n=24  #72 months equals 24 quarters
rate=np.rate(nper=n,pmt=0,pv=pva,fv=fva)  #interest rate function
print ("The rate of return per quarter is","{:,.3f}".format(rate*100),"%")

#4
n=16
g=0.05
r=0.1
payment=540000
A=(1+g)/(1+r)
B=A**n
pv=(payment/(r-g))*(1-B)  #The growing annuity payment formula
print ("Present value of winings is","{:,.2f}".format(pv))

#5
pmt=-380  #the PMT
i=0.08  #the interest rate
fv=25694  #the future value
n=np.nper(rate=i,pmt=pmt,pv=0,fv=fv)  #number of payments function
print ("There are","{:,.0f}".format(n),"payments")

#6
n=360
I=0.076/12
pmt=-800
pv=np.pv(rate=I,nper=n,pmt=pmt)  #present value of given pmt
ball=230000-pv
ballfv=np.fv(nper=n,rate=I,pmt=0,pv=-ball)  #future value of ballpayment
print ("The ballpayment should be","{:,.2f}".format(ballfv))

#7
pmt=17000
pv=-0.8*2800000
n=30*12
fv=0
rate=np.rate(nper=n,pmt=pmt,pv=pv,fv=fv)  
print ("The APR is","{:,.2f}".format(rate*12*100))
EAR=((1+((rate*12)/12))** 12)-1
print ("The EAR is","{:,.2f}".format(EAR*100))

#8
pmt=-1700 
r1=0.13/12 
r2=0.10/12
n1=6*12 
n2=10*12
fv=0
pv2=np.pv(nper=n2,rate=r2,pmt=pmt,fv = fv) #present value for the last 10 years
pv=(pv2)/((1+(r1))**n1)  #discount back pv2 to the present
pv1=np.pv(nper=n1,rate=r1,pmt=pmt,fv=fv) 
print ("Value of cash flows is","{:,.2f}".format(pv1+pv))

#9
pv=-43000
N=60
I=0.0825/12
pmt=np.pmt(rate=I,nper=N,pv=pv,fv=0)
print ("Montly payment should be","{:,.2f}".format(pmt))

#10
pv=5000
point=3
r=0.1
Upfront=pv*((point/100)) 
fv=pv*(1+r)
pv1=pv-Upfront
r1=(fv/pv1)-1
print ("Actual Rate is","{:.2f}%".format(r1* 100))
