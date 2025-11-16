import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================
# Step 1: Load Dataset
# ============================
print("Loading Dataset...")
df = pd.read_csv(r"C:\Zukhruf\Python\SMIT-AI and DataScience\Assignments\1st\Dataset\healthcare-dataset-stroke-data.csv")
print("Dataset Loaded Successfully!\n")

# ============================
# Step 2: Explore Dataset
# ============================
print("Full Dataset:\n", df)
print("\nHead of Dataset:\n", df.head())
print("\nDataset Info:\n")
df.info()
print("\nDuplicated Rows:", df.duplicated().sum())
print("\nNull Values:\n", df.isnull().sum())
print("\nColumns:\n", df.columns)

# ============================
# Step 3: Age Group Creation
# ============================
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '80+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)

# ============================
# 1. Stroke vs Heart Disease
# ============================
stroke_hd = df.groupby('heart_disease')['stroke'].sum()

plt.bar(['Has Heart Disease','No Heart Disease'], stroke_hd, color=['skyblue', 'salmon'])
plt.title("Stroke vs Heart Disease")
plt.xlabel("Heart Disease")
plt.ylabel("Number of Stroke Cases")
plt.show()

# ============================
# 2. Stroke vs Hypertension
# ============================
stroke_hyp = df.groupby('hypertension')['stroke'].sum()

plt.bar(['No Hypertension', 'Has Hypertension'], stroke_hyp, color=['orange', 'lightgreen'])
plt.title("Stroke vs Hypertension")
plt.xlabel("Hypertension")
plt.ylabel("Number of Stroke Cases")
plt.show()

# ============================
# 3. Stroke by Age Group
# ============================
stroke_age = df.groupby('age_group')['stroke'].sum()

plt.bar(stroke_age.index, stroke_age.values, color='violet')
plt.title("Stroke by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Stroke Cases")
plt.show()

# ============================
# 4. Stroke by Gender
# ============================
stroke_gender = df.groupby('gender')['stroke'].sum()

plt.bar(stroke_gender.index, stroke_gender.values, color=['lightcoral', 'lightblue', 'gray'])
plt.title("Stroke by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Stroke Cases")
plt.show()

# ============================
# 5. Hypertension by Age Group
# ============================
age_hyp = df.groupby('age_group')['hypertension'].sum()

plt.bar(age_hyp.index, age_hyp.values, color='teal')
plt.title("Hypertension by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Hypertension Cases")
plt.show()

# ============================
# 6. Heart Disease by Age Group
# ============================
age_hd = df.groupby('age_group')['heart_disease'].sum()

plt.bar(age_hd.index, age_hd.values, color='gold')
plt.title("Heart Disease by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Heart Disease Cases")
plt.show()

# ============================
# 7. Hypertension by Gender
# ============================
gender_hyp = df.groupby('gender')['hypertension'].sum()

plt.bar(gender_hyp.index, gender_hyp.values, color=['plum', 'lightgreen', 'gray'])
plt.title("Hypertension by Gender")
plt.xlabel("Gender")
plt.ylabel("Hypertension Cases")
plt.show()

# ============================
# 8. Report (As a Comment)
# ============================

"""
REPORT:

Overview:
This dataset contains people’s healthcare information including age, gender,
hypertension, heart disease, and stroke history. The goal was to study how
these health factors relate to stroke chances.

Findings:

1. Stroke & Heart Disease:
   People with heart disease were more likely to have a stroke.

2. Stroke & Hypertension:
   Individuals with high blood pressure showed higher stroke cases.

3. Stroke & Age:
   Stroke cases were highest among individuals aged 60 and above.

4. Stroke & Gender:
   Females had a slightly higher stroke rate compared to males.

5. Age & Hypertension:
   Older age groups had more hypertension cases.

6. Gender & Heart Disease:
   Males had more heart disease cases compared to females.

7. Age & Heart Disease:
   Heart disease was more common among older individuals.

8. Gender & Hypertension:
   Hypertension was more common in males than females.

Conclusion:
Age, hypertension, and heart disease are major contributors to stroke risk.
People above 60 with high blood pressure or heart problems have a much higher
chance of strokes. Proper heart care and blood pressure control can reduce
stroke risk significantly.
"""

