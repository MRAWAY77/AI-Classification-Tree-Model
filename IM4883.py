import nltk
import numpy as np
import os 
import math
import pandas as pd
import csv
from itertools import zip_longest

Survived, Die, temp = ([] for i in range(3))

TCount = 891

df = pd.read_csv('/home/alvinwong/Desktop/train.csv',skipinitialspace=True)

for i, j in zip(df['PassengerId'],df['Survived']):
	if j == 1:
		k = i-1
		Survived.append(df.loc[k])
	if j == 0:
		l = i-1
		Die.append(df.loc[l])

# print(content)
A = pd.DataFrame(Survived)
B = pd.DataFrame(Die)
A.to_csv('/home/alvinwong/Desktop/A.csv')
B.to_csv('/home/alvinwong/Desktop/B.csv')
del Survived[:]
del Die[:]

dfa = pd.read_csv('/home/alvinwong/Desktop/A.csv',skipinitialspace=True)
dfb = pd.read_csv('/home/alvinwong/Desktop/B.csv',skipinitialspace=True)

count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))
count_M,count_F = (0 for i in range(2))
count_S,count_C,count_Q,count_U = (0 for i in range(4))
n0,n1,n2,n3,n4,n5 = (0 for i in range(6))
p0,p1,p2,p3,p4,p5 = (0 for i in range(6))
a0,a1,a2,a3,a4,a5,a6,a7,a8 = (0 for i in range(9))
d0,d1,d2,d3,d4,d5 = (0 for i in range(6))
c0,c1,c2,c3 = (0 for i in range(4))
seatA,seatB,seatC,seatD,seatE,seatF = (0 for i in range(6))

Info_df = (-len(dfa)/TCount * math.log2(len(dfa)/TCount)) - (len(dfb)/TCount * math.log2(len(dfb)/TCount))
print('Info_df = {}'.format(Info_df))

for Pclass in dfa['Pclass']:
	if Pclass == 1:
		count_1+=1
	if Pclass == 2:
		count_2+=1
	if Pclass == 3:
		count_3+=1

print (count_1,count_2,count_3)

Info_Pclass1 = (216/TCount)*(-count_1/216 * math.log2(count_1/216) - (80/216 * math.log2(80/216))) 
Info_Pclass2 = (184/TCount)*(-count_2/184 * math.log2(count_2/184) - (97/184 * math.log2(97/184))) 
Info_Pclass3 = (491/TCount)*(-count_3/491 * math.log2(count_3/491) - (372/491 * math.log2(372/491))) 
Info_Pclass = Info_Pclass1 + Info_Pclass2 + Info_Pclass3

Gain_Pclass = Info_df - Info_Pclass
Split_Pclass = (-216/TCount * math.log2(216/TCount)) - (184/TCount * math.log2(184/TCount)) - (491/TCount * math.log2(491/TCount))
Pclass_ratio = Gain_Pclass/Split_Pclass

print('Info_Pclass = {}, Gain_Pclass = {}, PClass_Ratio = {}'.format(Info_Pclass,Gain_Pclass,Pclass_ratio))
count_1,count_2,count_3 = (0 for i in range(3))

for sex in dfa['Sex']:
	if sex == 'male':
		count_M+=1
	if sex == 'female':
		count_F+=1

print (count_M,count_F)

Info_M = (577/TCount)*(-count_M/577 * math.log2(count_M/577) - (468/577 * math.log2(468/577))) 
Info_F = (314/TCount)*(-count_F/314 * math.log2(count_F/314) - (81/314 * math.log2(81/314))) 

Info_Sex = Info_M + Info_F
Gain_Sex = Info_df - Info_Sex
Split_Sex = (-577/TCount * math.log2(577/TCount)) - (314/TCount * math.log2(314/TCount)) 
Sex_ratio = Gain_Sex/Split_Sex

print ('Info_Sex = {}, Gain_Sex = {}, Sex_Ratio = {}'.format(Info_Sex,Gain_Sex,Sex_ratio))

for location in dfa['Embarked']:
	if location == 'S':
		count_S+=1
	elif location == 'C':
		count_C+=1
	elif location == 'Q':
		count_Q+=1
	else:
		count_U+=1


print (count_S,count_C,count_Q,count_U)

