import numpy as np
import os 
import math
import pandas as pd
import csv
from itertools import zip_longest
import glob
import shutil

Gender = ['male','female']
Class = ['Pclass1','Pclass2','Pclass3']
Price = ['Low_Fare','Middle_Fare','High_Fare']
Maturity = ['Young','Adult','Senior','Elderly','Unknown']
Number = ['Alpha','Digit']
Place = ['S','C','Q','U']
Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','CabinG','Missing'] 
Siblings = [0,1,2,3,4,5]
ParCH = [0,1,2,3,4,5]
result = [0,1]
highest, filename, node = ([] for i in range(3))
count= 0

###################################################### Subroutine Function to check all attribute values ############################################
def info_division(inputs,name,file):
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
	print(name)
	Info_data = info_division(data['Survived'],name,data)
	print('\n')
	print(Info_data)

	Class_Type(data['Survived'],data['Pclass'],len(data),Info_data,name)
	gender(data['Survived'],data['Sex'],len(data),Info_data,name)
	location(data['Survived'],data['Embarked'],len(data),Info_data,name)
	ParentCh(data['Survived'],data['Parch'],len(data),Info_data,name)
	Sibling(data['Survived'],data['SibSp'],len(data),Info_data,name)
	Mature(data['Survived'],data['Age'],len(data),Info_data,name)
	ticket(data['Survived'],data['Ticket'],len(data),Info_data,name)
	price(data['Survived'],data['Fare'],len(data),Info_data,name)
	Seat(data['Survived'],data['Cabin'],len(data),Info_data,name)
	print('\n')
	print(highest)
	title  = max(highest)
	return title

def max(data):
	largest = 0
	for i in data:
		if i[2] >= largest:
			largest = i[2]
			name = i[0]
			title = i[1]

	print('Highest Ratio for {} is {} with a value of {}'.format(name,title,largest))
	# print('title = '.format(title))
	del highest[:]	
	# print('highest = {}'.format(highest))
	return title

############################################################### Entropy Function #######################################################################################################################
def gender(temp1,temp2,TCount,Info_df,name):
	Gender = ['male','female']
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

	print ('Name: {}, Info_Sex = {}, Gain_Sex = {}, Sex_Ratio = {}'.format(name,Info_Sex,Gain_Sex,Sex_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))
	highest.append([name,'Sex',Sex_ratio])

