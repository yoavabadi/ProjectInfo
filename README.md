# ProjectInfo
This repository houses Geographic Information Systems (GIS) Tools for Esri's End Users, via a Python toolbox of tools, for re-creating Esri's Advance Tools with only a Basic license.

## Getting Started - User Guide
* Make sure you have Esri's basic license and the arcpy library installed in your machine.
* Download the toolbox and place it in an appropriate folder on your machine. Navigate to the folder in Catalog. If you expand all the toolsets, you will see the following:

![alt tag](/toolset.PNG)

* Click on the appropriate tool, and start working!

## Contributing

This project welcomes contributions from anyone and everyone,  of many forms.

Examples of contributions include:

* Code patches
* Documentation improvements
* Bug reports and patch reviews. 

Those contributions should be performed by [submitting a pull request](https://github.com/yoavabadi/ProjectInfo/pulls).

## Issues

Found a bug, or want to request a new feature?  Please let me know by [submitting an issue](https://github.com/yoavabadi/ProjectInfo/issues).

## Tools

The tools are organized into toolsets, currently only one has been developed -Th e Data Management toolset.

### Data Management Tools
* #### Erase

  This tool creates an Erase (difference) layer from a source layer and overlay layer.

* #### Symmetric Difference

  This tool creates a Symmetric Difference layer from a source layer and overlay layer.

* #### Convex Hull

  This tool creates a Convex Hull of the input layer. This feature exists in ArcInfo, as part of the 'Minimum Bounding Geometry' tool.

* #### Split Line At Intersection

  This tool Split polylines in a polyline layer, by they're intersection points.

* #### Polygon to Line

  This tool creates a PolyLine layer from a Polygon layer (the polygons' boundary).

* #### Simplify Features

  This tool Simplify Polygons \ Polyline Features, by a tolerance distance.

* #### Aggregate Polygons

  This tool creates an aggregation layer of the input polygons, aggregated by a tolerance distance, with convex hull.
  This tool result differ from esri's tool, as you can see in the below figure (this tool's result in green, Esri's in red):
  
  <img src="https://github.com/yoavabadi/ProjectInfo/blob/master/aggregation_diff.PNG" width="200">

* #### Feature To Envelope

  This tool Creates an Envelope from a Feature layer.
  

* #### Features To Point

  This tool Creates a Points Features of true centroid from feature layer.
  

* #### Flip Lines

  This tool Flips polyline's end and start vertices directions.
  

* #### Feature Vertices To Points

  This tool Creates Points from feature's vertices.
  

* #### Split Line At Vertices

  This tool Split Line At Vertices
  ##### Known Issues:
   * Not Optimal solution - based on a convex hull method
   * Way to improve - check angles and extend polygons in the angles' directions
  
  
## Licensing
Licensed under the Apache License, Version 2.0 (the "License").
A copy of the license is available in the repository's [License.txt](/LICENSE) file.
