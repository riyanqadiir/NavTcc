from data_training import model,X_test,y_test
from sklearn.metrics import accuracy_score, classification_report
import joblib

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(model,"iris_file.pkl")
