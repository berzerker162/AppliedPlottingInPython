
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Reno, Nevada, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Reno, Nevada, United States** to Ann Arbor, USA. In that case at least one source file must be about **Reno, Nevada, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Reno, Nevada, United States** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[31]:

#Question: How does the climate of Reno, NV compare to the climate of Miami, FL?

#Data
#https://www.usclimatedata.com/climate/reno/nevada/united-states/usnv0076
#https://www.usclimatedata.com/climate/miami/florida/united-states/usfl0316


#get data
#month, avg high, avg low, avg rainfall, avg humidity
#Is there a comfortable human range? https://library.wmo.int/doc_num.php?explnum_id=8822

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read dataset

df = pd.read_csv('weather_data.csv').dropna(axis=1, how='all')

y_temp_reno_h = df[df['City']=='Reno']['High']
y_temp_reno_l = df[df['City']=='Reno']['Low']

y_temp_miami_h = df[df['City']=='Miami']['High']
y_temp_miami_l = df[df['City']=='Miami']['Low']

y_temp_reno_precip = df[df['City']=='Reno']['Precip']

y_temp_miami_precip = df[df['City']=='Miami']['Precip']

y_sun_reno = df[df['City']=='Reno']['Sun Hours']
y_sun_miami = df[df['City']=='Miami']['Sun Hours']

x = [0,1,2,3,4,5,6,7,8,9,10,11]
x_months = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']



# In[43]:

#plot
f= plt.figure()

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, sharex=True,figsize=(20,20))
fig.suptitle('Comparison of Climates Between Reno, NV and Miami, FL', fontsize=25)
plt.xticks(x,x_months)


#=========Highs=========
ax1.plot(x,y_temp_reno_h, color = 'black')

ax1.set_title('High Temp Avg (°F)',fontsize=20)

ax1.set_ylim([20,100])

ax1.plot(x,y_temp_miami_h, color = 'grey',linestyle=':')

ax1.fill_between(x, y_temp_miami_h, y_temp_reno_h, color = 'red', alpha = 0.1)



#=========Lows=========
ax2.plot(x,y_temp_reno_l, color = 'black')
ax2.set_title('Low Temp Avg (°F)',fontsize=20)
ax2.set_ylim([20,100])

ax2.plot(x,y_temp_miami_l, color = 'grey',linestyle=':')

ax2.fill_between(x, y_temp_miami_l, y_temp_reno_l, color = 'blue', alpha = 0.1)

#=========Sun=========

ax3.plot(x,y_sun_reno, color='black')
ax3.set_title('Sunshine Avg (hrs)',fontsize=20)
ax3.set_ylim([100,500])

ax3.plot(x,y_sun_miami, color = 'grey',linestyle=':')

ax3.fill_between(x, y_sun_miami, y_sun_reno, color = 'yellow', alpha = 0.1)

#=========Rain=========

#ax1.plot(x,y_temp_reno_h)
ax4.plot(x,y_temp_reno_precip, color='black')
#ax4.set_title('Reno')
ax4.set_title('Precip Avg (in)',fontsize=20)
ax4.set_ylim([0,15])

ax4.fill_between(x, y_temp_miami_precip, y_temp_reno_precip, color = 'green', alpha = 0.1)


#legends
L.get_texts()[0].set_text('Reno')
L.get_texts()[1].set_text('Miami')
L = ax2.legend(loc=1)
L.get_texts()[0].set_text('Reno')
L.get_texts()[1].set_text('Miami')
L = ax3.legend(loc=1)
L.get_texts()[0].set_text('Reno')
L.get_texts()[1].set_text('Miami')
L = ax4.legend(loc=1)
L.get_texts()[0].set_text('Reno')
L.get_texts()[1].set_text('Miami')


plt.show()
plt.savefig('climate_comparison.png')

