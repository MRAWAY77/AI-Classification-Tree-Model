import numpy as np
import os 
import math
import pandas as pd
import csv
from itertools import zip_longest

def Pclass(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

	for output, Pclass in zip(temp1,temp2):
		if output == 1 and Pclass == 1:
			count_1+=1
		elif output == 1 and Pclass == 2:
			count_2+=1
		elif output == 1 and Pclass == 3:
			count_3+=1
		elif output == 0 and Pclass == 1:
			count_4+=1
		elif output == 0 and Pclass == 2:
			count_5+=1
		elif output == 0 and Pclass == 3:
			count_6+=1

	print (count_1,count_2,count_3,count_4,count_5,count_6)

	if count_1 == 0 or count_4 == 0:
		Info_Pclass1 = 0
		Split_Pclass1 = 0

	else:
		Info_Pclass1 = ((count_1+count_4)/TCount)*(-count_1/(count_1+count_4) * math.log2(count_1/(count_1+count_4)) - (count_4/(count_1+count_4) * math.log2(count_4/(count_1+count_4)))) 
		Split_Pclass1 = (-(count_1+count_4)/TCount * math.log2((count_1+count_4)/TCount))
		
	if count_2 == 0 or count_5 == 0:
		Info_Pclass2 = 0
		Split_Pclass2 = 0

	else:
		Info_Pclass2 = ((count_2+count_5)/TCount)*(-count_2/(count_2+count_5) * math.log2(count_2/(count_2+count_5)) - (count_5/(count_2+count_5) * math.log2(count_5/(count_2+count_5)))) 
		Split_Pclass2 = (-(count_2+count_5)/TCount * math.log2((count_2+count_5)/TCount))

	if count_3 == 0 or count_6 == 0:
		Info_Pclass3 = 0
		Split_Pclass3 = 0

	else:
		Info_Pclass3 = ((count_3+count_6)/TCount)*(-count_3/(count_3+count_6) * math.log2(count_3/(count_3+count_6)) - (count_6/(count_3+count_6) * math.log2(count_6/(count_3+count_6)))) 
		Split_Pclass3 = (-(count_3+count_6)/TCount * math.log2((count_3+count_6)/TCount))

	Info_Pclass = Info_Pclass1 + Info_Pclass2 + Info_Pclass3
	Gain_Pclass = Info_df - Info_Pclass
	Split_Pclass = Split_Pclass1 + Split_Pclass2 + Split_Pclass3
	
	try:
		Pclass_ratio = Gain_Pclass/Split_Pclass 
	except ZeroDivisionError:
		Pclass_ratio = 0

	print('Info_Pclass = {}, Gain_Pclass = {}, PClass_Ratio = {}'.format(Info_Pclass,Gain_Pclass,Pclass_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

def Sex(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

	for output, gender in zip(temp1,temp2):
		if output == 1 and gender == 'male':
			count_1+=1
		elif output == 1 and gender == 'female':
			count_2+=1
		elif output == 0 and gender == 'male':
			count_3+=1
		elif output == 0 and gender == 'female':
			count_4+=1

	print (count_1,count_2,count_3,count_4)

	if count_1 == 0 or count_3 == 0:
		Info_male = 0
		Split_male = 0

	else:
		Info_male = ((count_1+count_3)/TCount)*(-count_1/(count_1+count_3) * math.log2(count_1/(count_1+count_3)) - (count_3/(count_1+count_3) * math.log2(count_3/(count_1+count_3)))) 
		Split_male = (-(count_1+count_3)/TCount * math.log2((count_1+count_3)/TCount))

	if count_2 == 0 or count_4 == 0:
		Info_female = 0
		Split_female = 0

	else:
		Info_female = ((count_2+count_4)/TCount)*(-count_2/(count_2+count_4) * math.log2(count_2/(count_2+count_4)) - (count_4/(count_2+count_4) * math.log2(count_4/(count_2+count_4)))) 
		Split_female = (-(count_2+count_4)/TCount * math.log2((count_2+count_4)/TCount))

	Info_Sex = Info_male + Info_female
	Gain_Sex = Info_df - Info_Sex
	Split_Sex =  Split_male + Split_female  
	
	try:
		Sex_ratio = Gain_Sex/Split_Sex 
	except ZeroDivisionError:
		Sex_ratio = 0

	print ('Info_Sex = {}, Gain_Sex = {}, Sex_Ratio = {}'.format(Info_Sex,Gain_Sex,Sex_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

def location(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8 = (0 for i in range(8))

	for output, dest in zip(temp1,temp2):
		if output == 1 and dest == 'S':
			count_1+=1
		elif output == 1 and dest == 'C':
			count_2+=1
		elif output == 1 and dest == 'Q':
			count_3+=1
		elif output == 1 and type(dest) == float:
			count_4+=1
		elif output == 0 and dest == 'S':
			count_5+=1
		elif output == 0 and dest == 'C':
			count_6+=1
		elif output == 0 and dest == 'Q':
			count_7+=1
		elif output == 0 and type(dest) == float:
			count_8+=1

	print (count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8)

	if count_1 == 0 or count_5 == 0:
		Info_S = 0
		Split_S = 0

	else:
		Info_S = ((count_1+count_5)/TCount)*(-count_1/(count_1+count_5) * math.log2(count_1/(count_1+count_5)) - (count_5/(count_1+count_5) * math.log2(count_5/(count_1+count_5)))) 
		Split_S = (-(count_1+count_5)/TCount * math.log2((count_1+count_5)/TCount))

	if count_2 == 0 or count_6 == 0:
		Info_C = 0
		Split_C =0

	else:
		Info_C = ((count_2+count_6)/TCount)*(-count_2/(count_2+count_6) * math.log2(count_2/(count_2+count_6)) - (count_6/(count_2+count_6) * math.log2(count_6/(count_2+count_6)))) 
		Split_C = (-(count_2+count_6)/TCount * math.log2((count_2+count_6)/TCount))

	if count_3 == 0 or count_7 == 0:
		Info_Q = 0
		Split_Q = 0

	else:
		Info_Q = ((count_3+count_7)/TCount)*(-count_3/(count_3+count_7) * math.log2(count_3/(count_3+count_7)) - (count_7/(count_3+count_7) * math.log2(count_7/(count_3+count_7))))
		Split_Q = (-(count_3+count_7)/TCount * math.log2((count_3+count_7)/TCount)) 
	
	if count_4 == 0 or count_8 == 0:
		Info_U = 0
		Split_U = 0

	else:
		Info_U = ((count_4+count_8)/TCount)*(-count_4/(count_4+count_8) * math.log2(count_4/(count_4+count_8)) - (count_8/(count_3+count_8) * math.log2(count_8/(count_3+count_8))))  
		Split_U = (-(count_4+count_8)/TCount * math.log2((count_4+count_8)/TCount))
	
	Info_dest = Info_S + Info_C + Info_Q + Info_U
	Gain_dest = Info_df - Info_dest
	Split_dest =  Split_S + Split_C + Split_Q + Split_U
	
	try:
		dest_ratio = Gain_dest/Split_dest 
	except ZeroDivisionError:
		dest_ratio = 0

	print('Info_dest = {}, Gain_dest = {}, Dest_ratio = {}'.format(Info_dest,Gain_dest,dest_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8 = (0 for i in range(8))

def Parch(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

	for output, parch in zip(temp1,temp2):
		if output == 1  and  parch == 0:
			count_1+=1
		elif output == 1 and parch == 1:
			count_2+=1
		elif output == 1 and parch == 2:
			count_3+=1
		elif output == 1 and parch == 3:
			count_4+=1
		elif output == 1 and parch == 4:
			count_5+=1
		elif output == 1 and parch >= 5:
			count_6+=1
		elif output == 0 and parch == 0:
			count_7+=1
		elif output == 0 and parch == 1:
			count_8+=1
		elif output == 0 and parch == 2:
			count_9+=1
		elif output == 0 and parch == 3:
			count_10+=1
		elif output == 0 and parch == 4:
			count_11+=1
		elif output == 0 and parch >= 5:
			count_12+=1
	print (count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12)
	
	if count_1 == 0 or count_7 == 0:
		Info_0 = 0
		Split_0 = 0

	else:
		Info_0 = ((count_1+count_7)/TCount)*(-count_1/(count_1+count_7) * math.log2(count_1/(count_1+count_7)) - (count_7/(count_1+count_7) * math.log2(count_7/(count_1+count_7)))) 
		Split_0 = (-(count_1+count_7)/TCount * math.log2((count_1+count_7)/TCount))

	if count_2 == 0 or count_8 == 0:
		Info_1 = 0
		Split_1 =0

	else:
		Info_1 = ((count_2+count_8)/TCount)*(-count_2/(count_2+count_8) * math.log2(count_2/(count_2+count_8)) - (count_8/(count_2+count_8) * math.log2(count_8/(count_2+count_8)))) 
		Split_1 = (-(count_2+count_8)/TCount * math.log2((count_2+count_8)/TCount))

	if count_3 == 0 or count_9 == 0:
		Info_2 = 0
		Split_2 = 0

	else:
		Info_2 = ((count_3+count_9)/TCount)*(-count_3/(count_3+count_9) * math.log2(count_3/(count_3+count_9)) - (count_9/(count_3+count_9) * math.log2(count_9/(count_3+count_9))))
		Split_2 = (-(count_3+count_9)/TCount * math.log2((count_3+count_9)/TCount))
	
	if count_4 == 0 or count_10 == 0:
		Info_3 = 0
		Split_3 = 0

	else:
		Info_3 = ((count_4+count_10)/TCount)*(-count_4/(count_4+count_10) * math.log2(count_4/(count_4+count_10)) - (count_10/(count_4+count_10) * math.log2(count_10/(count_4+count_10)))) 
		Split_3 = (-(count_4+count_10)/TCount * math.log2((count_4+count_10)/TCount))
	
	if count_5 == 0 or count_11 == 0:
		Info_4 = 0
		Split_4 = 0

	else:
		Info_4 = ((count_5+count_11)/TCount)*(-count_5/(count_5+count_11) * math.log2(count_5/(count_5+count_11)) - (count_11/(count_5+count_11) * math.log2(count_11/(count_5+count_11)))) 
		Split_4 =(-(count_5+count_11)/TCount * math.log2((count_5+count_11)/TCount))
	
	if count_6 == 0 or count_12 == 0:
		Info_5 = 0
		Split_5 = 0

	else:
		Info_5 = ((count_6+count_12)/TCount)*(-count_6/(count_6+count_12) * math.log2(count_6/(count_6+count_12)) - (count_12/(count_6+count_12) * math.log2(count_12/(count_6+count_12)))) 
		Split_5 =(-(count_6+count_12)/TCount * math.log2((count_6+count_12)/TCount))


	Info_parch = Info_0 + Info_1 + Info_2 + Info_3 + Info_4 + Info_5
	Gain_parch = Info_df - Info_parch
	Split_parch =  Split_0 + Split_1 + Split_2 + Split_3 + Split_4 + Split_5 
	
	try:
		parch_ratio = Gain_parch/Split_parch 
	except ZeroDivisionError:
		parch_ratio = 0

	print('Info_parch = {}, Gain_parch = {}, Parch_ratio = {}'.format(Info_parch,Gain_parch,parch_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

def SibSp(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

	for output, sibsp in zip(temp1,temp2):
		if output == 1  and  sibsp == 0:
			count_1+=1
		elif output == 1 and sibsp == 1:
			count_2+=1
		elif output == 1 and sibsp == 2:
			count_3+=1
		elif output == 1 and sibsp == 3:
			count_4+=1
		elif output == 1 and sibsp == 4:
			count_5+=1
		elif output == 1 and sibsp >= 5:
			count_6+=1
		elif output == 0 and sibsp == 0:
			count_7+=1
		elif output == 0 and sibsp == 1:
			count_8+=1
		elif output == 0 and sibsp == 2:
			count_9+=1
		elif output == 0 and sibsp == 3:
			count_10+=1
		elif output == 0 and sibsp == 4:
			count_11+=1
		elif output == 0 and sibsp >= 5:
			count_12+=1
	print (count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12)
	
	if count_1 == 0 or count_7 == 0:
		Info_0 = 0
		Split_0 = 0

	else:
		Info_0 = ((count_1+count_7)/TCount)*(-count_1/(count_1+count_7) * math.log2(count_1/(count_1+count_7)) - (count_7/(count_1+count_7) * math.log2(count_7/(count_1+count_7)))) 
		Split_0 = (-(count_1+count_7)/TCount * math.log2((count_1+count_7)/TCount))

	if count_2 == 0 or count_8 == 0:
		Info_1 = 0
		Split_1 =0

	else:
		Info_1 = ((count_2+count_8)/TCount)*(-count_2/(count_2+count_8) * math.log2(count_2/(count_2+count_8)) - (count_8/(count_2+count_8) * math.log2(count_8/(count_2+count_8)))) 
		Split_1 = (-(count_2+count_8)/TCount * math.log2((count_2+count_8)/TCount))

	if count_3 == 0 or count_9 == 0:
		Info_2 = 0
		Split_2 = 0

	else:
		Info_2 = ((count_3+count_9)/TCount)*(-count_3/(count_3+count_9) * math.log2(count_3/(count_3+count_9)) - (count_9/(count_3+count_9) * math.log2(count_9/(count_3+count_9))))
		Split_2 = (-(count_3+count_9)/TCount * math.log2((count_3+count_9)/TCount))
	
	if count_4 == 0 or count_10 == 0:
		Info_3 = 0
		Split_3 = 0

	else:
		Info_3 = ((count_4+count_10)/TCount)*(-count_4/(count_4+count_10) * math.log2(count_4/(count_4+count_10)) - (count_10/(count_4+count_10) * math.log2(count_10/(count_4+count_10)))) 
		Split_3 = (-(count_4+count_10)/TCount * math.log2((count_4+count_10)/TCount))
	
	if count_5 == 0 or count_11 == 0:
		Info_4 = 0
		Split_4 = 0

	else:
		Info_4 = ((count_5+count_11)/TCount)*(-count_5/(count_5+count_11) * math.log2(count_5/(count_5+count_11)) - (count_11/(count_5+count_11) * math.log2(count_11/(count_5+count_11)))) 
		Split_4 =(-(count_5+count_11)/TCount * math.log2((count_5+count_11)/TCount))
	
	if count_6 == 0 or count_12 == 0:
		Info_5 = 0
		Split_5 = 0

	else:
		Info_5 = ((count_6+count_12)/TCount)*(-count_6/(count_6+count_12) * math.log2(count_6/(count_6+count_12)) - (count_12/(count_6+count_12) * math.log2(count_12/(count_6+count_12)))) 
		Split_5 =(-(count_6+count_12)/TCount * math.log2((count_6+count_12)/TCount))


	Info_sibsp = Info_0 + Info_1 + Info_2 + Info_3 + Info_4 + Info_5
	Gain_sibsp = Info_df - Info_sibsp
	Split_sibsp =  Split_0 + Split_1 + Split_2 + Split_3 + Split_4 + Split_5 
	
	try:
		sibsp_ratio = Gain_sibsp/Split_sibsp 
	except ZeroDivisionError:
		sibsp_ratio = 0

	print('Info_sibsp = {}, Gain_sibsp = {}, Sibsp_ratio = {}'.format(Info_sibsp,Gain_sibsp,sibsp_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

def Age(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10 = (0 for i in range(10))

	for output, age in zip(temp1,temp2):
		if output == 1  and  (age >=0 and age <=20):
			count_1+=1
		elif output == 1 and (age > 20 and age <=40):
			count_2+=1
		elif output == 1 and (age > 40 and age <=60):
			count_3+=1
		elif output == 1 and (age > 60 and age <=80):
			count_4+=1
		elif output == 1 and type(age) == float:
			count_5+=1
		elif output == 0 and (age >=0 and age <=20):
			count_6+=1
		elif output == 0 and (age > 20 and age <=40):
			count_7+=1
		elif output == 0 and (age > 40 and age <=60):
			count_8+=1
		elif output == 0 and (age > 60 and age <=80):
			count_9+=1
		elif output == 0 and type(age) == float:
			count_10+=1
	
	print (count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10)
	
	if count_1 == 0 or count_6 == 0:
		Info_0 = 0
		Split_0 = 0

	else:
		Info_0 = ((count_1+count_6)/TCount)*(-count_1/(count_1+count_6) * math.log2(count_1/(count_1+count_6)) - (count_6/(count_1+count_6) * math.log2(count_6/(count_1+count_6)))) 
		Split_0 = (-(count_1+count_6)/TCount * math.log2((count_1+count_6)/TCount))

	if count_2 == 0 or count_7 == 0:
		Info_1 = 0
		Split_1 =0

	else:
		Info_1 = ((count_2+count_7)/TCount)*(-count_2/(count_2+count_7) * math.log2(count_2/(count_2+count_7)) - (count_7/(count_2+count_7) * math.log2(count_7/(count_2+count_7)))) 
		Split_1 = (-(count_2+count_7)/TCount * math.log2((count_2+count_7)/TCount))

	if count_3 == 0 or count_9 == 0:
		Info_2 = 0
		Split_2 = 0

	else:
		Info_2 = ((count_3+count_8)/TCount)*(-count_3/(count_3+count_8) * math.log2(count_3/(count_3+count_8)) - (count_8/(count_3+count_8) * math.log2(count_8/(count_3+count_8))))
		Split_2 = (-(count_3+count_8)/TCount * math.log2((count_3+count_8)/TCount))
	
	if count_4 == 0 or count_9 == 0:
		Info_3 = 0
		Split_3 = 0

	else:
		Info_3 = ((count_4+count_9)/TCount)*(-count_4/(count_4+count_9) * math.log2(count_4/(count_4+count_9)) - (count_9/(count_4+count_9) * math.log2(count_9/(count_4+count_9)))) 
		Split_3 = (-(count_4+count_9)/TCount * math.log2((count_4+count_9)/TCount))
	
	if count_5 == 0 or count_10 == 0:
		Info_4 = 0
		Split_4 = 0

	else:
		Info_4 = ((count_5+count_10)/TCount)*(-count_5/(count_5+count_10) * math.log2(count_5/(count_5+count_10)) - (count_10/(count_5+count_10) * math.log2(count_10/(count_5+count_10)))) 
		Split_4 =(-(count_5+count_10)/TCount * math.log2((count_5+count_10)/TCount))
	
	Info_age = Info_0 + Info_1 + Info_2 + Info_3 + Info_4 
	Gain_age = Info_df - Info_age
	Split_age =  Split_0 + Split_1 + Split_2 + Split_3 + Split_4 
	
	try:
		age_ratio = Gain_age/Split_age 
	except ZeroDivisionError:
		age_ratio = 0

	print('Info_age = {}, Gain_age = {}, Age_ratio = {}'.format(Info_age,Gain_age,age_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10 = (0 for i in range(10))

def Ticket(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

	for output, Ticket in zip(temp1,temp2):

		if output == 1  and type(Ticket) == int:
			count_1+=1
		elif output == 1  and Ticket.isdigit():
			count_2+=1	
		elif output == 1 and (Ticket.isdigit() == False):
			count_3+=1
		elif output == 0 and type(Ticket) == int:
			count_4+=1
		elif output == 0 and Ticket.isdigit():
			count_5+=1
		elif output == 0 and (Ticket.isdigit() == False):
			count_6+=1
	
	print (count_1,count_2,count_3,count_4,count_5,count_6)
	
	if count_1 == 0 or count_4 == 0:
		Info_0 = 0
		Split_0 = 0

	else:
		Info_0 = ((count_1+count_4)/TCount)*(-count_1/(count_1+count_4) * math.log2(count_1/(count_1+count_4)) - (count_4/(count_1+count_4) * math.log2(count_4/(count_1+count_4)))) 
		Split_0 = (-(count_1+count_4)/TCount * math.log2((count_1+count_4)/TCount))

	if count_2 == 0 or count_5 == 0:
		Info_1 = 0
		Split_1 = 0

	else:
		Info_1 = ((count_2+count_5)/TCount)*(-count_2/(count_2+count_5) * math.log2(count_2/(count_2+count_5)) - (count_5/(count_2+count_5) * math.log2(count_5/(count_2+count_5)))) 
		Split_1 = (-(count_2+count_5)/TCount * math.log2((count_2+count_5)/TCount))

	if count_3 == 0 or count_6 == 0:
		Info_2 = 0
		Split_2 = 0

	else:
		Info_2 = ((count_3+count_6)/TCount)*(-count_3/(count_3+count_6) * math.log2(count_3/(count_3+count_6)) - (count_6/(count_3+count_6) * math.log2(count_6/(count_3+count_6)))) 
		Split_2 = (-(count_3+count_6)/TCount * math.log2((count_3+count_6)/TCount))


	Info_Ticket = Info_0 + Info_1 + Info_2 
	Gain_Ticket = Info_df - Info_Ticket
	Split_Ticket =  Split_0 + Split_1 + Split_2 
	
	try:
		Ticket_ratio = Gain_Ticket/Split_Ticket 
	except ZeroDivisionError:
		Ticket_ratio = 0

	print('Info_Ticket = {}, Gain_Ticket = {}, Ticket_ratio = {}'.format(Info_Ticket,Gain_Ticket,Ticket_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))

def Fare(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

	for output, cash in zip(temp1,temp2):
		if output == 1 and (cash >=0 and cash <10):
			count_1+=1
		elif output == 1 and (cash >= 10 and cash<100):
			count_2+=1
		elif output == 1 and (cash >= 100 and cash <=1000):
			count_3+=1
		elif output == 0 and (cash >=0 and cash <10):
			count_4+=1
		elif output == 0 and (cash >= 10 and cash<100):
			count_5+=1
		elif output == 0 and (cash >= 100 and cash <=1000):
			count_6+=1

	print (count_1,count_2,count_3,count_4,count_5,count_6)

	if count_1 == 0 or count_4 == 0:
		Info_cash1 = 0
		Split_cash1 = 0

	else:
		Info_cash1 = ((count_1+count_4)/TCount)*(-count_1/(count_1+count_4) * math.log2(count_1/(count_1+count_4)) - (count_4/(count_1+count_4) * math.log2(count_4/(count_1+count_4)))) 
		Split_cash1 = (-(count_1+count_4)/TCount * math.log2((count_1+count_4)/TCount))
		
	if count_2 == 0 or count_5 == 0:
		Info_cash2 = 0
		Split_cash2 = 0

	else:
		Info_cash2 = ((count_2+count_5)/TCount)*(-count_2/(count_2+count_5) * math.log2(count_2/(count_2+count_5)) - (count_5/(count_2+count_5) * math.log2(count_5/(count_2+count_5)))) 
		Split_cash2 = (-(count_2+count_5)/TCount * math.log2((count_2+count_5)/TCount))

	if count_3 == 0 or count_6 == 0:
		Info_cash3 = 0
		Split_cash3 = 0

	else:
		Info_cash3 = ((count_3+count_6)/TCount)*(-count_3/(count_3+count_6) * math.log2(count_3/(count_3+count_6)) - (count_6/(count_3+count_6) * math.log2(count_6/(count_3+count_6)))) 
		Split_cash3 = (-(count_3+count_6)/TCount * math.log2((count_3+count_6)/TCount))

	Info_cash = Info_cash1 + Info_cash2 + Info_cash3
	Gain_cash = Info_df - Info_cash
	Split_cash = Split_cash1 + Split_cash2 + Split_cash3
	
	try:
		cash_ratio = Gain_cash/Split_cash 
	except ZeroDivisionError:
		cash_ratio = 0

	print('Info_Fare = {}, Gain_Fare = {}, Fare_Ratio = {}'.format(Info_cash,Gain_cash,cash_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

def Cabin(temp1,temp2,TCount,Info_df):
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

	for output, seat in zip(temp1,temp2):
		if output == 1 and (type(seat) == float):
			count_1+=1
		elif output == 1 and (type(seat) == str):
			count_2+=1
		elif output == 0 and (type(seat) == float):
			count_3+=1
		elif output == 0 and (type(seat) == str):
			count_4+=1

	print (count_1,count_2,count_3,count_4)

	if count_1 == 0 or count_3 == 0:
		Info_nan = 0
		Split_nan = 0

	else:
		Info_nan = ((count_1+count_3)/TCount)*(-count_1/(count_1+count_3) * math.log2(count_1/(count_1+count_3)) - (count_3/(count_1+count_3) * math.log2(count_3/(count_1+count_3)))) 
		Split_nan = (-(count_1+count_3)/TCount * math.log2((count_1+count_3)/TCount))

	if count_2 == 0 or count_4 == 0:
		Info_str = 0
		Split_str = 0

	else:
		Info_str = ((count_2+count_4)/TCount)*(-count_2/(count_2+count_4) * math.log2(count_2/(count_2+count_4)) - (count_4/(count_2+count_4) * math.log2(count_4/(count_2+count_4)))) 
		Split_str = (-(count_2+count_4)/TCount * math.log2((count_2+count_4)/TCount))

	Info_cabin = Info_nan + Info_str
	Gain_cabin = Info_df - Info_cabin
	Split_cabin =  Split_nan + Split_str  
	
	try:
		Cabin_ratio = Gain_Split_cabin 
	except ZeroDivisionError:
		Cabin_ratio = 0

	print ('Info_cabin = {}, Gain_cabin = {}, Cabin_Ratio = {}'.format(Info_cabin,Gain_cabin,Cabin_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))

def info_division(inputs,name):
	Survive, Die = (0 for i in range(2))
	for index in inputs:
		if index == 1:
			Survive+=1
		elif index == 0:
			Die+=1

	if Survive == 0 and Die != 0:
		Info_df = 1
		print('Everyone Died with all variable in {} = 0.'.format(name))
		exit()

	elif Die == 0 and Survive != 0:
		Info_df = 1
		print('Everyone Survive with all variable in {} = 1.'.format(name))
		exit()
		
	elif Survive != 0 and Die != 0:
		Info_df = (-Survive/len(inputs) * math.log2(Survive/len(inputs))) - (Die/len(inputs) * math.log2(Die/len(inputs)))
	
	Survive, Die = (0 for i in range(2))
	return Info_df

def call(data,name):
	Info_data = info_division(data['Survived'],name)
	print('\n')
	print(Info_data)

	Pclass(data['Survived'],data['Pclass'],len(data),Info_data)
	Sex(data['Survived'],data['Sex'],len(data),Info_data)
	location(data['Survived'],data['Embarked'],len(data),Info_data)
	Parch(data['Survived'],data['Parch'],len(data),Info_data)
	SibSp(data['Survived'],data['SibSp'],len(data),Info_data)
	Age(data['Survived'],data['Age'],len(data),Info_data)
	Ticket(data['Survived'],data['Ticket'],len(data),Info_data)
	Fare(data['Survived'],data['Fare'],len(data),Info_data)
	Cabin(data['Survived'],data['Cabin'],len(data),Info_data)

def gender(data,filepath):
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))

	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Pclass']):
		if j == 1:
			k = i-1
			temp1.append(data.loc[k])
		elif j == 2:
			l = i-1
			temp2.append(data.loc[l])
		elif j == 3:
			m = i-1
			temp3.append(data.loc[m])

	Pclass1 = pd.DataFrame(temp1)
	Pclass2 = pd.DataFrame(temp2)
	Pclass3 = pd.DataFrame(temp3)

	if filepath == 'Male':
		Pclass1.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Pclass1.csv', index = False)
		Pclass2.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Pclass2.csv', index = False)
		Pclass3.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Pclass3.csv', index = False)
	elif filepath == 'Female':
		Pclass1.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Pclass1.csv', index = False)
		Pclass2.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Pclass2.csv', index = False)
		Pclass3.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Pclass3.csv', index = False)

	del temp1[:]
	del temp2[:]
	del temp3[:]

def PClass(data,filepath):
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))
	Gender = ['Male','Female']
	Class = ['Pclass1','Pclass2','Pclass3']
	Price = ['Low_Fare','Middle_Fare','High_Fare']

	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Fare']):
		if j >=0 and j <10:
			k = i-1
			temp1.append(data.loc[k])
		elif j >=10 and j <100:
			l = i-1
			temp2.append(data.loc[l])
		elif j >=100 and j <1000:
			m = i-1
			temp3.append(data.loc[m])
		
	Low_Fare = pd.DataFrame(temp1)
	Middle_Fare = pd.DataFrame(temp2)
	High_Fare = pd.DataFrame(temp3)

	# for i in Gender:
	# 	for j in Class:
	# 		for k in Price:
	# 			Low_Fare.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}.csv'.format(i,j,k,k), index = False)
	# 			Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}.csv'.format(i,j,k,k), index = False)
	# 			High_Fare.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}.csv'.format(i,j,k,k), index = False)
	
	if filepath == 'MPclass1':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/High_Fare.csv', index = False)
	elif filepath == 'MPclass2':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/High_Fare/High_Fare.csv', index = False)
	elif filepath == 'MPclass3':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/High_Fare/High_Fare.csv', index = False)
	elif filepath == 'FPclass1':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/High_Fare.csv', index = False)
	elif filepath == 'FPclass2':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/High_Fare/High_Fare.csv', index = False)
	elif filepath == 'FPclass3':
		Low_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Low_Fare.csv', index = False)
		Middle_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Middle_Fare.csv', index = False)
		High_Fare.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/High_Fare/High_Fare.csv', index = False)
	
	del temp1[:]
	del temp2[:]
	del temp3[:]

def Fares(data,filepath1,filepath2,filepath3):
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))

	Gender = ['Male','Female']
	Class = ['Pclass1','Pclass2','Pclass3']
	Price = ['Low_Fare','Middle_Fare','High_Fare']
	Maturity = ['Young','Adult','Senior','Elderly','Unknown']

	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Age']):
		if j >=0 and j <=20:
			k = i-1
			temp1.append(data.loc[k])
		elif j >20 and j <=40:
			l = i-1
			temp2.append(data.loc[l])
		elif j >40 and j <=60:
			m = i-1
			temp3.append(data.loc[m])
		elif j >60 and j <=80:
			n = i-1
			temp4.append(data.loc[n])
		else:
			o = i-1
			temp5.append(data.loc[o])

	Young = pd.DataFrame(temp1)
	Adult = pd.DataFrame(temp2)
	Senior = pd.DataFrame(temp3)
	Elderly = pd.DataFrame(temp4)
	Unknown = pd.DataFrame(temp5)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Low_Fare':
				Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Young/Young.csv', index = False)
				Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Adult/adult.csv', index = False)
				Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Senior/senior.csv', index = False)
				Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Elderly/elderly.csv', index = False)
				Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Unknown/unknown.csv', index = False)

# 	if filepath == 'M1Lyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'M2Lyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'M3Lyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'F3Lyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Young.csv', index = False)
		
# 	elif filepath == 'M1Ladult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'M2Ladult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'M3Ladult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'F3Ladult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/adult.csv', index = False)
	
# 	elif filepath == 'M1Lsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'M2Lsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'M3Lsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'F3Lsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Senior/senior.csv', index = False)
	
# 	elif filepath == 'M1Lelderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'M2Lelderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'M3Lelderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'F3Lelderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Elderly/elderly.csv', index = False)
	
# 	elif filepath == 'M1Lunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'M2Lunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'M3Lunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'F3Lunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/unknown.csv', index = False)
# ####################################################################################################################	

# 	elif filepath == 'M1Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'F1Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'M2Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'F2Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'M3Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'F3Myoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Young.csv', index = False)
	
# 	elif filepath == 'M1Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'F1Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'M2Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'F2Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'M3Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'F3Madult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/adult.csv', index = False)
	
# 	elif filepath == 'M1Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'F1Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'M2Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'F2Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'M3Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'F3Msenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Senior/senior.csv', index = False)
	
# 	elif filepath == 'M1Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'F1Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'M2Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'F2Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'M3Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'F3Melderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Elderly/elderly.csv', index = False)
		
# 	elif filepath == 'M1Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'F1Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'M2Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'F2Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'M3Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'F3Munknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/unknown.csv', index = False)
# ##########################################################################################################################
# 	elif filepath == 'M1Hyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Young.csv', index = False)
# 	elif filepath == 'F1Hyoung':
# 		Young.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Young.csv', index = False)
	
# 	elif filepath == 'M1Hadult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/adult.csv', index = False)
# 	elif filepath == 'F1Hadult':
# 		Adult.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/adult.csv', index = False)
	
# 	elif filepath == 'M1Hsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/senior.csv', index = False)
# 	elif filepath == 'F1Hsenior':
# 		Senior.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Senior/senior.csv', index = False)
	
# 	elif filepath == 'M1Helderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Elderly/elderly.csv', index = False)
# 	elif filepath == 'F1Helderly':
# 		Elderly.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Elderly/elderly.csv', index = False)
	
# 	elif filepath == 'M1Hunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Unknown/unknown.csv', index = False)
# 	elif filepath == 'F1Hunknown':
# 		Unknown.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Unknown/unknown.csv', index = False)
#############################################################################################################################	
	del temp1[:]
	del temp2[:]
	del temp3[:]
	del temp4[:]
	del temp5[:]

def Ages(data,filepath):
	temp1,temp2 = ([] for i in range(2))

	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Ticket']):
		if type(j) == int:
			l = i-1
			temp1.append(data.loc[l])
		elif j.isdigit():
			l = i-1
			temp1.append(data.loc[l])
		else:
			m = i-1
			temp2.append(data.loc[m])
		
	Digit = pd.DataFrame(temp1)
	Alpha = pd.DataFrame(temp2)
########################################################### MALE ###############################################################
	if filepath == 'M1MFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1MFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1MFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1MFed':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1MFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Alpha/Alpha.csv', index = False)

	elif filepath == 'M1HFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1HFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'M1HFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/Alpha.csv', index = False)
	
	elif filepath == 'M2MFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'M2MFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'M2MFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Alpha/Alpha.csv', index = False)
	elif filepath == 'M2MFed':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/Alpha.csv', index = False)
	elif filepath == 'M2MFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/Alpha.csv', index = False)

	elif filepath == 'M3LFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'M3LFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'M3LFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/Alpha.csv', index = False)
	elif filepath == 'M3LFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Alpha/Alpha.csv', index = False)

	elif filepath == 'M3MFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'M3MFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'M3MFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/Alpha.csv', index = False)
########################################################### FEMALE ###############################################################
	elif filepath == 'F1MFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/Alpha.csv', index = False)
	
	elif filepath == 'F1HFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'F1HFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Alpha/Alpha.csv', index = False)
	
	elif filepath == 'F2MFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'F2MFse':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/Alpha.csv', index = False)
	
	elif filepath == 'F3LFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'F3LFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'F3LFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Alpha/Alpha.csv', index = False)

	elif filepath == 'F3MFyg':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/Alpha.csv', index = False)
	elif filepath == 'F3MFad':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/Alpha.csv', index = False)
	elif filepath == 'F3MFun':
		Digit.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/Digit.csv', index = False)
		Alpha.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Alpha/Alpha.csv', index = False)

	del temp1[:]
	del temp2[:]

def destination(data,filepath):
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))

	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Embarked']):
		if j == 'S':
			l = i-1
			temp1.append(data.loc[l])
		elif j == 'C':
			k = i-1
			temp2.append(data.loc[k])
		elif j == 'Q':
			m = i-1
			temp3.append(data.loc[m])
		else:
			w = i-1
			temp4.append(data.loc[w])
		
	S = pd.DataFrame(temp1)
	C = pd.DataFrame(temp2)
	Q = pd.DataFrame(temp3)
	U = pd.DataFrame(temp4)

	if filepath == 'M1MFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'M1MFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'M1MFadA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/U/U.csv', index = False)
	elif filepath == 'M1MFedD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/U/U.csv', index = False)
	elif filepath == 'M1MFseD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/U/U.csv', index = False)
	elif filepath == 'M1MFseA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/U/U.csv', index = False)
	elif filepath == 'M1MFunD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/U/U.csv', index = False)

	elif filepath == 'M1HFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'M1HFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'M1HFadA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/U/U.csv', index = False)
	elif filepath == 'M1HFseA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/U/U.csv', index = False)
	
	elif filepath == 'M2MFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'M2MFygA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/U/U.csv', index = False)
	elif filepath == 'M2MFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'M2MFseD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/U/U.csv', index = False)
	elif filepath == 'M2MFedA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/U/U.csv', index = False)
	elif filepath == 'M2MFunA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/U/U.csv', index = False)

	elif filepath == 'M3LFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'M3LFygA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/U/U.csv', index = False)
	elif filepath == 'M3LFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'M3LFadA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/U/U.csv', index = False)
	elif filepath == 'M3LFseD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/U/U.csv', index = False)
	elif filepath == 'M3LFseA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/U/U.csv', index = False)
	elif filepath == 'M3LFunD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/U/U.csv', index = False)

	elif filepath == 'M3MFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'M3MFygA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/U/U.csv', index = False)
	elif filepath == 'M3MFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'M3MFunD':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/U/U.csv', index = False)
	elif filepath == 'M3MFunA':
		S.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/U/U.csv', index = False)
