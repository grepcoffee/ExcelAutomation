import pandas as pd 

# import both xlsx files into the script. 
filea = pd.read_excel('LastLogon.xlsx')
fileb = pd.read_excel('TermReport.xlsx')

# Combine the files. change "UserName" to whatever excel row you would like.
combine = pd.merge(filea,fileb, on="UserName")

#export files to xlsx file called CombinedReport
combine.to_excel("CombinedReport.xlsx")
