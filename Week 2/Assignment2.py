
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[82]:

from datetime import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv', 
                parse_dates=['Date'])

#create a day of year column
df.loc[0,'Date'].strftime('%j')

df['Day'] = df['Date'].apply(lambda x: x.strftime('%j'))

#create month of year column
df['Month'] = df['Date'].apply(lambda x: x.strftime('%b'))

#create month of year column
df['Year'] = df['Date'].apply(lambda x: x.strftime('%Y'))

df['Year'] = df['Year'].astype(int)


#convert from tenths to deg celcius
df['Data_Value'] = df['Data_Value'] / 10

#get just 2005-2014
df_base = df[df['Year'] < 2015]
df_2015 = df[df['Year'] == 2015]

#create data series for days and high/low temps
df_extreme = df_base.groupby(['Day','Month'])['Data_Value'].agg([np.max, np.min])
df_extreme.reset_index(inplace=True)

x = df_extreme['Day'].astype(int)
y1 = df_extreme['amax'].astype(int)
y2 = df_extreme['amin'].astype(int)

#find dates where record occured in 2015

#join 10 yr records and 2015 and check if high is higher, low is lower
df_2015_records = pd.merge(df_extreme, df_2015, how='inner', on='Day')


df_2015_records['Is High'] = df_2015_records['amax'] < df_2015_records['Data_Value']
df_2015_records['Is Low'] = df_2015_records['amin'] > df_2015_records['Data_Value']

df_2015_records = df_2015_records.groupby(['Day','Is High','Is Low'])['Data_Value'].agg([np.max, np.min])

df_2015_records.reset_index(inplace=True)

records_high = df_2015_records[(df_2015_records['Is High'] == True)]
records_low = df_2015_records[(df_2015_records['Is Low'] == True)]


x_2015_high = records_high['Day'].astype(int)
x_2015_low = records_low['Day'].astype(int)

y_2015_high = records_high['amax'].astype(int)
y_2015_low = records_low['amin'].astype(int)

#plots
plt.figure(figsize=(20,10))

#plot
plt.box(False)
plt.plot(x, y1, color = 'red')
plt.plot(x, y2, color = 'blue')

#shade between high/low
plt.fill_between(x, y1, y2, color = 'grey', alpha = 0.1)

#lables
plt.title('10 Year Daily Record Temperatures\nw/ 2015 Record Breaking Temps\n(°C, 2005 - 2014)')
plt.xlabel('Day of Year')
plt.ylabel('°C')

#layer on 2015 record breaking points
plt.scatter(x_2015_high, y_2015_high, s=50, color='red')
plt.scatter(x_2015_low, y_2015_low, s=50, color='blue')

#add legend
#L = plt.legend()
L = plt.legend(loc=4, frameon=False)
L.get_texts()[0].set_text('Record High (05-14)')
L.get_texts()[1].set_text('Record Low (05-14)')
L.get_texts()[2].set_text('2015 New Record High')
L.get_texts()[3].set_text('2015 New Record Low')


plt.show()
