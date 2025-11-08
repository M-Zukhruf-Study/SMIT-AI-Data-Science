# from google.colab import drive
# drive.mount('/content/gdrive')
# ===========================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ===========================================================================
# Step 1: Load Dataset
print ("Loading The DataSet........")
# df = pd.read_csv("/content/gdrive/MyDrive/healthcare-dataset-stroke-data.csv")
# df = pd.read_csv("/content/drive/MyDrive/healthcare-dataset-stroke-data.csv")
df = pd.read_csv(r"C:\Zukhruf\Python\SMIT-AI and DataScience\Assignments\1st\Dataset\healthcare-dataset-stroke-data.csv")
print(" Dataset Loaded Successfully!\n")
# ===========================================================================
# Step 2: Explore Dataset
print("Whole DataSet........ \n\n", df)

print(" Head of DataSet........ \n\n", df.head())

print("Info of DataSet........ \n\n", df.info())

print (" Duplicated DataSet........ \n\n", df.duplicated().sum())

print ("Null Sets Of DataSet........\n\n", df.isnull().sum())

print("Name of Columns in DataSet........ \n\n", df.columns.to_series(index=[1,2,3,4,5,6,7,8,9,10,11,12]))

df['stroke']
df['stroke'].value_counts()

df[['stroke','heart_disease','hypertension','age','gender']]

df[['stroke','heart_disease','hypertension','age','gender']].value_counts()

df[['stroke','age']].value_counts()

# ===========================================================================
# how many people had stroke that already has Heart disease
stroke_hd = df.groupby('heart_disease')['stroke'].sum()

plt.bar(['No Heart Disease', 'Has Heart Disease'], stroke_hd, color=['skyblue', 'salmon'])
plt.title("Stroke vs Heart Disease")
plt.xlabel("Heart Disease")
plt.ylabel("Number of Stroke Cases")
plt.show()
# ===========================================================================
#how many people had stroke that already has hypertension
stroke_hyp = df.groupby('hypertension')['stroke'].sum()

plt.bar(['Has Hypertension', 'No Hypertension'], stroke_hyp, color=['lightgreen', 'orange'])
plt.title("Stroke vs Hypertension")
plt.xlabel("Hypertension")
plt.ylabel("Number of Stroke Cases")
plt.show()
# ===========================================================================
# which age group has more stroke rate

# Creating age groups
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '80+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)

# strokes/age group
stroke_age = df.groupby('age_group')['stroke'].sum()

plt.bar(stroke_age.index, stroke_age.values, color='violet')
plt.title("Stroke by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Stroke Cases")
plt.show()
# ===========================================================================
#which gender has more stroke rate

stroke_gender = df.groupby('gender')['stroke'].sum()

plt.bar(stroke_gender.index, stroke_gender.values, color=['lightcoral', 'lightblue', 'gray'])
plt.title("Stroke by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Stroke Cases")
plt.show()

df['gender'].value_counts()
# ===========================================================================
# which age group has more hypertension rate

age_hyp = df.groupby('age_group')['hypertension'].sum()

plt.bar(age_hyp.index, age_hyp.values, color='teal')
plt.title("Hypertension by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Hypertension Cases")
plt.show()
# ===========================================================================
# in which age group heart disease are common

age_hd = df.groupby('age_group')['heart_disease'].sum()

plt.bar(age_hd.index, age_hd.values, color='gold')
plt.title("Heart Disease by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Heart Disease Cases")
plt.show()

df['age'].sort_values().value_counts()
# df ['age']
# ===========================================================================
# hypertension is commom in which gender

gender_hyp = df.groupby('gender')['hypertension'].sum()

plt.bar(gender_hyp.index, gender_hyp.values, color=['plum', 'lightgreen', 'gray'])
plt.title("Hypertension by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Hypertension Cases")
plt.show()
# ===========================================================================
"""**Report :**

# **Overveiw Of Data**

  This dataset has information about peoples healtcare that include their age, gender, hypertension, heart disease, and ever they had a stroke.
The main goal of doing this analysis was to identify relationships between these health features and stroke.


# **Findings**
1. **Stroke & Heart Disease:**
People with heart disease had higher chance of having a stroke as compared to those without heart disease.

2. **Stroke & Hypertension:**
People who already had hypertension (high blood pressure) has a higher chance of stokes.

3. **Stroke & Age:**=
More Stroke Cases has been found in the age of 60 and 60 above.

4. **Stroke & Gender:**
Females has more stroke rates as compair to males.

5. **Age & Hypertension:**
Old age peoples had more hypertension cases.


6. **Gender & Heart Disease:**
Male has more heart disease rate as compair to females.

7. **Age & Heart Disease:**
Old age peoples had more Heart diseases.

8. **Gender & Hypertension:**
Male has more hypertension rate as compair to females.

# **Conclusion:**
In conclusion it is clear that old age, hypertension, and heart disease are the main factors that increase the chances of stroke.
People above 60 years, especially those with high blood pressure or heart problems, are more likely to have strokes.
The data also shows that females had slightly higher stroke rates, while males had more hypertension and heart disease.
Overall, maintaining heart health and controlling blood pressure can greatly help in reducing stroke risk.

"""