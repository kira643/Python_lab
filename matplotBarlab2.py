#1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion.
#Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
# Monthly expenses in dollars (replace with your own data)
#expenses = [1200, 400, 200, 150, 250]

#import requried library
import matplotlib.pyplot as plt

#  Given Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Plotting the bar chart
plt.bar(categories, expenses,color='purple', edgecolor='black')

#add labels and title
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses')

#show the plot
plt.show()