########################################################### FEMALE ###############################################################
	elif filepath == 'F1MFseA':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/U/U.csv', index = False)
	
	elif filepath == 'F1HFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'F1HFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/U/U.csv', index = False)
	
	elif filepath == 'F2MFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'F2MFseD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/U/U.csv', index = False)
	elif filepath == 'F2MFseA':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/U/U.csv', index = False)
	
	elif filepath == 'F3LFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'F3LFadA':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/U/U.csv', index = False)
	elif filepath == 'F3LFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'F3LFunD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/U/U.csv', index = False)
	
	elif filepath == 'F3MFygD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/U/U.csv', index = False)
	elif filepath == 'F3MFygA':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/U/U.csv', index = False)
	elif filepath == 'F3MFadD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/U/U.csv', index = False)
	elif filepath == 'F3MFadA':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/U/U.csv', index = False)	
	elif filepath == 'F3MFunD':
		S.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/S/S.csv', index = False)
		C.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/C/C.csv', index = False)
		Q.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/Q/Q.csv', index = False)
		U.to_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/U/U.csv', index = False)	

	del temp1[:]
	del temp2[:]
	del temp3[:]
	del temp4[:]

def Seat(data,filepath1,filepath2,filepath3,filepath4,filepath5,filepath6):
	temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9 = ([] for i in range(9))
	Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','Missing','CabinG'] 
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Cabin']):
		temp8.append(j)
		print(temp8)
	
		for item in temp8:
			if type(item) == float:
				r =i-1
				temp7.append(data.loc[r])
				del temp8[:]
				break

			for word in item:
				if word == 'A':
					l =i-1
					temp1.append(data.loc[l])
					del temp8[:]
					break
				elif word == 'B':
					m = i-1
					temp2.append(data.loc[m])
					del temp8[:]
					break
				elif word == 'C':
					n = i-1
					temp3.append(data.loc[n])
					del temp8[:]
					break
				elif word == 'D':
					o = i-1
					temp4.append(data.loc[o])
					del temp8[:]
					break
				elif word == 'E':
					p = i-1
					temp5.append(data.loc[p])
					del temp8[:]
					break
				elif word == 'F':
					q = i-1
					temp6.append(data.loc[q])
					del temp8[:]
					break
				elif word == 'G':
					s = i-1
					temp9.append(data.loc[s])
					del temp8[:]
					break
				else:
					r =i-1
					temp7.append(data.loc[r])
					del temp8[:]
					break
	print(temp8)
	
	CabinA = pd.DataFrame(temp1)
	CabinB = pd.DataFrame(temp2)
	CabinC = pd.DataFrame(temp3)
	CabinD = pd.DataFrame(temp4)
	CabinE = pd.DataFrame(temp5)
	CabinF = pd.DataFrame(temp6)
	CabinG = pd.DataFrame(temp9)
	Missing  = pd.DataFrame(temp7)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)	
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Alpha':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
												
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Elderly':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':						
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'High_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass1':
			if filepath3 == 'High_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Male':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Elderly':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':						
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Alpha':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)				
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)				
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Male':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass1':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Alpha':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass1':
			if filepath3 == 'High_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass1':
			if filepath3 == 'High_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Female':
		if filepath2 == 'Pclass2':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Senior':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)												
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Low_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'Q':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)	
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)	
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							CabinG.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[7]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)	
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Young':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							CabinG.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[7]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							CabinG.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[7]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)	
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Adult':
					if filepath5  == 'Alpha':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							CabinG.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[7]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'S':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)						
	if filepath1 == 'Female':
		if filepath2 == 'Pclass3':
			if filepath3 == 'Middle_Fare':
				if filepath4 == 'Unknown':
					if filepath5  == 'Digit':
						if filepath6 == 'C':
							CabinA.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[0]), index = False)
							CabinB.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[1]), index = False)
							CabinC.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[2]), index = False)
							CabinD.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[3]), index = False)
							CabinE.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[4]), index = False)
							CabinF.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[5]), index = False)
							Missing.to_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(filepath1,filepath2,filepath3,filepath4,filepath5,filepath6,Position[6]), index = False)

	del temp1[:]
	del temp2[:]
	del temp3[:]
	del temp4[:]
	del temp5[:]
	del temp6[:]
	del temp7[:]
	del temp8[:]
