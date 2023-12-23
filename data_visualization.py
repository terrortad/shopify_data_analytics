'''
This script loads the original dataset, filters active listings, and extracts and simplifies the condition data.
It then creates scatter plots using this data, with the actual prices on the y-axis.
The plots are designed to provide insights into the relationships between input variables and the output variables.
'''

import re
import pandas as pd
import plotly.express as px

# Load dataset
data = pd.read_csv(r'C:\Users\magic\Desktop\data structures\DE project\products_export_1-2.csv')

# Filter active listings
active_listings = data[data['Status'] == 'active']

def extract_condition(html_content):
    '''Function to extract the contition from the HTML content'''
    pattern = r"Condition:\s*(.+?)\s*</p>"
    match = re.search(pattern, str(html_content))
    return match.group(1) if match else None

active_listings['Extracted Condition'] = active_listings['Body (HTML)'].apply(extract_condition)

def simplify_condition(condition):
    '''Function to simplify the extracted conditions'''
    if condition is None:
        return 'Unknown'
    condition = condition.lower()
    if 'excellent' in condition:
        return 'Excellent'
    elif 'very good' in condition or 'vg' in condition:
        return 'Very Good'
    elif 'like new' in condition:
        return 'Like New'
    elif 'brand new' in condition or 'bnwt' in condition:
        return 'Brand New with Tags'
    elif 'new without tags' in condition or 'nwot' in condition:
        return 'New without Tags'
    elif 'good' in condition:
        return 'Good'
    elif 'play' in condition:
        return 'Play'
    else:
        return 'Other'

active_listings['Simplified Condition'] = active_listings['Extracted Condition'].apply(simplify_condition)

def remove_outliers(df, column, upper_limit):
    '''Remove outliers function'''
    return df[df[column] <= upper_limit]

# Set Max weight (30,000)
upper_limit_grams = 30000
filtered_active_listings = remove_outliers(active_listings, 'Variant Grams', upper_limit_grams)


# Visualizations using the ORIGINAL data

# Plot: Brand vs. Price
fig1 = px.scatter(active_listings, x='Vendor', y='Variant Price', color='Simplified Condition',
                  title='Brand vs. Price (Differentiated by Condition)',
                  labels={'Vendor': 'Brand', 'Variant Price': 'Price'})
fig1.show()

# Plot: Item Type vs. Price
fig2 = px.scatter(active_listings, x='Type', y='Variant Price', color='Simplified Condition',
                  title='Item Type vs. Price (Differentiated by Condition)',
                  labels={'Type': 'Item Type', 'Variant Price': 'Price'})
fig2.show()

# Plot: Grams vs. Price
fig3 = px.scatter(filtered_active_listings, x='Variant Grams', y='Variant Price', color='Simplified Condition',
                  title='Weight (Grams) vs. Price (Differentiated by Condition)',
                  labels={'Variant Grams': 'Weight (Grams)', 'Variant Price': 'Price'})
fig3.show()

# Plot: Cost per item vs. Price
fig4 = px.scatter(active_listings, x='Cost per item', y='Variant Price', color='Simplified Condition',
                  title='Cost per Item vs. Price (Differentiated by Condition)',
                  labels={'Cost per item': 'Cost per Item', 'Variant Price': 'Price'})
fig4.show()
