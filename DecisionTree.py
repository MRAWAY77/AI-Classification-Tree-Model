import numpy as np
import os 
import math
import pandas as pd
import csv
from itertools import zip_longest
import glob

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

def Cabin(data,filepath):
	Position = ['CabinA','CabinB','CabinC','CabinD','CabinE','CabinF','CabinG','Missing'] 
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

def SibSp(data,filepath):
	Siblings = ['S0','S1','S2','S3','S4','S5']
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

def Parch(data,filepath):
	ParCH = ['P0','P1','P2','P3','P4','P5']
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

def remove(filelist):
	for j in filelist:
		with open(j) as infocsv:
		    reader = [i for i in csv.DictReader(infocsv)]
		    if len(reader)>0:
		        print ('not empty')
		    else:
		        print ('empty')
		        os.remove(j)

def prediction(filepath,parameter,option):
	data = pd.read_csv(filepath,skipinitialspace=True)
	print(parameter,option)
	for a in data[parameter]:
		if option == 'Survive':
			data['Prediction'] = 1
			data.to_csv(filepath, index = False)

		if option == 'Died':
			data['Prediction'] = 0
			data.to_csv(filepath, index = False)

		if option == 'Undef':
			data['Prediction'] = 'Undef'
			data.to_csv(filepath, index = False)

############################################################## MAIN PROGRAM ##########################################################
Option = ['Sex','Pclass','Fare','Age','Ticket','Embarked','Cabin','SibSp','Parch']
name = glob.glob('/home/alvinwong/Desktop/AI/Validation/*.csv')

Test = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/test.csv') 
dst = '/home/alvinwong/Desktop/AI/Validation/'
Sex(Test,dst)

Female = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/female.csv') 
Cabin(Female,dst)

########################################## MALE ######################################################################################
Male = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/male.csv') 
Cabin(Male,dst)
############################## Cabin A ################################
CabinA = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Male/CabinA/CabinA.csv') 
SibSp(CabinA,dst)

S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Male/CabinA/S0.csv') 
Parch(S0,dst)

P0 = '/home/alvinwong/Desktop/AI/Validation/Male/CabinA/P0.csv'
prediction(P0,Option[-1],'Survive')

S1 = '/home/alvinwong/Desktop/AI/Validation/Male/CabinA/S1.csv'
prediction(S1,Option[-2],'Survive')

################################ Cabin B ################################
CabinB = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/CabinB.csv') 
Age(CabinB,dst)

Adult = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Adult.csv') 
Fare(Adult,dst)

MF = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Middle_Fare.csv') 
SibSp(MF,dst)

S0 = '/home/alvinwong/Desktop/AI/Validation/Male/CabinB/S0.csv'
prediction(S0,Option[-2],'Survive')

S1= '/home/alvinwong/Desktop/AI/Validation/Male/CabinB/S1.csv'
prediction(S1,Option[-2],'Survive')

Young = '/home/alvinwong/Desktop/AI/Validation/Male/CabinB/Young.csv'
prediction(Young,Option[3],'Survive')

Elderly = '/home/alvinwong/Desktop/AI/Validation/Male/CabinB/Elderly.csv'
prediction(Elderly,Option[3],'Died')

Senior = '/home/alvinwong/Desktop/AI/Validation/Male/CabinB/Senior.csv'
prediction(Senior,Option[3],'Died')

################################ Cabin C ################################
CabinC = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/CabinC.csv') 
Ticket(CabinC,dst)

Digit = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Digit.csv') 
Parch(Digit,dst)

P0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P0.csv') 
Embarked(P0,dst)

S = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S.csv') 
Age(S,dst)

P2 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P2.csv') 
Age(P2,dst)

Adult = '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/Adult.csv'
prediction(Adult,Option[3],'Died')

Alpha= '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/Alpha.csv'
prediction(Alpha,Option[4],'Died')

C = '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/C.csv'
prediction(C,Option[5],'Survive')

P1 = '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/P1.csv'
prediction(P1,Option[-1],'Died')

P2Adult = '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/P2Adult.csv'
prediction(P2Adult,Option[3],'Died')

Senior = '/home/alvinwong/Desktop/AI/Validation/Male/CabinC/Senior.csv'
prediction(Senior,Option[3],'Died')

################################ Cabin D ################################
CabinD= pd.read_csv('/home/alvinwong/Desktop/AI/Validation/CabinD.csv') 
Fare(CabinD,dst)

Middle_Fare = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Middle_Fare.csv') 
Age(Middle_Fare,dst)

Adult = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Adult.csv') 
SibSp(Adult,dst)

S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S0.csv') 
Ticket(S0,dst)

