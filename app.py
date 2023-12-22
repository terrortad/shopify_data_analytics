import streamlit as st
import pandas as pd

# Load the enhanced dataset
data = pd.read_csv('enhanced_dataset.csv')

# Creating the UI
st.title('Kids Resale Item Price Display')

# User input fields
brand = st.selectbox('Select Brand', options=data['Vendor'].unique())
condition = st.selectbox('Select Condition', options=data['Simplified Condition'].unique())
item_type = st.selectbox('Select Item Type', options=data['Item Category'].unique())
size = st.text_input('Enter Size (optional)')

# Button to display results
if st.button('Show Matching Items'):
    # Filter the dataset based on user inputs
    filtered_data = data[(data['Vendor'] == brand) & 
                         (data['Simplified Condition'] == condition) & 
                         (data['Item Category'] == item_type)]

    # Check for size input
    if size:
        filtered_data = filtered_data[filtered_data['Size'] == size] 

    # Display results
    if not filtered_data.empty:
        st.write(filtered_data[['Title', 'Variant Price']])
    else:
        st.write("No matching items found.")
