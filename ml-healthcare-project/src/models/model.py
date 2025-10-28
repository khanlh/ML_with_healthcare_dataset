# filepath: /ml-healthcare-project/ml-healthcare-project/src/models/model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

class Model:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestClassifier()

    def preprocess_data(self):
        # Example preprocessing: fill missing values and encode categorical variables
        self.data.fillna(method='ffill', inplace=True)
        self.data = pd.get_dummies(self.data, drop_first=True)

    def train(self, target_column):
        X = self.data.drop(columns=[target_column])
        y = self.data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        
        return accuracy, report

    def predict(self, new_data):
        return self.model.predict(new_data)