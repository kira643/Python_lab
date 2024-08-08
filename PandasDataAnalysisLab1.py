#1: Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.Also generate a bar chart based on the result and explain the conclusion.
# Input: student_data = pd.DataFrame({
#'school_code': ['s001','s002','s003','s001','s002','s004'],
#'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
#'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159],
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

# Grouping by 'class' and counting the number of students in each class
class_counts = student_data.groupby('class').size()
print(class_counts)

student_data['class'].value_counts().plot(kind='bar',color='purple',label='Class Counts ')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.title('Number of Students in Each Class')
plt.legend()
plt.show()



#Output:
#class
#V     2
#VI    4
#dtype: int64

#Conclusion:
#From the bar chart, you can visually observe how students are distributed across different classes.
#For example, if Class 'VI' has a taller bar compared to Class 'V', it indicates that there are more students in Class 'VI' than in Class 'V'.
# This kind of visualization helps in quickly assessing the distribution of students among different classes.