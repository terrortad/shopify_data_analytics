import pandas as pd
import plotly.express as px

# Load normalized dataset
normalized_data = pd.read_csv('normalized_active_listings.csv')

# Plot: Brand vs Normalized price
fig1 = px.scatter(normalized_data, x='Vendor', y='Variant Price', color='Simplified Condition',
                  title='Brand vs. Normalized Price (Differentiated by Condition)',
                  labels={'Vendor': 'Brand', 'Variant Price': 'Normalized Price'})
fig1.show()

# Plot: Item type vs. Normalized Price
fig2 = px.scatter(normalized_data, x='Type', y='Variant Price', color='Simplified Condition',
                  title='Item Type vs. Normalized Price (Differentiated by Condition)',
                  labels={'Type': 'Item Type', 'Variant Price': 'Normalized Price'})
fig2.show()

# Plot: Weight vs Price
fig3 = px.scatter(normalized_data, x='Variant Grams', y='Variant Price', color='Simplified Condition',
                  title='Weight (Grams) vs. Price (Differentiated by Condition)',
                  labels={'Variant Grams': 'Weight (Grams)', 'Variant Price': 'Price'})
fig3.show()

# Plot: Cost per item vs. Price
fig4 = px.scatter(normalized_data, x='Cost per item', y='Variant Price', color='Simplified Condition',
                  title='Cost per Item vs. Price (Differentiated by Condition)',
                  labels={'Cost per item': 'Cost per Item', 'Variant Price': 'Price'})
fig4.show()