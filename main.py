import pandas as pd
import os
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_seq_items',None)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('expand_frame_repr', False)
from simpledbf import Dbf5
import glob
for file in glob.glob(r"E:\rs-paper-august\data\shapefile_bharatpur\final-output-file\*.dbf"):
	if file.endswith('.dbf'):
		print(file)
		df=Dbf5(file)
		df1 = df.to_dataframe()
		with open(r"E:\rs-paper-august\data\shapefile_bharatpur\Namita-didi-task\%s.txt"%file.split('.')[-2].split('\\')[-1],'w+') as f1:
			f1.write(str(df1))
