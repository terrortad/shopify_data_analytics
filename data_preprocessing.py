import pandas as pd
import re
from sklearn.preprocessing import MinMaxScaler


# Load the dataset
data = pd.read_csv(r'C:\Users\Your\Path\To\products_export_1-2.csv')

# Filter for active listings
active_listings = data[data['Status'] == 'active']

# Function to extract condition from the HTML content
def extract_condition(html_content):
    pattern = r"Condition:\s*(.+?)\s*</p>"
    match = re.search(pattern, str(html_content))
    return match.group(1) if match else None

active_listings['Extracted Condition'] = active_listings['Body (HTML)'].apply(extract_condition)

def simplify_condition(condition):
    '''Simplify Conditions function'''
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

# Applying simplify_condition
active_listings['Simplified Condition'] = active_listings['Extracted Condition'].apply(simplify_condition)

# Function to remove outliers
def remove_outliers(df, column):
    '''Function to remove outliers using IQR method'''
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Apply the function to 'Variant Price' and 'Cost per item'
cleaned_active_listings = remove_outliers(active_listings, 'Variant Price')
cleaned_active_listings = remove_outliers(cleaned_active_listings, 'Cost per item')

# Normalization with Min-Max Scaler
scaler = MinMaxScaler()
columns_to_scale = ['Variant Price', 'Cost per item']
cleaned_active_listings[columns_to_scale] = scaler.fit_transform(cleaned_active_listings[columns_to_scale])

# Save the normalized data to a new CSV file
cleaned_active_listings.to_csv('normalized_active_listings.csv', index=False)

