import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# df =pd.read_csv('./dataset/student_data.csv') Expanded_data_with_more_features.csv  Original_data_with_more_rows.csv

# print(df)
df =pd.read_csv("./dataset/Expanded_data_with_more_features.csv")
# of = pd.read_csv('./StudentAnalyzer/dataset/student_data.csv')
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
plt.title('Gender Chart')
plt.show()

#from above chart we have count the number of female and male

gd=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gd)

plt.figure(figsize=(3,5))
plt.title("ParentEduc vs StudentMarks")
sns.heatmap(gd,annot=True)
plt.show()
#from above chart we have concluded that the education of the parents have a good impact 


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)

plt.figure(figsize=(4,4))
plt.title("ParentMarital vs StudentMarks")
sns.heatmap(gb1,annot=True)
plt.show()
#from the above chart we have concluded that their is no/negligible impact on the student's score

sns.boxplot(data=df,x="MathScore")
plt.show()

# Distribution of Ethnic Group
print(df["EthnicGroup"].unique())

groupA=df.loc[(df['EthnicGroup'] =="group A")].count()

groupB=df.loc[(df['EthnicGroup'] =="group B")].count()

groupC=df.loc[(df['EthnicGroup'] =="group C")].count()
groupD=df.loc[(df['EthnicGroup'] =="group D")].count()
groupE=df.loc[(df['EthnicGroup'] =="group E")].count()

l=['group A','group B','group C', 'group D', 'group E']
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

plt.title("Ethnic Chart")
plt.pie(mlist, labels=l, autopct="%1.2f%%")
plt.show()