Info_S = (644/TCount)*(-count_S/644 * math.log2(count_S/644) - (427/644 * math.log2(427/644))) 
Info_C = (168/TCount)*(-count_C/168 * math.log2(count_C/168) - (75/168 * math.log2(75/168))) 
Info_Q = (77/TCount)*(-count_Q/77 * math.log2(count_Q/77) - (47/77 * math.log2(47/77))) 
Info_U = 0

Info_Dest = Info_S + Info_C + Info_Q + Info_U
Gain_Dest = Info_df - Info_Dest
Split_Dest = (-644/TCount * math.log2(644/TCount)) - (168/TCount * math.log2(168/TCount)) - (77/TCount * math.log2(77/TCount)) - (2/TCount * math.log2(2/TCount))  
Dest_ratio = Gain_Dest/Split_Dest

print ('Info_Dest= {}, Gain_Dest = {}, Dest_Ratio = {}'.format(Info_Dest,Gain_Dest,Dest_ratio))

for num in dfa['SibSp']:
	if num == 0:
		n0+=1
	elif num == 1:
		n1+=1
	elif num == 2:
		n2+=1
	elif num == 3:
		n3+=1
	elif num == 4:
		n4+=1
	elif num >= 5:
		n5+=1

print (n0,n1,n2,n3,n4,n5)

Info_n0 = (608/TCount)*(-n0/608 * math.log2(n0/608) - (398/608 * math.log2(398/608))) 
Info_n1 = (209/TCount)*(-n1/209 * math.log2(n1/209) - (97/209 * math.log2(97/209))) 
Info_n2 = (28/TCount)*(-n2/28 * math.log2(n2/28) - (15/28 * math.log2(15/28))) 
Info_n3 = (16/TCount)*(-n3/16 * math.log2(n3/16) - (12/16 * math.log2(12/16))) 
Info_n4 = (18/TCount)*(-n4/18 * math.log2(n4/18) - (15/18 * math.log2(15/18))) 
Info_n5 = 0

Info_Sib = Info_n0 + Info_n1 + Info_n2 + Info_n3 + Info_n4 + Info_n5 
Gain_Sib = Info_df - Info_Sib
Split_Sib = (-608/TCount * math.log2(608/TCount)) - (209/TCount * math.log2(209/TCount)) - (28/TCount * math.log2(28/TCount)) - (16/TCount * math.log2(16/TCount)) - (18/TCount * math.log2(18/TCount)) - (12/TCount * math.log2(12/TCount))  
Sib_ratio = Gain_Sib/Split_Sib

print ('Info_Sib= {}, Gain_Sib = {},Split_Sib = {}, Sib_Ratio = {}'.format(Info_Sib,Gain_Sib,Split_Sib, Sib_ratio))

for num in dfa['Parch']:
	if num == 0:
		p0+=1
	elif num == 1:
		p1+=1
	elif num == 2:
		p2+=1
	elif num == 3:
		p3+=1
	elif num == 4:
		p4+=1
	elif num >= 5:
		p5+=1

print (p0,p1,p2,p3,p4,p5)

Info_p0 = (678/TCount)*(-p0/678 * math.log2(p0/678) - (445/678 * math.log2(445/678))) 
Info_p1 = (118/TCount)*(-p1/118 * math.log2(p1/118) - (53/118 * math.log2(53/118))) 
Info_p2 = (80/TCount)*(-p2/80 * math.log2(p2/80) - (40/80 * math.log2(40/80))) 
Info_p3 = (5/TCount)*(-p3/5 * math.log2(p3/5) - (2/5 * math.log2(2/5))) 
Info_p4 = 0
Info_p5 = 0


Info_Par = Info_p0 + Info_p1 + Info_p2 + Info_p3 + Info_n4 + Info_p5 
Gain_Par = Info_df - Info_Par
Split_Par = (-678/TCount * math.log2(678/TCount)) - (118/TCount * math.log2(118/TCount)) - (80/TCount * math.log2(80/TCount)) - (5/TCount * math.log2(5/TCount)) - (4/TCount * math.log2(4/TCount)) - (6/TCount * math.log2(6/TCount))  
Par_ratio = Gain_Par/Split_Par

print ('Info_Par= {}, Gain_Par = {}, Par_ratio = {}'.format(Info_Par,Gain_Par,Par_ratio))

