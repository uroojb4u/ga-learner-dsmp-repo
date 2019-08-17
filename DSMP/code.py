# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",", skip_header=1)
census=np.concatenate((data,new_record))
print(data)
print(new_record)
print (census)



# --------------
#Code starts here
age=np.array(census[:,0])
print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
#Code starts here
#a=np.array(census[:,2])
mask = census[:,2]==0
race_0= census[mask]
mask = census[:,2]==1
race_1= census[mask]
mask = census[:,2]==2
race_2= census[mask]
mask = census[:,2]==3
race_3= census[mask]
mask = census[:,2]==4
race_4= census[mask]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print ("0 is", len_0)
print ("1 is", len_1)
print ("2 is", len_2)
print ("3 is", len_3)
print ("4 is", len_4)
minority_race= 3
print ("the minority race is", minority_race)


# --------------
#Code starts here
senior_citizens= census[census[:,0]>60]
#print (senior_citizens)
working_hours_sum= senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print (senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print (avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
print (avg_pay_high)
avg_pay_low=np.mean(low[:,7])
print (avg_pay_low)
print (avg_pay_high>avg_pay_low)


