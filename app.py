# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("car data.csv")

df = load_data()

st.title("🚗 Car Resale Data Explorer")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Filters
fuel = st.multiselect("Fuel Type", df["Fuel_Type"].unique(), default=df["Fuel_Type"].unique())
trans = st.multiselect("Transmission", df["Transmission"].unique(), default=df["Transmission"].unique())

filtered = df[(df["Fuel_Type"].isin(fuel)) & (df["Transmission"].isin(trans))]

st.subheader("📊 Filtered Results")
st.write(filtered)

# Plot: Present Price vs Selling Price
st.subheader("💹 Present Price vs Selling Price")
fig, ax = plt.subplots()
ax.scatter(filtered["Present_Price"], filtered["Selling_Price"], c='blue')
ax.set_xlabel("Present Price")
ax.set_ylabel("Selling Price")
st.pyplot(fig)
