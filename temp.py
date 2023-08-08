import pandas as pd
import numpy as np

df = pd.read_csv("NLI_students.csv")

#-----------merge first and last name-------------
l_name = df['Last Name'].values.tolist()
f_name = df['First Name'].values.tolist()

fullname = [] # merged firstname and lastname
for i in range(len(f_name)):
	temp = f_name[i] + " " + l_name[i]
	fullname.append(temp)
#---------have put all names in a dictionary to remove duplicates-----------
name = {} 
for i in fullname:
	if i in name:
		name[i] += 1
	else:
		name[i] = 1
#----------store duplicate names-----------------------------------------------
print('Duplicate data\n')
dupname= []  
for k,v in name.items():
	if v>1:
		dupname.append(k)
		#print(k)
print(len(fullname))
print(len(name))
#------------------------------------------------------------------------

df['Fullname'] = fullname		
data = df.drop_duplicates(subset = ['Fullname','Email'])

#-------get names of students who have taken multiple courses--------------
print('\n\nStudents who have taken different Activity\n')
res = []
for i in range(len(fullname)):
	hehe = []
	hehe.append(df['Fullname'][i])
	hehe.append(df['ActivityName'][i])
	res.append(hehe)

for i in range(len(res)):
	for j in range(i,len(res)):
		if res[i][0] == res[j][0] and res[i][1] != res[j][1]:
			pass
			print (res[i])
			#print (res[j])
#----------------------------------------------------------------------------
del data['Fullname']
data = pd.DataFrame(data)
data.to_csv('NLI_students_updated1.csv')


#-------------------------------------------------------------------------
# filter using emails-------------------

email = df['Email'].values.tolist()

email_dic= {} 
for i in email:
	if i in name:
		email_dic[i] += 1
	else:
		email_dic[i] = 1
print (len(email_dic))
