import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the App
st.title("🎬 Movie Analysis Dashboard")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\dharn\Downloads\movies.csv")  # Make sure this file is in the same folder
    return df

df = load_data()

# Show Dataset
if st.checkbox("Show Raw Data"):
    st.write(df)

# Scatter Plot (Budget vs Gross)
st.subheader("📊 Budget vs Gross Revenue")
fig, ax = plt.subplots()
sns.scatterplot(x=df["budget"], y=df["gross"], alpha=0.5, ax=ax)
plt.xlabel("Budget")
plt.ylabel("Gross Revenue")
st.pyplot(fig)

# Correlation Matrix
st.subheader("📉 Correlation Matrix")
corr = df.corr(numeric_only=True)
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
