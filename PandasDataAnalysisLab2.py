#2.Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.
#Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],
#'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#'age': [12, 12, 13, 13, 14, 12],
#'height': [173, 192, 186, 167, 151, 159],
#'weight': [35, 32, 33, 30, 31, 32],
#'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )


#import requried liabrary
import pandas as pd
import matplotlib.pyplot as plt

#given data dictionary in pandas
student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],
                              'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
                              'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                              'age': [12, 12, 13, 13, 14, 12],
                              'height': [173, 192, 186, 167, 151, 159],
                              'weight': [35, 32, 33, 30, 31, 32],
                              'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']})

# Grouping by 'school_code' and calculating mean, min, and max of 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
#age_stats  = student_data.groupby(['school_code','age']).agg(['mean','min','max'])

# Displaying the result
print("Mean, Min, and Max age for each school code:")
print(age_stats)


age_stats.plot(kind='barh', figsize=(7, 6), color=['violet', 'lightgreen', 'pink'])
plt.xlabel('Number of School Code')
plt.ylabel('School Code')
plt.title('Age Statastics by School Code')
plt.legend()
plt.show()


#Output:
#Mean, Min, and Max age for each school code:
#            mean  min  max
#school_code
#s001         12.5   12   13
#s002         13.0   12   14
#s003         13.0   13   13
#s004         12.0   12   12


#Coclusion:
#From the chart and data:
#School s002 shows a wide range of ages (12 to 14 years), indicating a more diverse age group.
#School s003 has a uniform age of 13 years.
#School s001 has a mean age of 12.5 years, with ages spanning from 12 to 13 years.
#School s004 is the least diverse in age, with all students aged 12 years.