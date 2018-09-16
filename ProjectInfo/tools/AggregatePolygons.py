'''-------------------------------------------------------------------------------
 Tool Name:   AggregatePolygons
 Source Name: AggregatePolygons.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Aggregate Polygons by a convex hull method - not ideal
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
 Known Issues:
   * Not Optimal solution - based on a convex hull method
   * Way to improve - check angles and extend polygons in the angles' directions
-------------------------------------------------------------------------------'''
import arcpy


class AggregatePolygons(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Aggregate Polygons"
        self.description = "Create an aggregation layer of the input polygons, " \
                           "aggregated by a tolerance distance, with convex hull."
        self.canRunInBackground = False
        self.category = "Data Management"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(name="in_layer",
                                 displayName="Line Layer",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        param1 = arcpy.Parameter(name="out_layer",
                                 displayName="Output Layer",
                                 direction="Output",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        param2 = arcpy.Parameter(name="tolerance",
                                 displayName="Tolerance Distance",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPDouble")

        params = [param0, param1, param2]
        params[2].value = 10.0

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        in_layer = parameters[0].valueAsText
        out_layer = parameters[1].valueAsText
        tolerance = float(parameters[2].valueAsText)

        in_geometries = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())
        out_geometries = []
        for polygon in in_geometries:
            # Get all features in tolerance distance from current iterated polygon
            polygons_in_range = [feature for feature in in_geometries if polygon.distanceTo(feature) <= tolerance]
            # Union said features with a dissolve, in case that the features does not overlap
            union_polygon = arcpy.Dissolve_management(polygons_in_range, arcpy.Geometry())
            # Convex hull aggregates the features together
            convex_polygon = union_polygon[0].convexHull()
            out_geometries.append(convex_polygon)
        arcpy.Dissolve_management(out_geometries, out_layer, multi_part="SINGLE_PART")