########################################################################## MAIN PROGRAM ##############################################################################################################
df = pd.read_csv('/home/alvinwong/Desktop/AI/train.csv',skipinitialspace=True)

# call(df,'originalDataset')
########################################################################## 1st Split: Sex ##############################################################################################################
temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))

Gender = ['Male','Female']
Class = ['Pclass1','Pclass2','Pclass3']
Price = ['Low_Fare','Middle_Fare','High_Fare']
Maturity = ['Young','Adult','Senior','Elderly','Unknown']
Number = ['Alpha','Digit']
Place = ['S','C','Q','U']
Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','Missing'] 

df['ID'] = range(1,len(df)+1)
for i, j in zip(df['ID'],df['Sex']):
	if j == 'male':
		k = i-1
		temp1.append(df.loc[k])
	elif j == 'female':
		l = i-1
		temp2.append(df.loc[l])
	
Male = pd.DataFrame(temp1)
Female = pd.DataFrame(temp2)

Male.to_csv('/home/alvinwong/Desktop/AI/Male/Male.csv', index = False)
Female.to_csv('/home/alvinwong/Desktop/AI/Female/Female.csv', index = False)

del temp1[:]
del temp2[:]

for i in Gender:
	result = pd.read_csv('/home/alvinwong/Desktop/AI/{}/{}.csv'.format(i,i),skipinitialspace=True)
	gender(result,i)

