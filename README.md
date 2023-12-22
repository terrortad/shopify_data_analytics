# shopify_data_analytics
Repository for shopify data analytics

Kids Resale Items Analysis Project

Project Overview

This project dives into the analysis of kids' resale items, utilizing a dataset of over 13,000 rows obtained from a Shopify store. The goal is to uncover insights into the relationships between various attributes, such as brand, condition, item type, and price, to inform pricing strategies and inventory management.

Files in the Repository

app.py: A user-friendly Streamlit app that enables interactive exploration of item prices based on customizable filters for brand, condition, item type, and size.
data_visualization.py: Generates informative scatter plots to visualize relationships between different variables and item prices.
data_visualization_normalized.py: Produces scatter plots using normalized data, offering a visual perspective that accounts for variations in data scales.
data_preprocessing.py: Manages the essential tasks of data cleaning and preprocessing, including handling missing values, detecting outliers, and ensuring data integrity.
feature_eng.py: Implements feature engineering techniques, particularly focusing on extracting and categorizing item types from product titles to enhance analysis capabilities.
modify_dataset.py: Simplifies the condition data within the dataset, streamlining analysis and interpretation.
Installation and Running the Project

Prerequisites

Python 3.x
Required Python packages: pandas, plotly, streamlit
Install using pip install pandas plotly streamlit
Steps to Run

Clone the repository: git clone https://github.com/terrortad/shopify_data_analytics.git
Navigate to the cloned directory: cd shopify_data_analytics
Launch the Streamlit app: streamlit run app.py
This will open the app in your default web browser.
Usage

Streamlit App (app.py):
Interact with the app to explore item prices based on your preferred filters.
Customize your selections for brand, condition, item type, and size to view tailored results.
Visualization Scripts:
Run data_visualization.py or data_visualization_normalized.py to generate insightful scatter plots, aiding in visual data exploration and analysis.

