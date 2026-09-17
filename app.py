import streamlit as st
import joblib
model=joblib.load("LogisticRegression_study_hours_model.pkl")
st.title("Student Pass/Fail based on Study Hours")
hours=st.number_input("Enter Study Hours: ",min_value=0.0, max_value= 15.0, value=5.0)
if st.button("Predict"):
  prediction=model.predict([[hours]])
  probability = model.predict_proba([[hours]])
  fail_probability = probability[0][0] * 100
  pass_probability = probability[0][1] * 100
  if prediction[0]==1:
    st.success("✓ Pass")
    st.write("Pass Probability:", round(pass_probability, 2), "%")
  else:
    st.error("❌ Fail")
    st.write("Fail Probability:", round(fail_probability, 2), "%")
