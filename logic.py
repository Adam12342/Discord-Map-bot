import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def create_and_save_map(file_path, cities=None):
    fig = plt.figure(figsize=(10, 5))

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    ax.gridlines(draw_labels=True)

    ax.set_title('World Map')

    if cities:
        for city in cities:
            name, lat, lon = city
            ax.plot(lon, lat, 'ro')  
            ax.text(lon + 1, lat, name, fontsize=12, transform=ccrs.PlateCarree())

    plt.savefig(file_path)
    plt.close()

if __name__ == "__main__":
    cities = [('Moscow', 55.7558, 37.6173), ('New York', 40.7128, -74.0060), ('Tokyo', 35.6895, 139.6917), ('Los Angeles', 34.0549, 118.2426)]
    create_and_save_map('world_map_with_cities.png', cities)