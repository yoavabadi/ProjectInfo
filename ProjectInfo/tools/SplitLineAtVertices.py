'''-------------------------------------------------------------------------------
 Tool Name:   SplitLineAtVertices
 Source Name: SplitLineAtVertices.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Creates a PolyLine layer from a Polygon layer
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class SplitLineAtVertices(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Split Line At Vertices"
        self.description = "Split Line At Vertices"
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

        param0.filter.list = ["Polyline"]
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
        lines = []
        for geometry in geometries_list:
            # get the polylines' points
            points = geometry.getPart(0)
            # duplicate inner points to separate polyline
            # create a straight line for every two continuous points
            lines += [arcpy.Polyline(arcpy.Array([points.getObject(i),
                                                 points.getObject(i+1)])) for i in range(len(points) - 1)]
        return arcpy.CopyFeatures_management(lines, out_layer)
