import pandas as pd
import xlsxwriter
import numpy
import matplotlib.pyplot as plt
'''df=pd.DataFrame({'x':[1,2,4,3,5,6,7,8,9,2],'y':[9,8,7,6,5,4,3,1,2,4]})
writer=pd.ExcelWriter('pandas.xlsx')
df.to_excel(writer,sheet_name='sheet1')
writer.save()
'''
x=[1,5,8,3,7,6]
y=[5,8,2,6,8,3]
plt.title('My first graph!')
plt.plot(x,y,color='blue')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.xlim(0,5)
plt.show()
#file=open("pandas.xlsx",'rb')