Senior = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Senior.csv') 
Ticket(Senior,dst)

AdAlpha= '/home/alvinwong/Desktop/AI/Validation/Male/CabinD/AdAlpha.csv'
prediction(AdAlpha,Option[4],'Survive')

Elderly = '/home/alvinwong/Desktop/AI/Validation/Male/CabinD/Elderly.csv'
prediction(Elderly,Option[3],'Died')

Unknown = '/home/alvinwong/Desktop/AI/Validation/Male/CabinD/Unknown.csv'
prediction(Unknown,Option[3],'Died')

Young = '/home/alvinwong/Desktop/AI/Validation/Male/CabinD/Young.csv'
prediction(Young,Option[3],'Died')

SeDigit = '/home/alvinwong/Desktop/AI/Validation/Male/CabinD/SeDigit.csv'
prediction(SeDigit,Option[4],'Died')

################################ Cabin E ################################
CabinE= pd.read_csv('/home/alvinwong/Desktop/AI/Validation/CabinE.csv') 
Age(CabinE,dst)

Senior = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Senior.csv') 
SibSp(Senior,dst)

S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S0.csv') 
Ticket(S0,dst)

Adult= '/home/alvinwong/Desktop/AI/Validation/Male/CabinE/Adult.csv'
prediction(Adult,Option[3],'Survive')

Digit = '/home/alvinwong/Desktop/AI/Validation/Male/CabinE/Digit.csv'
prediction(Digit,Option[4],'Died')

Unknown = '/home/alvinwong/Desktop/AI/Validation/Male/CabinE/Unknown.csv'
prediction(Unknown,Option[3],'Undef')

Young = '/home/alvinwong/Desktop/AI/Validation/Male/CabinE/Young.csv'
prediction(Young,Option[3],'Survive')

S1 = '/home/alvinwong/Desktop/AI/Validation/Male/CabinE/S1.csv'
prediction(S1,Option[-2],'Died')


################################ Cabin F ################################
CabinF = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/CabinF.csv') 
Fare(CabinF,dst)

Low_Fare= '/home/alvinwong/Desktop/AI/Validation/Male/CabinF/Low_Fare.csv'
prediction(Low_Fare,Option[2],'Died')

Middle_Fare = '/home/alvinwong/Desktop/AI/Validation/Male/CabinF/Middle_Fare.csv'
prediction(Middle_Fare,Option[2],'Survive')

################################ Cabin Missing ################################
Missing = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Missing.csv') 
Parch(Missing,dst)

P2 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P2.csv') 
Age(P2,dst)

Young = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Young.csv') 
SibSp(Young,dst)
Adult= '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Adult.csv'
prediction(Adult,Option[3],'Died')
Senior = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Senior.csv'
prediction(Senior,Option[3],'Died')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Unknown.csv'
prediction(Unknown,Option[3],'Died')

P2S0 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P2S0.csv'
prediction(P2S0,Option[-2],'Survive')
P2S2 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P2S2.csv'
prediction(P2S2,Option[-2],'Undef')
P2S4 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P2S4.csv'
prediction(P2S4,Option[-2],'Died')
P2S5 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P2S5.csv'
prediction(P2S5,Option[-2],'Died')

P5 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P5.csv'
prediction(P5,Option[-1],'Died')

################################ SUB _SECTION #####################################
P1 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P1.csv') 
Age(P1,dst)

Young = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Young.csv') 
SibSp(Young,dst)

S1 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S1.csv') 
Fare(S1,dst)

Adult= '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Adult.csv'
prediction(Adult,Option[3],'Died')
Senior = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Senior.csv'
prediction(Senior,Option[3],'Died')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Unknown.csv'
prediction(Unknown,Option[3],'Survive')

P1S0 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P1S0.csv'
prediction(P1S0,Option[-2],'Survive')
P1S3 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P1S3.csv'
prediction(P1S3,Option[-2],'Died')
P1S4 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P1S4.csv'
prediction(P1S4,Option[-2],'Died')

Middle_Fare = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Middle_Fare.csv'
prediction(Middle_Fare,Option[2],'Survive')
################################# SUB _SECTION #####################################
P0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P0.csv') 
Pclass(P0,dst)

Pclass2 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Pclass2.csv'
prediction(Pclass2,Option[1],'Died')

################################ SUB Section ########################################
Pclass1 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Pclass1.csv') 
SibSp(Pclass1,dst)

P0S0 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P0S0.csv'
prediction(P0S0,Option[-2],'Died')
P0S1 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P0S1.csv'
prediction(P0S1,Option[-2],'Died')


################################# SUB Section ########################################
Pclass3 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Pclass3.csv') 
Fare(Pclass3,dst)

