import pandas as pd

input_doc = pd.read_csv('datos_data_engineer.tsv',sep='\t',encoding='utf-16-le')
input_doc.fillna(value='NULL', inplace=True)
input_doc.to_csv('datos_data_engineer.csv',sep='|',encoding='utf-8',index= False)

