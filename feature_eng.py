import re
import pandas as pd

# Load the original dataset
data = pd.read_csv(r'C:\Users\magic\Desktop\data structures\DE project\products_export_1-2.csv')

def categorize_by_title(title):
    '''Function to categorize item type based on the title'''
    if pd.isna(title):
        return 'Unknown'  # default category for missing titles
    title_lower = title.lower()
    
    if 'toy' in title_lower:
        return 'Toys'
    elif any(word in title_lower for word in ['top', 'shirt', 't-shirt', 'blouse']):
        return 'Tops'
    elif 'accessory' in title_lower or 'accessories' in title_lower:
        return 'Accessories'
    elif any(word in title_lower for word in ['dress', 'skirt']):
        return 'Dresses + Skirts'
    elif 'sweater' in title_lower:
        return 'Sweaters'
    elif 'short' in title_lower:
        return 'Shorts'
    elif 'set' in title_lower:
        return 'Sets'
    elif 'romper' in title_lower:
        return 'Rompers'
    elif 'pant' in title_lower or 'jean' in title_lower or 'legging' in title_lower:
        return 'Pants'
    elif any(word in title_lower for word in ['pj', 'pajama', 'sleep sack', 'sleepwear']):
        return 'Sleepwear / Accessories'
    elif any(word in title_lower for word in ['shoe', 'boot', 'sandal']):
        return 'Footwear'
    elif 'costume' in title_lower:
        return 'Costumes'
    elif 'outerwear' in title_lower or 'jacket' in title_lower or 'coat' in title_lower:
        return 'Outerwear'
    elif 'swim' in title_lower:
        return 'Swim'
    elif 'gear' in title_lower:
        return 'Gear'
    elif any(word in title_lower for word in ['maternity', 'nursing']):
        return 'Maternity + Nursing'
    elif 'blazer' in title_lower or 'suit' in title_lower:
        return 'Blazers + Suits'
    else:
        return 'Other'
    
def extract_and_simplify_condition(html_content):
    '''Function to extract and simplify condition from the HTML content'''
    pattern = r"Condition:\s*(.+?)\s*</p>"
    match = re.search(pattern, str(html_content))
    condition = match.group(1).lower() if match else 'unknown'

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

# Applying the function to extract and simplify condition
data['Simplified Condition'] = data['Body (HTML)'].apply(extract_and_simplify_condition)

data['Item Category'] = data['Title'].apply(categorize_by_title)

# Save the enhanced dataset to a new CSV file
data.to_csv('enhanced_dataset.csv', index=False)