########################################################################## 2nd Split for Male: PClass ##############################################################################################################
MPclass1 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Pclass1.csv',skipinitialspace=True)
MPclass2 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Pclass2.csv',skipinitialspace=True)
MPclass3 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Pclass3.csv',skipinitialspace=True)
FPclass1 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Pclass1.csv',skipinitialspace=True)
FPclass2 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Pclass2.csv',skipinitialspace=True)
FPclass3 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Pclass3.csv',skipinitialspace=True)

PClass(MPclass1,'MPclass1')
PClass(MPclass2,'MPclass2')
PClass(MPclass3, 'MPclass3')
PClass(FPclass1,'FPclass1')
PClass(FPclass2,'FPclass2')
PClass(FPclass3, 'FPclass3')
# ########################################################################## 3rd Split for PClass1: Fare ##############################################################################################################
for i in Gender:
		for j in Class:
			for k in Price:
				try:
					result = pd.read_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}.csv'.format(i,j,k,k),skipinitialspace=True)
					Fares(result,i,j,k)
				except pd.errors.EmptyDataError:
					continue

				

# Low_Fare1 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Low_Fare/Low_Fare.csv',skipinitialspace=True)
# Middle_Fare1 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)
# High_Fare1 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/High_Fare.csv',skipinitialspace=True)

