from operator import le
import pandas as pd
import csv
import openpyxl
from openpyxl import load_workbook

path = r"C:\Users\vimmadisetty\Desktop\Gini_Results"
book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

df1=pd.read_csv('ASM_3digit_NAICS_Specificed_units_for_all_states_from_2010_to_2020.csv')

NAICS_Title=['Food manufacturing','Beverage and tobacco product manufacturing','Textile mills','Textile product mills','Apparel manufacturing','Leather and allied product manufacturing','Wood product manufacturing','Paper manufacturing','Printing and related support activities','Petroleum and coal products manufacturing','Chemical manufacturing','Plastics and rubber products manufacturing','Nonmetallic mineral product manufacturing','Primary metal manufacturing','Fabricated metal product manufacturing','Machinery manufacturing','Computer and electronic product manufacturing','Electrical equipment  appliance and component manufacturing','Transportation equipment manufacturing','Furniture and related product manufacturing','Miscellaneous manufacturing']
#NICS_Code=['311','312','313','314','315','316','321','322','323','324','325','326','327','331','332','333','334','335','336','337','339']
Year=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

for i in NAICS_Title:

    for j in Year:
        a=df1.groupby('NAICS_TTL')
        df1_text=df1[df1['NAICS_TTL']=='{i}']
        b=df1_text[['NAICS_TTL','GEO_TTL','NAICS','2020']]
        b['Cumulative nomalized rank of income']=''
        b=b.sort_values(by='{j}',ascending=True)
        b.reset_index(drop=True,inplace=True)
        b.iat[0,b.columns.get_loc('Cumulative nomalized rank of income')]=1/51
        for i in range(1,len(b)):
            b.loc[i,'Cumulative nomalized rank of income']=b.loc[i-1,'Cumulative nomalized rank of income']+1/51
        sum_year=b['{j}'].sum()
        b['Lorenz_Curve_2020']=''
        b.iat[0,b.columns.get_loc('Lorenz_Curve_{j}')]=b.loc[0,'{j}']/sum_year
        for i in range(1,len(b)):
            b.loc[i,'Lorenz_Curve_{j}']=b.loc[i-1,'Lorenz_Curve_{j}']+(b.loc[i,'{j}']/sum_year)
        b['Perfect equality Line Area- {j} [A+B]']=b['Cumulative nomalized rank of income']
        b['Area Under the Lorenz curve {j} [B]']=''
        b.iat[0,b.columns.get_loc('Area Under the Lorenz curve {j} [B]')]=(0.5*b.iat[0,b.columns.get_loc('Lorenz_Curve_{j}')])/51
        for i in range(1,len(b)):
            b.loc[i,'Area Under the Lorenz curve {j} [B]']=(0.5*(b.loc[i,'Lorenz_Curve_{j}']-b.loc[i-1,'Lorenz_Curve_{j}'])+b.loc[i-1,'Lorenz_Curve_{j}'])/51
        b['Area between Lorenz and Perfect equality {j}[A]']=b['Perfect equality Line Area- {j} [A+B]']-b['Area Under the Lorenz curve {j} [B]']
        count=0
        for i in range(1,len(b)):
            count=count+b.loc[i,'Area Under the Lorenz curve {j} [B]']
        b['GINI Coefficient {j}']=''
        b.iat[0,b.columns.get_loc('GINI Coefficient {j}')]=(0.5-count)/0.5
        b.to_excel(writer,sheet_name='{i}_{j}')
        writer.save()
        writer.close()






        



        '''
	    #df1_Textile_product_mills=df1[df1['NAICS_TTL']=='Miscellaneous manufacturing']
	    #b=df1_Textile_product_mills[['NAICS_TTL','GEO_TTL','NAICS','2020']]
	    #b['Cumulative nomalized rank of income']=''
	    #b=b.sort_values(by='2020',ascending=True)
	    #b.reset_index(drop=True, inplace=True)  # reindexing the dataframe
	    #b.iat[0,b.columns.get_loc('Cumulative nomalized rank of income')]=1/51
	    #for i in range(1,len(b)):
		    #b.loc[i,'Cumulative nomalized rank of income']=b.loc[i-1,'Cumulative nomalized rank of income']+1/51
	    #sum_2020=b['2020'].sum()

	    b['Lorenz_Curve_2020']=''
	    b.iat[0,b.columns.get_loc('Lorenz_Curve_2020')]=b.loc[0,'2020']/sum_2020

	    for i in range(1,len(b)):
		    b.loc[i,'Lorenz_Curve_2020']=b.loc[i-1,'Lorenz_Curve_2020']+(b.loc[i,'2020']/sum_2020)

	    b['Perfect equality Line Area- 2020 [A+B]']=b['Cumulative nomalized rank of income']

	    b['Area Under the Lorenz curve 2020 [B]']=''

	    b.iat[0,b.columns.get_loc('Area Under the Lorenz curve 2020 [B]')]=(0.5*b.iat[0,b.columns.get_loc('Lorenz_Curve_2020')])/51


	    for i in range(1,len(b)):
		    b.loc[i,'Area Under the Lorenz curve 2020 [B]']=(0.5*(b.loc[i,'Lorenz_Curve_2020']-b.loc[i-1,'Lorenz_Curve_2020'])+b.loc[i-1,'Lorenz_Curve_2020'])/51


	    b['Area between Lorenz and Perfect equality 2020[A]']=b['Perfect equality Line Area- 2020 [A+B]']-b['Area Under the Lorenz curve 2020 [B]']


	    count=0
	    for i in range(1,len(b)):
		    count=count+b.loc[i,'Area Under the Lorenz curve 2020 [B]']
	    b['GINI Coefficient 2020']=''

	    b.iat[0,b.columns.get_loc('GINI Coefficient 2020')]=(0.5-count)/0.5
	    b.head()'''


print(df1.head())