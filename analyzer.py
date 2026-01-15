import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# df =pd.read_csv('./dataset/student_data.csv')
# print(df)
df =pd.read_csv('./dataset/Expanded_data_with_more_features.csv')
of=pd.read_csv('./dataset/Original_data_with_more_rows.csv')
# print(of.head())

print(df.isnull().sum())

# Drop unnamed columns
df=df.drop('Unnamed: 0',axis=1)
print(df.head())

# Change weeklyStudysession into columns
# df["WklyStudyHours"]=df['WklyStudyHours'].replace("{want to cahange}.to change value")

# Gender Distribution
plt.figure(figsize=(4,4))
ax=sns.countplot(data=df,x='Gender')
# sns tell us count of specfic columns
# for fignure size
ax.bar_label(ax.containers[0])
plt.show()
