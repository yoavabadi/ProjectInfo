'''-------------------------------------------------------------------------------
 Tool Name:   FeaturesToPoint
 Source Name: FeaturesToPoint.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description:  Description: Creates a Points Features of true centroid from feature layer.
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class FeaturesToPoint(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Features To Point"
        self.description = "Creates a Points Features of true centroid from feature layer."
        self.canRunInBackground = False
        self.category = "Data Management"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(name="in_layer",
                                 displayName="Feature Layer",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        param1 = arcpy.Parameter(name="out_layer",
                                 displayName="Output Layer",
                                 direction="Output",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        params = [param0, param1]
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

        geometries_list = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())
        result_geometry = [arcpy.PointGeometry(polygon.centroid) for polygon in geometries_list]
        return arcpy.SpatialJoin_analysis(result_geometry, in_layer, out_layer)
