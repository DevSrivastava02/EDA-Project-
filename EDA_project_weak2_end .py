import pandas as pd
import matplotlib.pyplot as mp
import seaborn as se

df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# anaysis the data
print(df.info())
print(df.describe())
#see the first 5 datasets and last 5 dataset
print(df.head())
print(df.tail())


#Handle the missing Dataset
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.head())
print(df.tail())



