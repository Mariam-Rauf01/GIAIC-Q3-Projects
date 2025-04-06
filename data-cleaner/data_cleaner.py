import streamlit as st
import pandas as pd
from io import BytesIO

# Set page config with a custom title and layout
st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")

# Streamlit Styles
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
    }
    [data-testid="stHeader"] {
        background-color: #E63946;
    }
    h1 {
        text-align: center;
        color: #E63946;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with Markdown styling
st.markdown("<h1>📁 File Converter & Cleaner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload CSV or Excel files to clean and convert effortlessly 🚀</p>", unsafe_allow_html=True)

# File uploader widget
files = st.file_uploader("📤 Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

def load_file(file):
    """Loads CSV or Excel file."""
    ext = file.name.split(".")[-1]
    try:
        if ext == "csv":
            return pd.read_csv(file, delimiter=",")  # Allow custom delimiter later
        elif ext == "xlsx":
            return pd.read_excel(file)
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        st.error(f"❌ Error reading {file.name}: {e}")
        return None

if files:
    for file in files:
        df = load_file(file)

        if df is None:
            continue

        # File preview
        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        # Data cleaning options
        with st.expander(f"🔧 Data Cleaning Options - {file.name}"):
            fill_option = st.radio("Fill Missing Values:", ["Mean", "Custom Value"], key=file.name)
            if fill_option == "Mean":
                df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            else:
                custom_value = st.number_input("Enter a value to replace missing values", value=0.0)
                df.fillna(custom_value, inplace=True)
            st.success("✅ Missing values handled!")
            st.dataframe(df.head())

            if st.checkbox("🗑 Remove Duplicate Rows"):
                df.drop_duplicates(inplace=True)
                st.success("✅ Duplicate rows removed!")

        selected_columns = st.multiselect(f"🎛️ Select Columns to Keep - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        # Chart visualization
        with st.expander(f"📊 Data Visualization - {file.name}"):
            numeric_cols = df.select_dtypes(include="number").columns
            if numeric_cols.any():
                chart_cols = st.multiselect("📈 Select Numeric Columns for Chart", numeric_cols, default=numeric_cols[:2])
                if chart_cols:
                    st.bar_chart(df[chart_cols])
                else:
                    st.info("ℹ️ Please select at least one numeric column.")
            else:
                st.warning("⚠️ No numeric columns found!")

        # Format choice radio button
        format_choice = st.radio(f"🔄 Convert {file.name} to:", ["CSV", "Excel"], key=f"convert_{file.name}")

        if st.button(f"⬇️ Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(".xlsx", ".csv")
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(".csv", ".xlsx")
            output.seek(0)
            st.download_button("⬇️ Download File", file_name=new_name, data=output, mime=mime)

    st.success("🎉 All files processed successfully!")
else:
    st.info("👆 Upload one or more CSV or Excel files to get started.")