for age in dfb['Age']:
	if age >=0 and age <=10:
		a0+=1
	elif age > 10 and age <=20:
		a1+=1
	elif age > 20 and age <=30:
		a2+=1
	elif age > 30 and age <=40:
		a3+=1
	elif age > 40 and age <=50:
		a4+=1
	elif age > 50 and age <=60:
		a5+=1
	elif age > 60 and age <=70:
		a6+=1
	elif age > 70 and age <=80:
		a7+=1
	else:
		a8+=1

print (a0,a1,a2,a3,a4,a5,a6,a7,a8)


Info_a0 = (64/TCount)*(-a0/64 * math.log2(a0/64) - (26/64 * math.log2(26/64))) 
Info_a1 = (115/TCount)*(-a1/115 * math.log2(a1/115) - (71/115 * math.log2(71/115))) 
Info_a2 = (230/TCount)*(-a2/230 * math.log2(a2/230) - (146/230 * math.log2(146/230))) 
Info_a3 = (155/TCount)*(-a3/155 * math.log2(a3/155) - (86/155 * math.log2(86/155))) 
Info_a4 = (86/TCount)*(-a4/86 * math.log2(a4/86) - (53/86 * math.log2(53/86))) 
Info_a5 = (42/TCount)*(-a5/42 * math.log2(a5/42) - (25/42 * math.log2(25/42))) 
Info_a6 = (17/TCount)*(-a6/17 * math.log2(a6/17) - (13/17 * math.log2(13/17))) 
Info_a7 = (5/TCount)*(-a7/5 * math.log2(a7/5) - (4/5 * math.log2(4/5))) 
Info_a8 = (177/TCount)*(-a8/177 * math.log2(a8/177) - (125/177 * math.log2(125/177))) 

Info_age = Info_a0 + Info_a1 + Info_a2 + Info_a3 + Info_a4 + Info_a5 +Info_a6 + Info_a7 + Info_a8 
Gain_age = Info_df - Info_age
Split_age = (-64/TCount * math.log2(64/TCount)) - (115/TCount * math.log2(115/TCount)) - (230/TCount * math.log2(230/TCount)) - (155/TCount * math.log2(155/TCount)) - (86/TCount * math.log2(86/TCount)) - (42/TCount * math.log2(42/TCount))  - (17/TCount * math.log2(17/TCount))  - (5/TCount * math.log2(5/TCount))   - (177/TCount * math.log2(177/TCount)) 
Age_ratio = Gain_age/Split_age


print ('Info_age= {}, Gain_age = {}, Age_ratio = {}'.format(Info_age,Gain_age,Age_ratio))
a0,a1,a2,a3,a4,a5,a6,a7,a8 = (0 for i in range(9))

for digit in dfb['Ticket']:
	if digit.isdigit():
		if int(digit) >=0 and int(digit) <1000:
			d0+=1
		elif int(digit) >= 1000 and int(digit) <10000:
			d1+=1
		elif int(digit) >= 10000 and int(digit) <100000:
			d2+=1
		elif int(digit) >= 100000 and int(digit) <1000000:
			d3+=1
		elif int(digit) >= 1000000 and int(digit) <10000000:
			d4+=1
	else:
		d5+=1
		temp.append(digit)

print (d0,d1,d2,d3,d4,d5)
del temp[:]
# print(temp)


Info_d0 = 0
Info_d1 = (97/TCount)*(-d1/97 * math.log2(d1/97) - (61/97 * math.log2(61/97))) 
Info_d2 = (131/TCount)*(-d2/131 * math.log2(d2/131) - (50/131 * math.log2(50/131))) 
Info_d3 = (415/TCount)*(-d3/415 * math.log2(d3/415) - (282/415 * math.log2(282/415))) 
Info_d4 = (16/TCount)*(-d4/16 * math.log2(d4/16) - (12/16 * math.log2(12/16))) 
Info_d5 = (230/TCount)*(-d5/230 * math.log2(d5/230) - (142/230 * math.log2(142/230))) 

Info_Tkt = Info_d0 + Info_d1 + Info_d2 + Info_d3 + Info_d4 + Info_d5 
Gain_Tkt = Info_df - Info_Tkt
Split_tkt = (-2/TCount * math.log2(2/TCount)) - (97/TCount * math.log2(97/TCount)) - (131/TCount * math.log2(131/TCount)) - (415/TCount * math.log2(415/TCount)) - (16/TCount * math.log2(16/TCount)) - (230/TCount * math.log2(230/TCount))
Tkt_ratio = Gain_Tkt/Split_tkt


