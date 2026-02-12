import streamlit as st
import numpy as np
from model import AcademicAIAgent

st.title(" Academic Performance AI Agent")

agent = AcademicAIAgent("data_sample.csv")

valid, message = agent.validate_data()

if not valid:
    st.error(message)
else:
    agent.train_model()
    st.success("Model trained successfully!")

    student_id = st.number_input("Enter Student ID", min_value=1, max_value=3)

    student_data = agent.data[agent.data['student_id'] == student_id]

    if not student_data.empty:
        gpa_trend = np.polyfit(student_data['semester'], student_data['gpa'], 1)[0]
        avg_attendance = student_data['attendance'].mean()
        avg_assignments = student_data['assignments_completed'].mean()
        latest_gpa = student_data['gpa'].iloc[-1]

        risk = agent.predict_risk(gpa_trend, avg_attendance, avg_assignments)
        zone = agent.categorize_zone(risk, latest_gpa)
        recommendation = agent.generate_recommendation(zone)

        st.subheader(" Performance Summary")
        st.write(f"GPA Trend: {round(gpa_trend, 2)}")
        st.write(f"Average Attendance: {round(avg_attendance, 2)}%")
        st.write(f"Zone: {zone}")

        st.subheader(" Recommendation")
        st.write(recommendation)

        st.line_chart(student_data.set_index("semester")["gpa"])
    else:
        st.warning("Student not found.")