Low_Fare = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Low_Fare.csv') 
SibSp(Low_Fare,dst)

S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S0.csv') 
Age(S0,dst)

Adult = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Adult.csv') 
Ticket(Adult,dst)

Young = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Young.csv'
prediction(Young,Option[3],'Died')
Senior = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Senior.csv'
prediction(Senior,Option[3],'Died')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Unknown.csv'
prediction(Unknown,Option[3],'Died')

P0P3S1 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P0P3S1.csv'
prediction(P0P3S1,Option[-2],'Died')
P0P3S2 = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/P0P3S2.csv'
prediction(P0P3S2,Option[-2],'Died')

Alpha = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Alpha.csv'
prediction(Alpha,Option[4],'Died')
Digit = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Digit.csv'
prediction(Digit,Option[4],'Died')

Middle_Fare = '/home/alvinwong/Desktop/AI/Validation/Male/Missing/Middle_Fare.csv'
prediction(Middle_Fare,Option[2],'Died')

########################################## FEMALE ######################################################################################
Female = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/female.csv') 
Pclass(Female,dst)

##################################### Pclass 1 ##########################################
Pclass1 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Pclass1.csv') 
Age(Pclass1,dst)

Young = '/home/alvinwong/Desktop/AI/Validation/Female/Young.csv'
prediction(Young,Option[3],'Survive')
Senior = '/home/alvinwong/Desktop/AI/Validation/Female/Senior.csv'
prediction(Senior,Option[3],'Survive')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Female/Unknown.csv'
prediction(Unknown,Option[3],'Undef')
Adult= '/home/alvinwong/Desktop/AI/Validation/Female/Adult.csv'
prediction(Adult,Option[3],'Survive')
Elderly = '/home/alvinwong/Desktop/AI/Validation/Female/Elderly.csv'
prediction(Elderly,Option[3],'Survive')

##################################### Pclass 2 ##########################################
Pclass2 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Pclass2.csv') 
Age(Pclass2,dst)

Young = '/home/alvinwong/Desktop/AI/Validation/Female/Young.csv'
prediction(Young,Option[3],'Survive')
Senior = '/home/alvinwong/Desktop/AI/Validation/Female/Senior.csv'
prediction(Senior,Option[3],'Survive')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Female/Unknown.csv'
prediction(Unknown,Option[3],'Survive')
Adult= '/home/alvinwong/Desktop/AI/Validation/Female/Adult.csv'
prediction(Adult,Option[3],'Survive')

##################################### Pclass 3 ##########################################
Pclass3 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Pclass3.csv') 
Embarked(Pclass3,dst)

S = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S.csv') 
Age(S,dst)
############################# 1st SUB SECTION ##################################
Young = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Young.csv') 
SibSp(Young,dst)

S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S0.csv') 
Cabin(S0,dst)

Missing = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Missing.csv') 
Parch(Missing,dst)

P0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P0.csv') 
Fare(P0,dst)

Senior = '/home/alvinwong/Desktop/AI/Validation/Female/Senior.csv'
prediction(Senior,Option[3],'Died')
Unknown = '/home/alvinwong/Desktop/AI/Validation/Female/Unknown.csv'
prediction(Unknown,Option[3],'Died')

Low_Fare = '/home/alvinwong/Desktop/AI/Validation/Female/Low_Fare.csv'
prediction(Low_Fare,Option[2],'Died')

S1 = '/home/alvinwong/Desktop/AI/Validation/Female/S1.csv'
prediction(S1,Option[-2],'Survive')
S5 = '/home/alvinwong/Desktop/AI/Validation/Female/S5.csv'
prediction(S5,Option[-2],'Died')

P1 = '/home/alvinwong/Desktop/AI/Validation/Female/P1.csv'
prediction(P1,Option[-1],'Survive')

############################# 2nd SUB SECTION ##################################
Adult = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Adult.csv') 
SibSp(Adult,dst)

S1 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S1.csv') 
Fare(S1,dst)

Middle_Fare = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Middle_Fare.csv') 
Cabin(Middle_Fare,dst)

Missing = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Missing.csv') 
Ticket(Missing,dst)

S2 = '/home/alvinwong/Desktop/AI/Validation/Female/S2.csv'
prediction(S2,Option[-2],'Died')
S4 = '/home/alvinwong/Desktop/AI/Validation/Female/S4.csv'
prediction(S4,Option[-2],'Undef')


Low_Fare = '/home/alvinwong/Desktop/AI/Validation/Female/Low_Fare.csv'
prediction(Low_Fare,Option[2],'Died')

