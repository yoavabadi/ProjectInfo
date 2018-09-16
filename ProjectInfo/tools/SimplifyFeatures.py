'''-------------------------------------------------------------------------------
 Tool Name:   SimplifyFeatures
 Source Name: SimplifyFeatures.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Simplify Polygons \ Polyline Features, by a tolerance distance
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class SimplifyFeatures(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Simplify Features"
        self.description = "Simplify Polygons \ Polyline Features, by a tolerance distance."
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

        # Using the "arcpy.Geometry" object's generalize method,
        # which simplify the geometry by a distance tolerance between vertices
        in_geometries = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())
        result_geometry = [feature.generalize(tolerance) for feature in in_geometries]
        return arcpy.CopyFeatures_management(result_geometry, out_layer)
