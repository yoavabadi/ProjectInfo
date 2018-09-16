'''-------------------------------------------------------------------------------
 Tool Name:   ConvexHull
 Source Name: ConvexHull.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Create a Convex Hull of input layer.
 This feature exists in ArcInfo, as part of the
 'Minimum Bounding Geometry' tool.
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class ConvexHull(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Convex Hull"
        self.description = "Create a Convex Hull of input layer. " \
                           "This feature exists in ArcInfo, as part of the " \
                           "'Minimum Bounding Geometry' tool."
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

        param2 = arcpy.Parameter(name="method",
                                 displayName="Method",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPString")

        params = [param0, param1, param2]
        params[2].filter.type = "ValueList"
        params[2].filter.list = ['NONE', 'ALL']
        params[2].value = 'NONE'

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
        method = parameters[2].valueAsText

        in_geometries = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())
        if method == 'ALL':
            in_geometries = arcpy.Dissolve_management(in_geometries, arcpy.Geometry())
        result_geometry = [line.convexHull() for line in in_geometries if line.convexHull().type == 'polygon']
        return arcpy.CopyFeatures_management(result_geometry, out_layer)
