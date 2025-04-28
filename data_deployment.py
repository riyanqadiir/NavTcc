import joblib
from data_training import train_model
from data_evaluation import evaluate_model

# Train and save the model
model, X_train, X_test, y_train, y_test = train_model()
evaluate_model(model, X_test, y_test)

joblib.dump(model, 'iris_model.pkl')
print("Model saved as iris_model.pkl")
