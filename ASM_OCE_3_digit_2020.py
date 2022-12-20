import pandas as pd
import csv
import numpy as np
df3=pd.read_csv('Temp_ASM_2020_1.csv')
df4=pd.read_csv('Temp_OES_2020_1.csv')
#print(df3.head(2))
#print(df4.head(0))

#df4['Match']=np.where(df4['Combined2'].isin(df3['Combined1']),df3['EMP']-df4['OES_EMP_Total'],0)
#print(df3.info())
#print(df4.info())

#print(df3['Combined1'].isin(df4['Combined2']))

df3.sort_index(inplace=True)
for ix,i in df4.iterrows():
    for iy,j in df3.iterrows():
        if (i[0:1]==j[0:1]):
            i[ix,'ASM_Total_EMP'].append(j[iy,'EMP'])

df4.to_csv('ASM_OCE_final_data.csv',index=False)

'''
for ix,i in df4.iterrows():
    df2Row = df3[df3['Combined1'] == i['Combined2']]
'''


