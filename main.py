import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for store locations, sales, and customer density
np.random.seed(42)  # for reproducibility
num_stores = 50
store_data = {
    'StoreID': range(1, num_stores + 1),
    'Longitude': np.random.uniform(-122.5, -122, num_stores),
    'Latitude': np.random.uniform(37.7, 37.8, num_stores),
    'Sales': np.random.randint(10000, 100000, num_stores),
    'CustomerDensity': np.random.randint(100, 1000, num_stores)
}
df_stores = pd.DataFrame(store_data)
# Create geometry column for geospatial analysis
df_stores['geometry'] = df_stores.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
gdf_stores = gpd.GeoDataFrame(df_stores, geometry='geometry', crs="EPSG:4326")
# --- 2. Analysis ---
# Calculate average sales per customer density
df_stores['SalesPerCustomer'] = df_stores['Sales'] / df_stores['CustomerDensity']
# Identify high-performing stores
high_performing_stores = df_stores[df_stores['Sales'] > 75000]
# Identify low-performing stores
low_performing_stores = df_stores[df_stores['Sales'] < 25000]
# --- 3. Visualization ---
# Plot store locations with sales performance
plt.figure(figsize=(10, 6))
plt.scatter(df_stores['Longitude'], df_stores['Latitude'], c=df_stores['Sales'], cmap='viridis', s=50)
plt.colorbar(label='Sales')
plt.title('Store Locations and Sales Performance')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
#Save the plot
output_filename = 'store_locations.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Plot high and low performing stores
plt.figure(figsize=(10,6))
plt.scatter(high_performing_stores['Longitude'], high_performing_stores['Latitude'], color='green', label='High Performing', s=100)
plt.scatter(low_performing_stores['Longitude'], low_performing_stores['Latitude'], color='red', label='Low Performing', s=100)
plt.legend()
plt.title('High and Low Performing Stores')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
output_filename = 'high_low_performing.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis could involve clustering algorithms to identify optimal locations for new stores
#or spatial autocorrelation analysis to understand the relationship between store locations and sales.