import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Interactive Data Dashboard")
st.markdown("""
Upload your CSV file and explore your data with interactive charts and summaries!
""")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    # تحديد الأعمدة الرقمية فقط
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_columns:
        column_to_plot = st.selectbox("Select a column to plot", numeric_columns)

        chart_type = st.selectbox("Select chart type", ["Histogram", "Boxplot", "Line Chart"])

        st.subheader(f"{chart_type} of {column_to_plot}")
        fig, ax = plt.subplots()

        if column_to_plot in df.columns:
            if chart_type == "Histogram":
                sns.histplot(df[column_to_plot], kde=True, ax=ax)
            elif chart_type == "Boxplot":
                sns.boxplot(y=df[column_to_plot], ax=ax)
            elif chart_type == "Line Chart":
                sns.lineplot(data=df[column_to_plot], ax=ax)

            st.pyplot(fig)
        else:
            st.warning("⚠️ The selected column does not exist in the dataset!")
    else:
        st.warning("⚠️ No numeric columns found in the uploaded CSV file.")
