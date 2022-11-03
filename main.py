import pandas as pd
import os
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_seq_items',None)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('expand_frame_repr', False)
from simpledbf import Dbf5
import glob
for file in glob.glob(input-directory\*.dbf"):
	if file.endswith('.dbf'):
		print(file)
		df=Dbf5(file)
		df1 = df.to_dataframe()
		with open("output-directory\name of file.txt",'w+') as f1:
			f1.write(str(df1))
