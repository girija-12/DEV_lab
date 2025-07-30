import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Sample data for countries, Indian states, districts
world_data = pd.DataFrame({
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})

india_states_data = pd.DataFrame({
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'],
    'Value': [50, 75, 60, 40, 30]
})

india_districts_data = pd.DataFrame({
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'],
    'Value': [20, 30, 25, 15, 10]
})

# Load world map
world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge world data
world_data_geo = world_map.merge(world_data, how='left', left_on='name', right_on='Country')

# Since naturalearth_lowres doesn't have Indian states/districts,
# we'll create empty GeoDataFrames for demonstration
india_states_map = gpd.GeoDataFrame({'State': india_states_data['State']})
india_districts_map = gpd.GeoDataFrame({'District': india_districts_data['District']})

# Merge state/district data with empty GeoDataFrames (no geometry)
india_states_data_geo = india_states_map.merge(india_states_data, on='State')
india_districts_data_geo = india_districts_map.merge(india_districts_data, on='District')

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# World Countries plot
world_data_geo.boundary.plot(ax=axs[0], color='Black')
world_data_geo.plot(column='Value', ax=axs[0], legend=True,
                    legend_kwds={'label': "Values by Country"})
axs[0].set_title('World Countries Data')

# Indian States plot (no geometry, so just plot bar chart)
axs[1].bar(india_states_data_geo['State'], india_states_data_geo['Value'], color='orange')
axs[1].set_title('Indian States Data')
axs[1].set_ylabel('Value')
axs[1].set_xticklabels(india_states_data_geo['State'], rotation=45, ha='right')

# Indian Districts plot (no geometry, so just plot bar chart)
axs[2].bar(india_districts_data_geo['District'], india_districts_data_geo['Value'], color='green')
axs[2].set_title('Indian Districts Data')
axs[2].set_ylabel('Value')
axs[2].set_xticklabels(india_districts_data_geo['District'], rotation=45, ha='right')

plt.tight_layout()
plt.show()