# FMiddle_Fare1 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)
# FHigh_Fare1 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/High_Fare.csv',skipinitialspace=True)

# Low_Fare2 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Low_Fare/Low_Fare.csv',skipinitialspace=True)
# Middle_Fare2 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)
# FMiddle_Fare2 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)

# Low_Fare3 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Low_Fare.csv',skipinitialspace=True)
# Middle_Fare3 = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)
# FLow_Fare3 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Low_Fare.csv',skipinitialspace=True)
# FMiddle_Fare3 = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Middle_Fare.csv',skipinitialspace=True)

# Fares(Low_Fare1, 'M1Lyoung')
# Fares(Low_Fare2, 'M2Lyoung')
# Fares(Low_Fare3, 'M3Lyoung')
# Fares(FLow_Fare3, 'F3Lyoung')

# Fares(Low_Fare1, 'M1Ladult')
# Fares(Low_Fare2, 'M2Ladult')
# Fares(Low_Fare3, 'M3Ladult')
# Fares(FLow_Fare3, 'F3Ladult')

# Fares(Low_Fare1, 'M1Lsenior')
# Fares(Low_Fare2, 'M2Lsenior')
# Fares(Low_Fare3, 'M3Lsenior')
# Fares(FLow_Fare3, 'F3Lsenior')