Alpha = '/home/alvinwong/Desktop/AI/Validation/Female/Alpha.csv'
prediction(Alpha,Option[4],'Survive')
Digit = '/home/alvinwong/Desktop/AI/Validation/Female/Digit.csv'
prediction(Digit,Option[4],'Died')

############################# 3RD SUB SECTION ####################################
S0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/S0.csv') 
Parch(S0,dst)

P0 = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/P0.csv') 
Ticket(P0,dst)

Alpha = '/home/alvinwong/Desktop/AI/Validation/Female/Alpha.csv'
prediction(Alpha,Option[4],'Survive')
Digit = '/home/alvinwong/Desktop/AI/Validation/Female/Digit.csv'
prediction(Digit,Option[4],'Died')

P2 = '/home/alvinwong/Desktop/AI/Validation/Female/P2.csv'
prediction(P2,Option[-1],'Survive')

###################################### Embarked C/Q  ##########################################
C = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/C.csv') 
Fare(C,dst)

Q = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/Q.csv') 
Parch(Q,dst)

P0 = '/home/alvinwong/Desktop/AI/Validation/Female/P0.csv'
prediction(P0,Option[-1],'Survive')
Low_Fare = '/home/alvinwong/Desktop/AI/Validation/Female/Low_Fare.csv'
prediction(Low_Fare,Option[2],'Died')
Middle_Fare = '/home/alvinwong/Desktop/AI/Validation/Female/Middle_Fare.csv'
prediction(Middle_Fare,Option[2],'Died')
##################################### MERGING ALL CSV BACK INTO ONE ##################################################################
os.chdir('/home/alvinwong/Desktop/AI/Validation')
merge = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("*")):
    namedf = pd.read_csv(file)
    print(namedf)
    if 'Prediction' in namedf:
    	merge = merge.append(namedf)
 
merge.to_csv('/home/alvinwong/Desktop/AI/Validation/PredictedTestResult.csv')

########################Classifying Undef Output Prediction #################################################

filelist = pd.read_csv('/home/alvinwong/Desktop/AI/Validation/PredictedTestResult.csv')

Survive,Die,Undef = (0 for i in range(3))
for i in filelist['Prediction']:
	if i == '1':
		Survive+=1
	elif i == '0':
		Die+=1
	elif i == 'Undef':
		Undef+=1

Total = Undef+Survive+Die

print('Total = {}, Undefined = {}, Survive = {}, Die = {}.'.format(Total,Undef,Survive,Die))


trainlist = pd.read_csv('/home/alvinwong/Desktop/AI/TrainClassification/train.csv')

a,b,c,d = (0 for i in range(4))
for i,j in zip(trainlist['Survived'],trainlist['Sex']):
		if i == 1 and j == 'male':
			a+=1
		elif i == 0 and j == 'male':
			b+=1
		elif i == 0 and j == 'female':
			c+=1
		elif i == 1 and j == 'female':
			d+=1

print('MaleSurvive = {}, MaleDie = {}, FemaleSurvive = {}, FemaleDie = {}.'.format(a,b,d,c))

############################################### Assignment Part (f) ###################################################
df = pd.read_csv('/home/alvinwong/Desktop/PredictedTestResult (FINAL).csv')

female,survive,young,single,P1,P2,P3,S,Q,C = (0 for i in range(10))

for i,j in zip(df['Prediction'],df['Sex']):
	if i == '1' and j == 'female':
		female+=1
	if i == '1':
		survive+=1

for i,j in zip(df['Prediction'],df['Age']):
	if i == '1' and j < 18:
		young+=1

for i,j,k in zip(df['Prediction'],df['Parch'],df['SibSp']):
	if i == '1' and j  == 0 and k == 0:
		single+=1

for i,j in zip(df['Prediction'],df['Pclass']):
	if i == '1' and j == 1:
		P1+=1
	if i == '1' and j == 2:
		P2+=1
	if i == '1' and j == 3:
		P3+=1

for i,j in zip(df['Prediction'],df['Embarked']):
	if i == '1' and j == 'S':
		S+=1
	if i == '1' and j == 'Q':
		C+=1
	if i == '1' and j == 'C':
		Q+=1

print('Amongst the {} survivors, {} are female, {} are below 18yrs, {} are single.'.format(survive,female,young,single))
print('\n')
print('Passenger from Pclass1 that survived are {}'.format(P1))
print('Passenger from Pclass2 that survived are {}'.format(P2))
print('Passenger from Pclass3 that survived are {}'.format(P3))
print('\n')
print('Passenger from loading from S that survived are {}'.format(S))
print('Passenger from loading from C that survived are {}'.format(C))
print('Passenger from loading from Q that survived are {}'.format(Q))