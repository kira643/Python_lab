#2.Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time. You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.
#Input: months = np.arange(1, 13)
#electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
#clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
#home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
#sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

#import requried liabray
import matplotlib.pyplot as plt
import numpy as np

#given input for subplot chart
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create a figure and a set of subplots
fig, axs = plt.subplots(2,2, figsize=(12,8))

#first subplot - electronics_sales
axs[0,0].plot(months,electronics_sales,marker='o',color='purple')
axs[0,0].set_title('Electronics Sales Data')
axs[0,0].set_xlabel('Months')
axs[0,0].set_ylabel('Electronics Sales')

#second subplot - clothing_sales
axs[0,1].plot(months,clothing_sales,marker='o',color='black')
axs[0,1].set_title('Clothing Sales Data')
axs[0,1].set_xlabel('Months')
axs[0,1].set_ylabel('Clothing Sales')

#third subplot - home_garden_sales
axs[1,0].plot(months,home_garden_sales,marker='o',color='green')
axs[1,0].set_title('Home Garden Sales Data')
axs[1,0].set_xlabel('Months')
axs[1,0].set_ylabel('Home Garden Sales')

#fourth subplot - sports_outdoors_sales
axs[1,1].plot(months,sports_outdoors_sales,marker='o',color='red')
axs[1,1].set_title('Sports Outdoors Sales Data')
axs[1,1].set_xlabel('Months')
axs[1,1].set_ylabel('Sports Outdoors Sales')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()