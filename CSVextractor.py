# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:21:19 2024

@author: User
"""

import pandas as pd
from dtstruct import struct

#Get file
data = pd.read_csv('Comfort_Database.csv')


#Return struct
def getData(country1, country2):
    myObj = struct(country1, country1)
    selectIndex = data.index.get_loc(data[data['Countries'] == myObj.country1].index[0])
    selectIndex2  = data.index.get_loc(data[data['Countries'] == myObj.country2].index[0])
    
    
    #Iterate and get each stat for each colmn (bar first column)
    for i in range (1, len(data.columns)):
        myObj.fieldnames.append(data.columns[i])
        myObj.c1stats.append(data.loc[selectIndex, [data.columns[i]]].item())
        myObj.c2stats.append(data.loc[selectIndex, [data.columns[i]]].item())
        #percentage = (data.loc[selectIndex, [data.columns[i]]].item() / data.loc[selectIndex2, [data.columns[i]]].item())* 100
    return myObj