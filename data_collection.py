import pandas as pd

# Example: Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
data['species'].unique()
data['species'].values