# Fares(Low_Fare1, 'M1Lelderly')
# Fares(Low_Fare2, 'M2Lelderly')
# Fares(Low_Fare3, 'M3Lelderly')
# Fares(FLow_Fare3, 'F3Lelderly')

# Fares(Low_Fare1, 'M1Lunknown')
# Fares(Low_Fare2, 'M2Lunknown')
# Fares(Low_Fare3, 'M3Lunknown')
# Fares(FLow_Fare3, 'F3Lunknown')
# #################################################
# Fares(Middle_Fare1, 'M1Myoung')
# Fares(FMiddle_Fare1, 'F1Myoung')
# Fares(Middle_Fare2, 'M2Myoung')
# Fares(FMiddle_Fare2, 'F2Myoung')
# Fares(Middle_Fare3, 'M3Myoung')
# Fares(FMiddle_Fare3, 'F3Myoung')

# Fares(Middle_Fare1, 'M1Madult')
# Fares(FMiddle_Fare1, 'F1Madult')
# Fares(Middle_Fare2, 'M2Madult')
# Fares(FMiddle_Fare2, 'F2Madult')
# Fares(Middle_Fare3, 'M3Madult')
# Fares(FMiddle_Fare3, 'F3Madult')

# Fares(Middle_Fare1, 'M1Msenior')
# Fares(FMiddle_Fare1, 'F1Msenior')
# Fares(Middle_Fare2, 'M2Msenior')
# Fares(FMiddle_Fare2, 'F2Msenior')
# Fares(Middle_Fare3, 'M3Msenior')
# Fares(FMiddle_Fare3, 'F3Msenior')

