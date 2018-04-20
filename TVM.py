
#1 Annual increasing in selling price

avgP07 = 27958
avgP01 = 21308
year = 6
incP = ((avgP07/avgP01)**(1/year)) - 1

print ("The annual increase in selling price: {0:.2f}%".format(incP * 100))

#2 Number of year
from math import exp, log

FerPri = 180000
PreMon = 35000 #Saving Money at t=0
Int = 0.05
NumYear = (log(FerPri)-log(PreMon))/ (log(1+Int))

print ('It will be {:.2f} years before you have enough money to buy the car' .format(NumYear))

#3 Present value of liability

from math import exp, log

mill=1000000
FV = 650*mill 
year= 17 
INT= 0.095 

PV = FV/((1+INT)**(year))

print ('Present Value:', '${:,.2f}'.format(PV))

#4 Present Value of Windfall

mill = 1000000
PrizeVal = 4.5*mill
year = 73
Int = 0.08

PresentVal = PrizeVal/((1+Int)**(year))

print ('The present value of windfall: ${:,.2f}' .format(PresentVal))

#5 Future Value of Coin Collection

PresVal = 55
Int = 0.07
future = 2034
present = 1947
year = future - present

FutureVal = PresVal * ((1+Int)**year)

print ('The future value of Coin Collection: ${:,.2f}' .format(FutureVal))

#6 Percentage increase in Winner Check & Future Value of Winner Prize in 2040

WinPriz01 = 120
WinPriz02 = 1179000
n1 = 1895
n2 = 2007
n3 = 2040

Int = ((WinPriz02/WinPriz01)**(1/(n2-n1))) - 1
WinPriz03 = WinPriz02 * ((1+Int)**(n3-n2))

print ("a) The percentage increase per year in the winner's prize: {:.2f}%" .format(Int*100))
print ("b) The winner prize in 2040: ${:,.2f}" .format(WinPriz03*100))

#7 Annual return rate

Price2003 = 10305500
Price1999 = 12385500
n1=1999
n2 = 2003
year = n2-n1

Return = ((Price2003/Price1999)**(1/year))-1

print ('The annual return rate on the sculpture: {:.2f}%' .format(Return*100))

#8 Future Value

RetireAmt = 2000
Int = 0.1
n = 35
wait = 7

Future01 = RetireAmt*((1+Int)**n)
Future02 = RetireAmt*((1+Int)**(n+wait))

print ('a) There will be ${0:,.2f} in the account when you retire in 35 years' .format(Future01))
print ('b) There will be ${0:,.2f} in the account if waiting 7 years before contributing' .format(Future02))

#9 Future Value

PresVal = 29000
Int = 0.05
now = 2
future = 10
year = future - now

FutureVal = PresVal*((1+Int)**(year))

print ('There will be ${0:,.2f} in the account in 10 years' .format(FutureVal))

#10 Number of Investing Period

from math import exp, log

PresVal = 8000
now = 2
Int = 0.12
FutureVal = 95000

year = (log(FutureVal)-log(PresVal))/log(1+Int)

print ('Waiting {:,.2f} years to get $95000' .format(year +2))