import streamlit as st
import joblib
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('Sentiment-Analysis')
getSeverityDict()
getDescription()
getprecautionDict()
getInfo()
tree_to_code(clf,cols)