# Fares(Middle_Fare1, 'M1Melderly')
# Fares(FMiddle_Fare1, 'F1Melderly')
# Fares(Middle_Fare2, 'M2Melderly')
# Fares(FMiddle_Fare2, 'F2Melderly')
# Fares(Middle_Fare3, 'M3Melderly')
# Fares(FMiddle_Fare3, 'F3Melderly')

# Fares(Middle_Fare1, 'M1Munknown')
# Fares(FMiddle_Fare1, 'F1Munknown')
# Fares(Middle_Fare2, 'M2Munknown')
# Fares(FMiddle_Fare2, 'F2Munknown')
# Fares(Middle_Fare3, 'M3Munknown')
# Fares(FMiddle_Fare3, 'F3Munknown')
# ########################################################################
# Fares(High_Fare1, 'M1Hyoung')
# Fares(FHigh_Fare1, 'F1Hyoung')

# Fares(High_Fare1, 'M1Hadult')
# Fares(FHigh_Fare1, 'F1Hadult')

# Fares(High_Fare1, 'M1Hsenior')
# Fares(FHigh_Fare1, 'F1Hsenior')

# Fares(High_Fare1, 'M1Helderly')
# Fares(FHigh_Fare1, 'F1Helderly')

# Fares(High_Fare1, 'M1Hunknown')
# Fares(FHigh_Fare1, 'F1Hunknown')
########################################################################### 4th Split for Middle_Fare: Age ##############################################################################################################
M1MFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Young.csv',skipinitialspace=True)
M1MFad = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/adult.csv',skipinitialspace=True)
M1MFse = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/senior.csv',skipinitialspace=True)
M1MFed = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/elderly.csv',skipinitialspace=True)
M1MFun = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/unknown.csv',skipinitialspace=True)

M1HFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Young.csv',skipinitialspace=True)
M1HFad = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/adult.csv',skipinitialspace=True)
M1HFse = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/senior.csv',skipinitialspace=True)

M2MFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Young.csv',skipinitialspace=True)
M2MFad = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/adult.csv',skipinitialspace=True)
M2MFse = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/senior.csv',skipinitialspace=True)
M2MFed = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/elderly.csv',skipinitialspace=True)
M2MFun = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/unknown.csv',skipinitialspace=True)

M3LFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Young.csv',skipinitialspace=True)
M3LFad = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/adult.csv',skipinitialspace=True)
M3LFse = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/senior.csv',skipinitialspace=True)
M3LFun = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/unknown.csv',skipinitialspace=True)

M3MFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Young.csv',skipinitialspace=True)
M3MFad = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/adult.csv',skipinitialspace=True)
M3MFun = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/unknown.csv',skipinitialspace=True)

F1MFse = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/senior.csv',skipinitialspace=True)

F1HFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Young.csv',skipinitialspace=True)
F1HFad = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/adult.csv',skipinitialspace=True)

F2MFad = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/adult.csv',skipinitialspace=True)
F2MFse = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/senior.csv',skipinitialspace=True)

F3LFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Young.csv',skipinitialspace=True)
F3LFad = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/adult.csv',skipinitialspace=True)
F3LFun = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/unknown.csv',skipinitialspace=True)

F3MFyg = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Young.csv',skipinitialspace=True)
F3MFad = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/adult.csv',skipinitialspace=True)
F3MFun = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/unknown.csv',skipinitialspace=True)

Ages(M1MFyg,'M1MFyg')
Ages(M1MFad,'M1MFad')
Ages(M1MFse,'M1MFse')
Ages(M1MFed,'M1MFed')
Ages(M1MFun,'M1MFun')

Ages(M1HFyg,'M1HFyg')
Ages(M1HFad,'M1HFad')
Ages(M1HFse,'M1HFse')

Ages(M2MFyg,'M2MFyg')
Ages(M2MFad,'M2MFad')
Ages(M2MFse,'M2MFse')
Ages(M2MFed,'M2MFed')
Ages(M2MFun,'M2MFun')

Ages(M3LFyg,'M3LFyg')
Ages(M3LFad,'M3LFad')
Ages(M3LFse,'M3LFse')
Ages(M3LFun,'M3LFun')

Ages(M3MFyg,'M3MFyg')
Ages(M3MFad,'M3MFad')
Ages(M3MFun,'M3MFun')

Ages(F1MFse,'F1MFse')

Ages(F1HFyg,'F1HFyg')
Ages(F1HFad,'F1HFad')

Ages(F2MFad,'F2MFad')
Ages(F2MFse,'F2MFse')

Ages(F3LFyg,'F3LFyg')
Ages(F3LFad,'F3LFad')
Ages(F3LFun,'F3LFun')

Ages(F3MFyg,'F3MFyg')
Ages(F3MFad,'F3MFad')
Ages(F3MFun,'F3MFun')
########################################################################### 5th Split by Ticket  ##############################################################################################################
M1MFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
M1MFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
M1MFseD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Digit/Digit.csv',skipinitialspace=True)
M1MFedD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Elderly/Digit/Digit.csv',skipinitialspace=True)
M1MFunD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Unknown/Digit/Digit.csv',skipinitialspace=True)
M1MFadA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Adult/Alpha/Alpha.csv',skipinitialspace=True)
M1MFseA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/Middle_Fare/Senior/Alpha/Alpha.csv',skipinitialspace=True)

