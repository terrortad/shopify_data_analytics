import pandas as pd

normalized_data = pd.read_csv(r'C:\Users\magic\Desktop\data structures\normalized_active_listings.csv')

# Check min and max values of the normalized columns to verify normalization is in correct range
print(normalized_data['Variant Price'].min(), normalized_data['Variant Price'].max())
print(normalized_data['Cost per item'].min(), normalized_data['Cost per item'].max())

