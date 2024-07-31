
#2.Visualize the daily temperature changes over time in a city and give your conclusion
#Input: days = list(range(1, 32))
# Daily temperature data (replace with your own data)
#temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]


#import requried library
import matplotlib.pyplot as plt

#  Given Data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Plotting the bar chart
plt.plot(days, temperature,marker='o',color="purple")
#add labels and title
plt.title('Daily Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature')

#show the plot
plt.show()