# Academic-Performance-AI-Agent
#  Academic Performance AI Agent

## Objective

This project designs an AI Agent that helps students and faculty understand academic performance trends. The system retrieves academic and attendance data, analyzes trends, detects performance gaps, forecasts risk, and generates actionable recommendations.

---

##  AI Agent Architecture

### System Flow:

Institutional Database / LMS  
↓  
Data Ingestion Layer  
↓  
Data Validation Module  
↓  
Feature Engineering  
↓  
Performance Analysis Engine  
↓  
Risk Prediction Model  
↓  
Insight Generation  
↓  
Recommendation Engine  
↓  
Dashboard Output  

---

##  Internal Components

### 1 Data Ingestion
- Retrieves GPA, attendance, assignment data
- Structured academic records

### 2 Data Validation
- Checks missing values
- Ensures sufficient historical data
- Flags incomplete records

### 3 Feature Engineering
- GPA trend slope
- Average attendance
- Assignment completion consistency

### 4 Performance Analysis
- Linear Regression for GPA trend
- Random Forest for risk prediction

### 5 Risk Categorization
- 🟢 Green → On track
- 🟡 Yellow → Needs monitoring
- 🔴 Red → At risk

### 6 Recommendation Engine
Hybrid rule-based + ML approach:
- Low attendance → Suggest attendance improvement
- Declining GPA → Suggest tutoring
- High risk → Immediate intervention

---

##  Technology Stack

| Layer | Technology | Justification |
|-------|------------|---------------|
| Data Processing | Pandas | Structured data handling |
| ML Model | Scikit-learn | Risk classification |
| Trend Analysis | NumPy | Regression calculation |
| Dashboard | Streamlit | Fast UI deployment |
| Language | Python | AI/ML ecosystem |

---

##  Security & Privacy Considerations

- Role-based access control
- Student data confidentiality
- No hard-coded credentials
- Expandable to FERPA/GDPR compliance

---

##  How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
