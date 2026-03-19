import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from kagglehub import KaggleDatasetAdapter

dataset = "vedavyasv/usa-housing"
file_path = "USA_Housing.csv"
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    dataset,
    file_path
)
head = df.head(10)
print(head)

info = df.info()
print(info)

describe = df.describe()
print(describe)

columns = df.columns
print(columns)

sns.pairplot(df.select_dtypes(include=[np.number]))

sns.pairplot(df.select_dtypes(include=[np.number]).corr(), annot=True)

plt.show()