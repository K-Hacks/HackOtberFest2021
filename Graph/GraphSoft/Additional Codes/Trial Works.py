#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pylab as pylab
import matplotlib.axes as Axs
#Importing the Necessary Data
google_csv=pd.read_csv("D:\Ajmal\Project\Google 2012-20.csv")
yahoo_csv=pd.read_csv("D:\Ajmal\Project\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("D:\Ajmal\Project\wNetflix 2012-20.csv")

#Imported Data (Run these Codes only to check if working or not)
print(google_csv)
print(yahoo_csv)
print(netflix_csv)

#Defining a Dictionary for the Years specified in DataFrames
id_dict={2012:0,2013:1,2014:2,2015:3,2016:4,2017:5,2018:6,2019:7}

#Getting Input from User
Start_Year=int(input("Choose an Year (between 2012-2019): "))
End_Year=int(input("Choose an Year (between 2012-2019): "))

#Applying the Input Command on the Dictionary
x_start=int(id_dict[Start_Year])
x_end=int(id_dict[End_Year])+1

#Creating New DataFrames based on User input
mod_gcsv=google_csv[x_start:x_end]
mod_ycsv=yahoo_csv[x_start:x_end]
mod_ncsv=netflix_csv[x_start:x_end]

#plt.plot(google_csv['Year'],googl_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])

#fig = pylab.figure()    
#ax = fig.add_subplot(1,1,1)
#ax.yaxis.grid(color='gray', linestyle='dashed')

#plotting new graphs based on user requirements

plt.suptitle('Revenue over Years Graph')
plt.subplot(2,1,1)
plt.title('Overall Graph')
plt.plot(google_csv['Year'],google_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])
plt.subplot(2,1,2)
plt.title('Graph Based on User Request')
plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],mod_ycsv['Year'],mod_ycsv['Revenue'],mod_ncsv['Year'],mod_ncsv['Revenue'])
plt.show()
