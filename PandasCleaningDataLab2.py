#2.Write a Pandas program to drop those rows from a given DataFrame in which specific columns have missing values. Input: df = pd.DataFrame({ 'ord_no':[np.nan,np.nan,70002,np.nan,np.nan,70005,np.nan,70010,70003,70012,np.n an,np.nan], '
#purch_amt':[np.nan,270.65,65.26,np.nan,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,np.nan],
#'ord_date': [np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10- 10','2012-10-10','2012-06-27','2012-08-17',np.nan],
#'customer_id':[np.nan,3001,3001,np.nan,3002,3001,3001,3004,3003,3002,3001,np.na n]})

#import requried liabrary
import pandas as pd
import numpy as np

#given data dictionary in pandas
df = pd.DataFrame({ 'ord_no':[np.nan,np.nan,70002,np.nan,np.nan,70005,np.nan,70010,70003,70012,np.nan,np.nan],
                    'purch_amt':[np.nan,270.65,65.26,np.nan,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,np.nan],
                    'ord_date': [np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10- 10','2012-10-10','2012-06-27','2012-08-17',np.nan],
                    'customer_id':[np.nan,3001,3001,np.nan,3002,3001,3001,3004,3003,3002,3001,np.nan]})

#print the dataframe
df=pd.DataFrame(df)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

#drop the missing values
df_drop= df.dropna()

# Display the DataFrame after dropping the rows
print("\nDataFrame after dropping rows with missing values:")
print(df_drop)


#output:
#Original DataFrame:
#    ord_no  purch_amt     ord_date  customer_id
#0       NaN        NaN          NaN          NaN
#1       NaN     270.65   2012-09-10       3001.0
#2   70002.0      65.26          NaN       3001.0
#3       NaN        NaN          NaN          NaN
#4       NaN     948.50   2012-09-10       3002.0
#5   70005.0    2400.60   2012-07-27       3001.0
#6       NaN    5760.00   2012-09-10       3001.0
#7   70010.0    1983.43  2012-10- 10       3004.0
#8   70003.0    2480.40   2012-10-10       3003.0
#9   70012.0     250.45   2012-06-27       3002.0
#10      NaN      75.29   2012-08-17       3001.0
#11      NaN        NaN          NaN          NaN

#DataFrame after dropping rows with missing values:
    #ord_no  purch_amt     ord_date  customer_id
#5  70005.0    2400.60   2012-07-27       3001.0
#7  70010.0    1983.43  2012-10- 10       3004.0
#8  70003.0    2480.40   2012-10-10       3003.0
#9  70012.0     250.45   2012-06-27       3002.0