def Class_Type(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_Pclass = {}, Gain_Pclass = {}, PClass_Ratio = {}'.format(name,Info_Pclass,Gain_Pclass,Pclass_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))
	highest.append([name,'Pclass',Pclass_ratio])

def location(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_dest = {}, Gain_dest = {}, Dest_ratio = {}'.format(name,Info_dest,Gain_dest,dest_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8 = (0 for i in range(8))
	highest.append([name,'Embarked',dest_ratio])

def ParentCh(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_parch = {}, Gain_parch = {}, Parch_ratio = {}'.format(name,Info_parch,Gain_parch,parch_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))
	highest.append([name,'Parch',parch_ratio])

def Sibling(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_sibsp = {}, Gain_sibsp = {}, Sibsp_ratio = {}'.format(name,Info_sibsp,Gain_sibsp,sibsp_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))
	highest.append([name,'SibSp',sibsp_ratio])

def Mature(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_age = {}, Gain_age = {}, Age_ratio = {}'.format(name,Info_age,Gain_age,age_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10 = (0 for i in range(10))
	highest.append([name,'Age',age_ratio])

def ticket(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {},Info_Ticket = {}, Gain_Ticket = {}, Ticket_ratio = {}'.format(name,Info_Ticket,Gain_Ticket,Ticket_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10,count_11,count_12 = (0 for i in range(12))
	highest.append([name,'Ticket',Ticket_ratio])

def price(temp1,temp2,TCount,Info_df,name):
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

	print('Name: {}, Info_Fare = {}, Gain_Fare = {}, Fare_Ratio = {}'.format(name,Info_cash,Gain_cash,cash_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))
	highest.append([name,'Fare',cash_ratio])

def Seat(temp1,temp2,TCount,Info_df,name):
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
		Cabin_ratio = Gain_cabin/Split_cabin 
	except ZeroDivisionError:
		Cabin_ratio = 0

	print ('Name: {}, Info_cabin = {}, Gain_cabin = {}, Cabin_Ratio = {}'.format(name,Info_cabin,Gain_cabin,Cabin_ratio))
	count_1,count_2,count_3,count_4,count_5,count_6 = (0 for i in range(6))
	highest.append([name,'Cabin',Cabin_ratio])

############################################################################################### Spliting Function #######################################################################################
def Sex(data,filepath):
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))	
	Gender = ['male','female']
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Sex']):
		if j == 'male':
			a = i-1
			temp1.append(data.loc[a])
		elif j == 'female':
			a = i-1
			temp2.append(data.loc[a])

	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)

	output1.to_csv('{}{}.csv'.format(filepath,Gender[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath,Gender[1]), index = False)

	filename1 = '{}{}'.format(filepath,Gender[0])
	filename2 = '{}{}'.format(filepath,Gender[1])

	filename.append(filename1)
	filename.append(filename2)

def Pclass(data,filepath):
	Class = ['Pclass1','Pclass2','Pclass3']
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Pclass']):
		if j == 1:
			a = i-1
			temp1.append(data.loc[a])
		elif j == 2:
			a = i-1
			temp2.append(data.loc[a])
		elif j == 3:
			a = i-1
			temp3.append(data.loc[a])

	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)

	output1.to_csv('{}{}.csv'.format(filepath, Class[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Class[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Class[2]), index = False)

	filename1 = '{}{}'.format(filepath, Class[0])
	filename2 = '{}{}'.format(filepath, Class[1])
	filename3 = '{}{}'.format(filepath, Class[2])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)

def Fare(data,filepath):
	Price = ['Low_Fare','Middle_Fare','High_Fare']
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))	
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
	
	
	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)

	output1.to_csv('{}{}.csv'.format(filepath, Price[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Price[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Price[2]), index = False)

	filename1 = '{}{}'.format(filepath, Price[0])
	filename2 = '{}{}'.format(filepath, Price[1])
	filename3 = '{}{}'.format(filepath, Price[2])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	
def Age(data,filepath):
	Maturity = ['Young','Adult','Senior','Elderly','Unknown']
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))	
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


	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)
	output4 = pd.DataFrame(temp4)
	output5 = pd.DataFrame(temp5)

	output1.to_csv('{}{}.csv'.format(filepath, Maturity[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Maturity[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Maturity[2]), index = False)
	output4.to_csv('{}{}.csv'.format(filepath, Maturity[3]), index = False)
	output5.to_csv('{}{}.csv'.format(filepath, Maturity[4]), index = False)

	filename1 = '{}{}'.format(filepath, Maturity[0])
	filename2 = '{}{}'.format(filepath, Maturity[1])
	filename3 = '{}{}'.format(filepath, Maturity[2])
	filename4 = '{}{}'.format(filepath, Maturity[3])
	filename5 = '{}{}'.format(filepath, Maturity[4])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	filename.append(filename4)
	filename.append(filename5)

def Ticket(data,filepath):
	Number = ['Alpha','Digit']
	temp1,temp2,temp3,temp4,temp5,temp6 = ([] for i in range(6))	
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


	output1 = pd.DataFrame(temp2)
	output2 = pd.DataFrame(temp1)

	output1.to_csv('{}{}.csv'.format(filepath, Number[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Number[1]), index = False)

	filename1 = '{}{}'.format(filepath,Number[0])
	filename2 = '{}{}'.format(filepath,Number[1])

	filename.append(filename1)
	filename.append(filename2)

def Embarked(data,filepath):
	Place = ['S','C','Q','U']
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
		elif type(j) == float:
			w = i-1
			temp4.append(data.loc[w])



	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)
	output4 = pd.DataFrame(temp4)

	output1.to_csv('{}{}.csv'.format(filepath, Place[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Place[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Place[2]), index = False)
	output4.to_csv('{}{}.csv'.format(filepath, Place[3]), index = False)

	filename1 = '{}{}'.format(filepath, Place[0])
	filename2 = '{}{}'.format(filepath, Place[1])
	filename3 = '{}{}'.format(filepath, Place[2])
	filename4 = '{}{}'.format(filepath, Place[3])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	filename.append(filename4)

def Cabin(data,filepath):
	Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','CabinG','Unknown'] 
	temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9 = ([] for i in range(9))	
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Cabin']):
		temp9.append(j)
	
		for item in temp9:
			if type(item) == float:
				r =i-1
				temp8.append(data.loc[r])
				del temp9[:]
				break

			for word in item:
				if word == 'A':
					l =i-1
					temp1.append(data.loc[l])
					del temp9[:]
					break
				elif word == 'B':
					m = i-1
					temp2.append(data.loc[m])
					del temp9[:]
					break
				elif word == 'C':
					n = i-1
					temp3.append(data.loc[n])
					del temp9[:]
					break
				elif word == 'D':
					o = i-1
					temp4.append(data.loc[o])
					del temp9[:]
					break
				elif word == 'E':
					p = i-1
					temp5.append(data.loc[p])
					del temp9[:]
					break
				elif word == 'F':
					q = i-1
					temp6.append(data.loc[q])
					del temp9[:]
					break
				elif word == 'G':
					s = i-1
					temp7.append(data.loc[s])
					del temp9[:]
					break
				else:
					r =i-1
					temp8.append(data.loc[r])
					del temp9[:]
					break


	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)
	output4 = pd.DataFrame(temp4)
	output5 = pd.DataFrame(temp5)
	output6 = pd.DataFrame(temp6)
	output7 = pd.DataFrame(temp7)
	output8 = pd.DataFrame(temp8)

	output1.to_csv('{}{}.csv'.format(filepath, Position[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Position[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Position[2]), index = False)
	output4.to_csv('{}{}.csv'.format(filepath, Position[3]), index = False)
	output5.to_csv('{}{}.csv'.format(filepath, Position[4]), index = False)
	output6.to_csv('{}{}.csv'.format(filepath, Position[5]), index = False)
	output7.to_csv('{}{}.csv'.format(filepath, Position[6]), index = False)
	output8.to_csv('{}{}.csv'.format(filepath, Position[7]), index = False)

	filename1 = '{}{}'.format(filepath, Position[0])
	filename2 = '{}{}'.format(filepath, Position[1])
	filename3 = '{}{}'.format(filepath, Position[2])
	filename4 = '{}{}'.format(filepath, Position[3])
	filename5 = '{}{}'.format(filepath, Position[4])
	filename6 = '{}{}'.format(filepath, Position[5])
	filename7 = '{}{}'.format(filepath, Position[6])
	filename8 = '{}{}'.format(filepath, Position[7])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	filename.append(filename4)
	filename.append(filename5)
	filename.append(filename6)
	filename.append(filename7)
	filename.append(filename8)

def SibSp(data,filepath):
	Siblings = [0,1,2,3,4,5]
	temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9 = ([] for i in range(9))	
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['SibSp']):
		if j == 0:
			k = i-1
			temp1.append(data.loc[k])
		elif j == 1:
			l = i-1
			temp2.append(data.loc[l])
		elif j  == 2:
			m = i-1
			temp3.append(data.loc[m])
		elif j == 3:
			n = i-1
			temp4.append(data.loc[n])
		elif j == 4:
			o = i-1
			temp5.append(data.loc[o])
		else:
			p = i-1
			temp6.append(data.loc[p])



	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)
	output4 = pd.DataFrame(temp4)
	output5 = pd.DataFrame(temp5)
	output6 = pd.DataFrame(temp6)

	output1.to_csv('{}{}.csv'.format(filepath, Siblings[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, Siblings[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, Siblings[2]), index = False)
	output4.to_csv('{}{}.csv'.format(filepath, Siblings[3]), index = False)
	output5.to_csv('{}{}.csv'.format(filepath, Siblings[4]), index = False)
	output6.to_csv('{}{}.csv'.format(filepath, Siblings[5]), index = False)

	filename1 = '{}{}'.format(filepath, Siblings[0])
	filename2 = '{}{}'.format(filepath, Siblings[1])
	filename3 = '{}{}'.format(filepath, Siblings[2])
	filename4 = '{}{}'.format(filepath, Siblings[3])
	filename5 = '{}{}'.format(filepath, Siblings[4])
	filename6 = '{}{}'.format(filepath, Siblings[5])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	filename.append(filename4)
	filename.append(filename5)
	filename.append(filename6)

def Parch(data,filepath):
	ParCH = [0,1,2,3,4,5]
	temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9 = ([] for i in range(9))	
	data['ID'] = range(1,len(data)+1)
	for i, j in zip(data['ID'],data['Parch']):
		if j == 0:
			k = i-1
			temp1.append(data.loc[k])
		elif j == 1:
			l = i-1
			temp2.append(data.loc[l])
		elif j  == 2:
			m = i-1
			temp3.append(data.loc[m])
		elif j == 3:
			n = i-1
			temp4.append(data.loc[n])
		elif j == 4:
			o = i-1
			temp5.append(data.loc[o])
		else:
			p = i-1
			temp6.append(data.loc[p])



	output1 = pd.DataFrame(temp1)
	output2 = pd.DataFrame(temp2)
	output3 = pd.DataFrame(temp3)
	output4 = pd.DataFrame(temp4)
	output5 = pd.DataFrame(temp5)
	output6 = pd.DataFrame(temp6)

	output1.to_csv('{}{}.csv'.format(filepath, ParCH[0]), index = False)
	output2.to_csv('{}{}.csv'.format(filepath, ParCH[1]), index = False)
	output3.to_csv('{}{}.csv'.format(filepath, ParCH[2]), index = False)
	output4.to_csv('{}{}.csv'.format(filepath, ParCH[3]), index = False)
	output5.to_csv('{}{}.csv'.format(filepath, ParCH[4]), index = False)
	output6.to_csv('{}{}.csv'.format(filepath, ParCH[5]), index = False)

	filename1 = '{}{}'.format(filepath, ParCH[0])
	filename2 = '{}{}'.format(filepath, ParCH[1])
	filename3 = '{}{}'.format(filepath, ParCH[2])
	filename4 = '{}{}'.format(filepath, ParCH[3])
	filename5 = '{}{}'.format(filepath, ParCH[4])
	filename6 = '{}{}'.format(filepath, ParCH[5])

	filename.append(filename1)
	filename.append(filename2)
	filename.append(filename3)
	filename.append(filename4)
	filename.append(filename5)
	filename.append(filename6)
################################################################################### Decision Making Fucntion #######################################################
def prediction(filepath):
	data = pd.read_csv(filepath,skipinitialspace=True)
	Survive, Die = (0 for i in range(2))
	for a in data['Survived']:
		if a  == 1:
			Survive+=1
		elif a == 0:
			Die+=1

	if Die == len(data):
		data['Prediction'] = 0
		data.to_csv(filepath, index = False)

	elif Survive == len(data):
		data['Prediction'] = 1
		data.to_csv(filepath, index = False)

def function(result,dst,Function):
	Option = ['Sex','Pclass','Fare','Age','Ticket','Embarked','Cabin','SibSp','Parch']
	if Function == 'Sex':
		# print('dst = {}'.format(dst))
		src = '{}{}'.format(dst,Function)
		# print('src = {}'.format(src))
		Sex(result,src)
		# print('Alvin')
	elif Function == 'Pclass':
		src = '{}{}'.format(dst,Function)
		Pclass(result,src)
		# print('Alvin')
	elif Function == 'Fare':
		src = '{}{}'.format(dst,Function)
		Fare(result,src)
	elif Function == 'Age':
		src = '{}{}'.format(dst,Function)
		Age(result,src)
	elif Function == 'Ticket':
		src = '{}{}'.format(dst,Function)
		Ticket(result,src)
	elif Function == 'Embarked':
		src = '{}{}'.format(dst,Function)
		Embarked(result,src)
	elif Function == 'Cabin':
		src = '{}{}'.format(dst,Function)
		Cabin(result,src)
		# print('Alvin')
	elif Function == 'SibSp':
		src = '{}{}'.format(dst,Function)
		SibSp(result,src)
	elif Function == 'Parch':
		src = '{}{}'.format(dst,Function)
		Parch(result,src)

def decision_making(filepath,dst):
	# print('filepath in DM is {}'.format(filepath))
	data = pd.read_csv(filepath,skipinitialspace=True)
	title = call(data,filepath)
	# print('title = {}'.format(title))
	for i in Option:
		if i == title:
			Function = i
			print(Function)
			try:
				function(data,dst,Function)
			except pd.errors.EmptyDataError:
				continue
			except FileNotFoundError:
				continue

def Calulation(data,name):
	TP,FP,TN,FN = (0 for i in range(4))

	total =len(data)

	for i,j in zip(Results['Survived'],Results['Prediction']):
		if i == 1 and j == 1:
			TP+=1
		elif i == 0 and j == 1:
			FP+=1
		elif i == 0 and j == 0:
			TN+=1
		elif i == 1 and j == 0:
			FN+=1

	TPR = TP/(TP+FN)*100
	FPR = FP/(FP+TN)*100
	recall = TP/(TP+FN)*100
	precision = TP/(TP+FP)*100
	F_measure = (2*precision*recall)/(precision+recall)
	accuracy  = ((TP+TN)/total)*100

	print('\n')
	print(' {}: True_Positive = {}, False_Positive = {}, True_Negative = {}, False_Negative = {}.'.format(name,TP,FP,TN,FN))
	print('{}: Precision = {}, Recall = {}, F-Measure = {}.'.format(name,precision,recall,F_measure))
	print('{}: True_Positive_Rate = {}, False_Positive_Rate = {}.'.format(name,TPR,FPR))
	print('{}: Accuracy = {}'.format(name,accuracy))
	print('\n')
##################################################################### Maninuplation & Labour Function #####################################################################
def Check_data(filepath):
	data = pd.read_csv(filepath,skipinitialspace=True)
	Survive, Die = (0 for i in range(2))
	for a in data['Survived']:
		if a  == 1:
			Survive+=1
		elif a == 0:
			Die+=1

	if Survive == len(data):
		print(filepath)
		exit()
	if Die == len(data):
		print(filepath)
		exit()

def remove(filelist):
	for j in filelist:
		with open(j) as infocsv:
		    reader = [i for i in csv.DictReader(infocsv)]
		    if len(reader)>0:
		        print ('not empty')
		    else:
		        print ('empty')
		        os.remove(j)
	     

def move(src,dst):
	for i in src:
		shutil.move(i, dst)
############################################################################# Main Program ################################################################################
Split = [('Sex','Gender'),('Pclass','Class'),('Fare','Price'),('Age','Maturity'),('Ticket','Number'),('Embarked','Place'),('Cabin','Position'),('SibSp','Siblings'),('Parch''ParCH')]

filepath = '/home/alvinwong/Desktop/AI/TrainClassification/train.csv'
dst = '/home/alvinwong/Desktop/AI/TrainClassification/'

decision_making(filepath,dst) # Checking for the Best Entropy Ratio to Split!

empty_file = glob.glob('/home/alvinwong/Desktop/AI/TrainClassification/*.csv')
remove(empty_file)

MALE = '/home/alvinwong/Desktop/AI/TrainClassification/Male'
FEMALE =' /home/alvinwong/Desktop/AI/TrainClassification/Female'
os.chdir('')
for counter, file in enumerate(glob.glob("*")):
	prediction(file)

os.chdir('/home/alvinwong/Desktop/AI/TrainClassification/Results')
merge = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("*")):
    namedf = pd.read_csv(file)
    print(namedf)
    if 'Prediction' in namedf:
    	merge = merge.append(namedf)
 
merge.to_csv('/home/alvinwong/Desktop/AI/TrainClassification/Results/PredictedTrainResult.csv')

Results = pd.read_csv('/home/alvinwong/Desktop/AI/TrainClassification/Results/PredictedTrainResult.csv')
Calulation(Results,'Training Data')