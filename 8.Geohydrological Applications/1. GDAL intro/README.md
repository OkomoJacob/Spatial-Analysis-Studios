## What is GDAL
[GDAL](http://www.gdal.org) is a translator library for raster geospatial data formats that is released under an MIT style Open Source license by the Open Source Geospatial Foundation. As a [library](https://data-flair.training/blogs/python-libraries/), it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.

gdal allows you to perform many spatial queries viz., 
   * Retrieve information from GIS data
   * Reproject GIS data
   * Change raster properties
   * Convert raster formats
   * Convert vector formats
   * Apply spatial queries on vectors
   * Convert comma separated values files
   * Perform batch conversion, inter alia

### Retrieving Information from Raster Data
One of the easiest and most useful commands in GDAL is [gdalinfo](https://gdal.org/programs/gdalinfo.html). When given an image as an argument, it retrieves and prints all relevant information that is known about the file. This is especially useful if the image contains additional tag data, as is the case with TIFF files. When working with satellite imagery, this is an extremely useful way of keeping track of the images location in long/lat coordinates as well as the image projection.

* command `gdalinfo file.tif`
### Retrieve Information from Vector Data
For retrieving info from vector data we use the [ogrinfo](https://gdal.org/programs/ogrinfo.html) command.

* command `ogrinfo -al roads.shp`
### Reproject Raster Data
GDAL has the capability to change a raster coordinate system using the following syntax:

gdalwarp -t_srs EPSG:... <input> <output>

The -t_srs argument specifies the target coordinate system. If the source coordinate system is unknown it must be specified with the -s_srs argument. EPSG:... specifies the EPSG code of the projection. <input> and <output> are the input and output data respectively.

We are now going to reproject a Digital Elevation Model (DEM) acquired by the Shuttle Radar Topography Mission (SRTM). You can  download DEM's for your own area of interest from USGS Earth Explorer. Here we'll use the provided course data.

In order to reproject the DEM from WGS-84 lat/lon to Amersfoort/RD New we use this command:

gdalwarp -t_srs EPSG:XXXXX srtm_37_02.tif dem_rd.tif

1. Replace XXXXX with the proper EPSG code for Amersfoort/RD New (see one of your previous answers using ogrinfo).

2. Execute the command:

gdalwarp -t_srs EPSG:28992 srtm_37_02.tif dem_rd.tif <ENTER>

* More gdal commands can be found [here](https://gdal.org/drivers/raster/index.html)

### Batch conversion

Desktop GIS programmes are very useful for GIS operations, but are hard to use if we have to repeat the same task for many GIS layers. Then scripting can be a solution.

Here I have an example dataset from a land-use model of Dublin. The data are in IDRISI raster format (.rst), with one layer for each year between 1990 and 2030. Our task is to convert all layers to GeoTiff (.tif )format.

```python

for %%f in (*.rst) do (
   echo %%~nf
   gdal_translate -of GTiff %%f %%~nf.tif
)

```
