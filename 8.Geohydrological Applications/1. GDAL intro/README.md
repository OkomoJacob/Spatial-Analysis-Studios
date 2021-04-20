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

