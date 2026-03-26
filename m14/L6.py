import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())
df = sns.load_dataset('penguins')
print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
print(df.corr(numeric_only=True))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()
df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(8,12))
plt.show()
print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())
sns.countplot(data=df, x='sex')
plt.show()
sns.countplot(data=df, x='island')
plt.show()
sns.countplot(data=df, x='species')
plt.show()
sns.countplot(data=df, x='sex', hue='species')
plt.show()
sns.countplot(data=df, x='island', hue='species')
plt.show()
sns.pairplot(data=df, hue='species')
plt.show()

import pandas as pd
product = {'customer': ['Anastasia','Dima','Katherine','James','Emily','Micheal','Matthew','Laura','Kevin','Jonas'],
             'place': ['France', 'Spain', 'Portugal', 'India', 'USA', 'Brazil', 'India', 'Morocco','Chile','Monaco'],
             'ID':[12424,32345,23255,344663,23646,365365,145346,163443,264643,13643]}

df = pd.DataFrame(product)
print(df)