from data_wrangling import data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


data['petal_ratio'] = data['petal_length'] / data['petal_width']# feature engineering
X = data.drop('species', axis=1)
y = data['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=True)

print("train",X_train)
model = RandomForestClassifier()
model.fit(X_train, y_train)


__all__ = ["model","X_test","y_test"]