print ('Info_Ticket= {}, Gain_Ticket = {}, Tkt_ratio = {}'.format(Info_Tkt,Gain_Tkt,Tkt_ratio))

for cash in dfb['Fare']:
	if cash >=0 and cash <10:
		c0+=1
	elif cash >= 10 and cash<100:
		c1+=1
	elif cash >= 100 and cash <=1000:
		c2+=1

print (c0,c1,c2)

Info_c0 = (336/TCount)*(-c1/336 * math.log2(c1/336) - (269/336 * math.log2(269/336))) 
Info_c1 = (502/TCount)*(-c1/502 * math.log2(c1/502) - (266/502 * math.log2(266/502))) 
Info_c2 = (53/TCount)*(-c2/52 * math.log2(c2/53) - (14/53 * math.log2(14/53))) 

Info_Fare = Info_c0 + Info_c1 + Info_c2 
Gain_Fare = Info_df - Info_Fare
Split_fare = (-336/TCount * math.log2(336/TCount)) - (502/TCount * math.log2(502/TCount)) - (53/TCount * math.log2(53/TCount)) 
Fare_ratio = Gain_Fare/Split_fare

print ('Info_Fare= {}, Gain_Fare = {}, Fare_ratio = {}'.format(Info_Fare,Gain_Fare, Fare_ratio))

for cabin in dfa['Cabin']:
	if type(cabin) == float:
		seatA+=1
	elif type(cabin) == str:
		seatB+=1

print (seatA,seatB)

Info_CA = (687/TCount)*(-seatA/687 * math.log2(seatA/687) - (136/687 * math.log2(136/687))) 
Info_CB = (204/TCount)*(-seatB/502042 * math.log2(seatB/204) - (68/204 * math.log2(68/204))) 

Info_Cabin = Info_CA + Info_CB 
Gain_Cabin = Info_df - Info_Cabin
Split_Cabin = (-687/TCount * math.log2(687/TCount)) - (204/TCount * math.log2(204/TCount))
Cabin_ratio = Gain_Cabin/Split_Cabin

print ('Info_Cabin= {}, Gain_Cabin = {}, Cabin_Ratio = {}'.format(Info_Cabin,Gain_Cabin,Cabin_ratio))


################################## 1ST SPLIT: GENDER ############################################
for i, j in zip(dfa['PassengerId'],dfa['Sex']):
	if j == 'male':
		k = i-1
		Survived.append(df.loc[k])
	if j == 'female':
		l = i-1
		Die.append(df.loc[l])

SM = pd.DataFrame(Survived)
SF = pd.DataFrame(Die)
SM.to_csv('/home/alvinwong/Desktop/SM.csv')
SF.to_csv('/home/alvinwong/Desktop/SF.csv')
del Survived[:]
del Die[:]

for i, j in zip(dfb['PassengerId'],dfb['Sex']):
	if j == 'male':
		k = i-1
		Survived.append(df.loc[k])
	if j == 'female':
		l = i-1
		Die.append(df.loc[l])

DM = pd.DataFrame(Survived)
DF = pd.DataFrame(Die)
DM.to_csv('/home/alvinwong/Desktop/DM.csv')
DF.to_csv('/home/alvinwong/Desktop/DF.csv')
del Survived[:]
del Die[:]

dfsm = pd.read_csv('/home/alvinwong/Desktop/SM.csv',skipinitialspace=True)
dfsf = pd.read_csv('/home/alvinwong/Desktop/SF.csv',skipinitialspace=True)

temp1,temp2,temp3 = ([] for i in range(3))

for i, j in zip(dfsm['PassengerId'],dfsm['Age']):
	if j == 1:
		k = i-1
		temp1.append(dfsm.loc[k])
	if j == 2:
		l = i-1
		temp2.append(dfsm.loc[l])
	if j == 3:
		m = i-1
		temp3.append(dfsm.loc[m])

Pclass1 = pd.DataFrame(temp1)
Pclass2 = pd.DataFrame(temp2)
Pclass3 = pd.DataFrame(temp3)
Pclass1.to_csv('/home/alvinwong/Desktop/Pclass1.csv')
Pclass2.to_csv('/home/alvinwong/Desktop/Pclass2.csv')
Pclass3.to_csv('/home/alvinwong/Desktop/Pclass3.csv')
del temp1[:]
del temp2[:]
del temp3[:]