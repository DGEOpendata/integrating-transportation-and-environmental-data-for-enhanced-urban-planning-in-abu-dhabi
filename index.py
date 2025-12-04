python
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Load transportation and environmental datasets
transport_data = pd.read_csv('abu_dhabi_transportation_infrastructure.csv')
environmental_data = pd.read_csv('abu_dhabi_environmental_quality_indicators.csv')

# Example of merging datasets on a common key, e.g., district or area
merged_data = pd.merge(transport_data, environmental_data, on='area_id')

# Convert to GeoDataFrame for spatial operations
gdf = gpd.GeoDataFrame(
    merged_data, geometry=gpd.points_from_xy(merged_data.longitude, merged_data.latitude)
)

# Plotting transportation routes overlayed with air quality indicators
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(column='air_quality_index', cmap='coolwarm', ax=ax, legend=True)
plt.title('Transportation Routes and Air Quality in Abu Dhabi')
plt.show()
