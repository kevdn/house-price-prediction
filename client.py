import streamlit as st
import requests
server = "http://localhost:30001"

st.title("House Price Prediction")

# Input feature values
MSSubClass = st.number_input("MSSubClass", min_value=20, max_value=190, value=60)
MSZoning = st.text_input("MSZoning", "RL")
LotArea = st.number_input("LotArea", min_value=1300, max_value=215000, value=7844)
LotConfig = st.text_input("LotConfig", "Inside")
BldgType = st.text_input("BldgType", "1Fam")
OverallCond = st.number_input("OverallCond", min_value=1, max_value=10, value=7)
YearBuilt = st.number_input("YearBuilt", min_value=1800, max_value=2020, value=1978)
YearRemodAdd = st.number_input("YearRemodAdd", min_value=1800, max_value=2020, value=1978)
Exterior1st = st.text_input("Exterior1st", "HdBoard")
BsmtFinSF2 = st.number_input("BsmtFinSF2", min_value=0.0, max_value=2000.0, value=0.0)
TotalBsmtSF = st.number_input("TotalBsmtSF", min_value=0.0, max_value=2000.0, value=672.0)

# Create a dictionary with the data
data = {
    "MSSubClass" : MSSubClass,
    "MSZoning" : MSZoning,
    "LotArea" : LotArea,
    "LotConfig" : LotConfig,
    "BldgType" : BldgType,
    "OverallCond" : OverallCond,
    "YearBuilt" : YearBuilt,
    "YearRemodAdd" : YearRemodAdd,
    "Exterior1st" : Exterior1st,
    "BsmtFinSF2" : BsmtFinSF2,
    "TotalBsmtSF" : TotalBsmtSF
}

# Make a request to the server
response = requests.post(f"{server}/predict", json=data)

# Get the result
result = response.json()

# Display the result
st.write(f"The predicted price is: {result['price']}")


