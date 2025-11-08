import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ---------------------------------
# Step 1: Load Dataset
print ("Loading The DataSet........ \n")
df = pd.read_csv(r"C:\Zukhruf\Python\SMIT-AI and DataScience\Assignments\1st\Dataset\healthcare-dataset-stroke-data.csv")
print("✅ Dataset Loaded Successfully!\n")
# ---------------------------------
# Step 2: Explore Dataset
print("Whole DataSet........ \n\n", df , "\n")

print("Shape of dataset.....\n\n", df.shape, "\n")

print("Info of DataSet........ \n\n", df.info() , "\n")

print ("Null Sets Of DataSet........\n\n", df.isnull().sum() , "\n")

print("Name of Columns in DataSet........ \n\n", df.columns.to_series(index=[1,2,3,4,5,6,7,8,9,10,11,12]), "\n")

print("ID Coloum of DataSet........ \n\n",( df['id'].head(10)) , "\n")

print(" Head of DataSet........ \n\n", df.head(10) , "\n")

print (" Duplicated DataSet........ \n\n", df.duplicated().sum() , "\n")

print (df['stroke'])
print (df['age'])
print (df['stroke'].value_counts() , "\n")


# mask1=df['stroke']=='0'
# mask2=df['age']>'2010-01-01'
# df[mask1 & mask2].shape[0]