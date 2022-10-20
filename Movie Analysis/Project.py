#Part 1
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

    
while True:
#Part 2
    print('***********************************')
    print('MOVIE REVENUE ANAlYSIS')
    print('***********************************')
    print('')
    print('MENU')
    print('')
    print('Read Data From File')
    print('1. Read complete csv file')
    print('========================')
    print('Data Visualization')
    print('2. Line Chart')
    print('3. Bar Plot')
    print('========================')
    print('Apply Data Manipulation in the records of CSV file')
    print('4. Sorting the data as per Reveue')
    print('5. Read Records from file as per requirement')
    print('6. Read Records from file as per requirement and make a copy as CSV file')
    print('7. Sort the Data based on Genre')
    print('8. Sort the Data based on Release Year')
    user_input=int(input('Choose any option between 1 and 8: '))
    df1=pd.read_csv('Part1.csv')
    
    

#Part 3
    if user_input==1:
        print(df1)
        
    elif user_input==2:
        df_x=df1['title']
        df_y=df1['worldwide_gross']
        plt.plot(df_x,df_y,marker="*",markerfacecolor='red')
        plt.xlabel('Movie Name')
        plt.ylabel('Revenue (in billions)')
        plt.title('Movies and their Revenues')
        plt.show()
        
    elif user_input==3:
        df_y=df1['title']
        df_x=df1['worldwide_gross']
        plt.bar(df_y,df_x,color='purple')
        plt.xlabel('Movie Name')
        plt.ylabel('Revenue (in billions)')
        plt.title('Movies and their Revenues')
        plt.show()
        
    elif user_input==4:
        print('The values can be printed in Descending Order')
        df1.sort_values('worldwide_gross')
        print(df1)
        
    elif user_input==5:
        print(df1)
        df_start=int(input('Select an Value between 1 and 8: '))
        df_end=int(input('Select an Value between 1 and 8: '))
        if df_end<df_start:
            print('Sorry, Error in Input')
            exit()
        elif df_end>df_start:
            df_start=df_start-1
            list1=[]
            list2=[]
            for i in range(df_start,df_end):
                df=pd.DataFrame()
                newdata=df1.iloc[i]
                list1.append(newdata['title'])
                list2.append(newdata['worldwide_gross'])
        dict1={'Movie':list1,'Worldwide Gross':list2}
        df=pd.DataFrame(dict1)
        print('The DataFrame made from the Requested data is shown below')
        print(df)
        
    elif user_input==6:
        print(df1)
        df_start=int(input('Select an Value between 1 and 8: '))
        df_end=int(input('Select an Value between 1 and 8: '))
        if df_end<df_start:
            print('Sorry, Error in Input')
            exit()
        elif df_end>df_start:
            df_start=df_start-1
            list1=[]
            list2=[]
            for i in range(df_start,df_end):
                df=pd.DataFrame()
                newdata=df1.iloc[i]
                list1.append(newdata['title'])
                list2.append(newdata['worldwide_gross'])
        dict1={'Movie':list1,'Worldwide Gross':list2}
        df=pd.DataFrame(dict1)
        print('The DataFrame made from the Requested data is shown below')
        print(df)
        user_newin=str(input('Would you like to export this Data? (Y/N): '))
        if user_newin in ['Y','y']:
            df.to_csv(r'Export CSV\User Export.csv', index = False, header=True)
            print('The file is exported to a folder named "Export CSV" in the same root folder as this program')
        elif user_newin in ['N','n']:
            print('Export Cancelled')
        elif user_newin not in ['Y','y','N','n']:
            print('Wrong Input')
            exit()
            
    elif user_input==7:
        print(df1.sort_values('genre'))
    
    elif user_input==8:
        print(df1.sort_values('release_year'))
    
    elif user_input not in range(1,9):
        print('Wrong Option')
    

