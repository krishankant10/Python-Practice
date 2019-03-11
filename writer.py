import xlsxwriter
import pandas as pd
df=pd.DataFrame({'x':[1,2,4,3,5,6,7,8,9,2],'y':[9,8,7,6,5,4,3,1,2,4]})
writer=pd.ExcelWriter('pandas.xlsx')
df.to_excel(writer,sheet_name='sheet1')
writer.save()