M1HFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
M1HFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
M1HFadA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Adult/Alpha/Alpha.csv',skipinitialspace=True)
M1HFseA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass1/High_Fare/Senior/Alpha/Alpha.csv',skipinitialspace=True)

M2MFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
M2MFygA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Young/Alpha/Alpha.csv',skipinitialspace=True)
M2MFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
M2MFseD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Senior/Digit/Digit.csv',skipinitialspace=True)
M2MFedA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Elderly/Alpha/Alpha.csv',skipinitialspace=True)
M2MFunA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass2/Middle_Fare/Unknown/Alpha/Alpha.csv',skipinitialspace=True)

M3LFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
M3LFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
M3LFseD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Digit/Digit.csv',skipinitialspace=True)
M3LFunD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Unknown/Digit/Digit.csv',skipinitialspace=True)
M3LFygA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Young/Alpha/Alpha.csv',skipinitialspace=True)
M3LFadA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Adult/Alpha/Alpha.csv',skipinitialspace=True)
M3LFseA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Low_Fare/Senior/Alpha/Alpha.csv',skipinitialspace=True)

M3MFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
M3MFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
M3MFunD = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Digit/Digit.csv',skipinitialspace=True)
M3MFygA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Young/Alpha/Alpha.csv',skipinitialspace=True)
M3MFunA = pd.read_csv('/home/alvinwong/Desktop/AI/Male/Pclass3/Middle_Fare/Unknown/Alpha/Alpha.csv',skipinitialspace=True)

F1MFseA = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/Middle_Fare/Senior/Alpha/Alpha.csv',skipinitialspace=True)

F1HFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
F1HFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass1/High_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)

F2MFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
F2MFseD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Digit/Digit.csv',skipinitialspace=True)
F2MFseA = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass2/Middle_Fare/Senior/Alpha/Alpha.csv',skipinitialspace=True)

F3LFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
F3LFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
F3LFunD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Unknown/Digit/Digit.csv',skipinitialspace=True)
F3LFadA = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Low_Fare/Adult/Alpha/Alpha.csv',skipinitialspace=True)

F3MFygD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Digit/Digit.csv',skipinitialspace=True)
F3MFadD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Digit/Digit.csv',skipinitialspace=True)
F3MFunD = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Unknown/Digit/Digit.csv',skipinitialspace=True)
F3MFygA = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Young/Alpha/Alpha.csv',skipinitialspace=True)
F3MFadA = pd.read_csv('/home/alvinwong/Desktop/AI/Female/Pclass3/Middle_Fare/Adult/Alpha/Alpha.csv',skipinitialspace=True)

destination(M1MFygD,'M1MFygD')
destination(M1MFadD,'M1MFadD')
destination(M1MFseD,'M1MFseD')
destination(M1MFedD,'M1MFedD')
destination(M1MFunD,'M1MFunD')
destination(M1MFadA,'M1MFadA')
destination(M1MFseA,'M1MFseA')

destination(M1HFygD,'M1HFygD')
destination(M1HFadD,'M1HFadD')
destination(M1HFadA,'M1HFadA')
destination(M1HFseA,'M1HFseA')

destination(M2MFygD,'M2MFygD')
destination(M2MFygA,'M2MFygA')
destination(M2MFadD,'M2MFadD')
destination(M2MFseD,'M2MFseD')
destination(M2MFedA,'M2MFedA')
destination(M2MFunA,'M2MFunA')
 
destination(M3LFygD,'M3LFygD')
destination(M3LFadD,'M3LFadD')
destination(M3LFseD,'M3LFseD')
destination(M3LFunD,'M3LFunD')
destination(M3LFygA,'M3LFygA')
destination(M3LFadA,'M3LFadA')
destination(M3LFseA,'M3LFseA')

destination(M3MFygD,'M3MFygD')
destination(M3MFadD,'M3MFadD')
destination(M3MFunD,'M3MFunD')
destination(M3MFygA,'M3MFygA')
destination(M3MFunA,'M3MFunA')
 
destination(F1MFseA,'F1MFseA')

destination(F1HFygD,'F1HFygD')
destination(F1HFadD,'F1HFadD')

destination(F2MFadD,'F2MFadD')
destination(F2MFseD,'F2MFseD')
destination(F2MFseA,'F2MFseA')

destination(F3LFygD,'F3LFygD')
destination(F3LFadD,'F3LFadD')
destination(F3LFunD,'F3LFunD')
destination(F3LFadA,'F3LFadA')

destination(F3MFygD,'F3MFygD')
destination(F3MFadD,'F3MFadD')
destination(F3MFunD,'F3MFunD')
destination(F3MFygA,'F3MFygA')
destination(F3MFadA,'F3MFadA')

# ########################################################################## 6th Split: SibSp ##############################################################################################################
# df['ID'] = range(1,len(df)+1)
# for i, j in zip(df['ID'],df['SibSp']):
# 	if j == 0:
# 		k = i-1
# 		temp1.append(df.loc[k])
# 	elif j == 1:
# 		l = i-1
# 		temp2.append(df.loc[l])
# 	elif j == 2:
# 		m = i-1
# 		temp3.append(df.loc[m])
# 	elif j == 3:
# 		n = i-1
# 		temp4.append(df.loc[n])
# 	elif j == 4:
# 		o = i-1
# 		temp5.append(df.loc[o])
# 	elif j >= 5:
# 		p = i-1
# 		temp6.append(df.loc[p])

# Sbone = pd.DataFrame(temp1)
# Sbtwo = pd.DataFrame(temp2)
# Sbthree = pd.DataFrame(temp3)
# Sbfour = pd.DataFrame(temp4)
# Sbfive = pd.DataFrame(temp5)
# Sbsix = pd.DataFrame(temp6)

# Sbone.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbone.csv', index = False)
# Sbtwo.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbtwo.csv', index = False)
# Sbthree.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbthree.csv', index = False)
# Sbfour.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbfour.csv', index = False)
# Sbfive.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbfive.csv', index = False)
# Sbsix.to_csv('/home/alvinwong/Desktop/AI/SibSp/Sbsix.csv', index = False)

# del temp1[:]
# del temp2[:]
# del temp3[:]
# del temp4[:]
# del temp5[:]
# del temp6[:]

# Sbone = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbone.csv',skipinitialspace=True)
# Sbtwo = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbtwo.csv',skipinitialspace=True)
# Sbthree = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbone.csv',skipinitialspace=True)
# Sbfour = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbtwo.csv',skipinitialspace=True)
# Sbfive = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbone.csv',skipinitialspace=True)
# Sbsix = pd.read_csv('/home/alvinwong/Desktop/AI/SibSp/Sbtwo.csv',skipinitialspace=True)

# # call(Sbone,'Sbone')
# # call(Sbtwo,'Sbtwo')
# # call(Sbthree,'Sbthree')
# # call(Sbfour,'Sbfour')
# # call(Sbfive,'Sbfive')
# # call(Sbsix,'Sbsix')
# ########################################################################## 7th Split: Parch ##############################################################################################################
for i in Gender:
	for j in Class:
		for k in Price:
			for l in Maturity:
				for m in Number:
					for n in Place:
						try:
							result = pd.read_csv('/home/alvinwong/Desktop/AI/{}/{}/{}/{}/{}/{}/{}.csv'.format(i,j,k,l,m,n,n),skipinitialspace=True)
							Seat(result,i,j,k,l,m,n)
						except pd.errors.EmptyDataError:
							continue
						except FileNotFoundError:
							continue

