from geopandas import plotting as plot
from matplotlib import pyplot as plt
from rasterio.plot import show_hist #Plots and displays a particular raster that we will assign to it
from rasterio.plot import show
import geopandas as gpd
import rasterstats
import rasterio

# Read the distrct .shp
districts = gpd.read_file(r'Districts/districts.shp')
districts.plot()
rainFall = rasterio.open('Rainfall Data Rasters/2020-4-3.tif', mode='r')
# show(rainFall)

# Plot both raster and vector at ago using matplotlib
fig, ax = plt.subplots(1, 1)