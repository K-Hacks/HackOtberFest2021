import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
weather=pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv')
print(weather[:12])
#weather.plot(x="Month",y="Tmax",figsize=(8,5),color='Red',grid=True)
#weather.plot(x="Month",y="Tmax",figsize=(8,5),color='Red',grid=True,xticks=np.arange(0,30,5),yticks=(1,30,5),xlim=[0,40],ylim=[0,100])
#plt.axis([0,27,0,15])
weather.plot(x="Month",y="Tmax",figsize=(8,5),color='Red',grid=True)
#plt.xlim([0,40])
#plt.ylim([0,100])
plt.show()

