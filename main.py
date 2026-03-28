import streamlit as st
import pandas as pd
# import numpy as np        # Will be used in future versions (data processing)
# import seaborn as sns     # Planned for advanced visualizations
import matplotlib.pyplot as plt

def main(): #Title and Sidebar
    st.title("Data_Visualization_Brick")
    st.sidebar.title("Files Section")
    upload_file = st.sidebar.file_uploader(
        "Upload Your File here",
        type=['csv', 'xlsx', 'xls', 'json', 'xml'])

    try:
        if upload_file is None:
            st.info("Please upload a file to continue.")
            return
        file_name = upload_file.name.lower()
        if file_name.endswith(".csv"):
            data = pd.read_csv(upload_file)
        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            data = pd.read_excel(upload_file)
        elif file_name.endswith(".json"):
            data = pd.read_json(upload_file)
        elif file_name.endswith(".xml"):
            data = pd.read_xml(upload_file)
        else:
            st.error("Unsupported file format")
            st.stop()
# numpy and pandas for data visualization
        st.sidebar.success("File uploaded successfully") #heading for sidebar
        st.subheader("Visualized data")
        st.dataframe(data.head())
# must you the sub headers
        st.subheader("Lets see some more details in data") #heading for sidebar
        st.write("Shape of the the data as Row,Column:",data.shape) #heandings
        st.write("The column name inside data is ",data.columns) #headings
        st.write("Missing value into column",data.isnull().sum()) #headings

# using matplotlib for graphs
        st.subheader("Lets see some more details in data")
        st.write(data.describe())
        st.subheader("Select columns for visualization")
        numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
        x_col = st.selectbox("Select X-axis column", numeric_columns)
        y_col = st.selectbox("Select Y-axis column", numeric_columns)

# graphs matplotlib x and y

        chart_type = st.selectbox("Select chart type", ["Line", "Bar"])
        st.subheader("Generated Graph")

        fig, ax = plt.subplots()

        if chart_type == "Line":
            ax.plot(data[x_col], data[y_col])
        elif chart_type == "Bar":
            ax.bar(data[x_col], data[y_col])

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{chart_type} Chart: {y_col} vs {x_col}")

        st.pyplot(fig)






    except Exception as e:
            st.error(f"Error:{e}")

if __name__ == "__main__":
    main()


#streamlit run aura-data-visualization/main.py
#code updated as on 29 jan 4:31 For inter changes 
