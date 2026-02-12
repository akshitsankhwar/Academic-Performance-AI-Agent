import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class AcademicAIAgent:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = RandomForestClassifier(random_state=42)

    def validate_data(self):
        if self.data.isnull().sum().sum() > 0:
            return False, "Missing values detected."
        if self.data['semester'].nunique() < 2:
            return False, "Not enough historical data."
        return True, "Data is valid."

    def feature_engineering(self):
        features = []
        labels = []

        for student_id in self.data['student_id'].unique():
            student_data = self.data[self.data['student_id'] == student_id]

            gpa_trend = np.polyfit(student_data['semester'], student_data['gpa'], 1)[0]
            avg_attendance = student_data['attendance'].mean()
            avg_assignments = student_data['assignments_completed'].mean()

            features.append([gpa_trend, avg_attendance, avg_assignments])

            if student_data['gpa'].iloc[-1] < 6.0:
                labels.append(1)
            else:
                labels.append(0)

        return np.array(features), np.array(labels)

    def train_model(self):
        X, y = self.feature_engineering()
        self.model.fit(X, y)

    def predict_risk(self, gpa_trend, attendance, assignments):
        prediction = self.model.predict([[gpa_trend, attendance, assignments]])
        return prediction[0]

    def categorize_zone(self, risk, gpa):
        if risk == 1 or gpa < 6:
            return "🔴 Red"
        elif gpa < 7.5:
            return "🟡 Yellow"
        else:
            return "🟢 Green"

    def generate_recommendation(self, zone):
        if zone == "🔴 Red":
            return "Immediate academic intervention required. Increase attendance and seek tutoring."
        elif zone == "🟡 Yellow":
            return "Performance needs monitoring. Improve assignment consistency."
        else:
            return "Keep up the good performance!"