from sklearn.preprocessing import LabelEncoder
from data_collection import data as dw 

# Encode categorical target variable
le = LabelEncoder()
data = dw.copy()
data['species'] = le.fit_transform(data['species'])
print(data['species'].values)
# Check for missing values
print(data.isnull().sum())