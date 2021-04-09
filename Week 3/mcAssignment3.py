
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


# In[69]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt

#get means 
mean_92 = df.loc[1992].mean()
mean_93 = df.loc[1993].mean()
mean_94 = df.loc[1994].mean()
mean_95 = df.loc[1995].mean()

#get standard error of the means
se_92 = df.loc[1992].std() / np.sqrt(len(df.loc[1992]))
se_93 = df.loc[1993].std() / np.sqrt(len(df.loc[1993]))
se_94 = df.loc[1994].std() / np.sqrt(len(df.loc[1994]))
se_95 = df.loc[1995].std() / np.sqrt(len(df.loc[1995]))



#points to plot
x = np.array([1992, 1993, 1994,1995])
y = np.array([mean_92, mean_93, mean_94, mean_95])
error = np.array([se_92, se_93, se_94, se_95])

#confidence intervals
y_max = np.add(y,error)
y_min = np.subtract(y,error)


# In[71]:

global reference
reference = 42000

#color masks for plot
mask_within = (reference <= y_max) & (reference >= y_min)
mask_above = reference > y_max
mask_below = reference < y_min


#plot points
plt.bar(x, y, yerr=error, capsize=3)

#plot colors based on y-axis reference versus bar error ranges
plt.bar(x[mask_within],y[mask_within], edgecolor= 'black', color='white')
plt.bar(x[mask_above], y[mask_above], edgecolor= 'black', color='red')
plt.bar(x[mask_below], y[mask_below], edgecolor= 'black', color='blue')

plt.xticks(x)

#plot reference line
plt.axhline(y=reference, color = 'black', linestyle='--')

plt.legend(['reference','above range','within range', 'below range'], loc=4)
plt.box(on=None)

plt.show()

#get user click for reference line and redraw plot with appropriate colors
def onclick(event):
    plt.clf()
    reference = event.ydata
    #color masks for plot

    mask_within = (reference <= y_max) & (reference >= y_min)
    mask_above = reference > y_max
    mask_below = reference < y_min


    #plot points
    plt.bar(x, y, yerr=error, capsize=3)

    #plot colors based on y-axis reference versus bar error ranges
    plt.bar(x[mask_within],y[mask_within], edgecolor= 'black', color='white')
    plt.bar(x[mask_above], y[mask_above], edgecolor= 'black', color='red')
    plt.bar(x[mask_below], y[mask_below], edgecolor= 'black', color='blue')

    plt.xticks(x)

    #plot reference line
    #plt.plot(x, np.repeat(reference, len(x)))
    plt.axhline(y=reference, color = 'black', linestyle='--')

    plt.legend(['reference','above range','within range', 'below range'], loc=4)
    plt.box(on=None)

    plt.show()


# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

