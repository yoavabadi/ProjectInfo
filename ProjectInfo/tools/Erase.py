'''-------------------------------------------------------------------------------
 Tool Name:   Erase
 Source Name: Erase.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Creates an Erase (difference) layer
 from source layer and overlay layer
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class Erase(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Erase"
        self.description = "Creates an Erase (difference) layer " \
                           "from source layer and overly layer"
        self.canRunInBackground = False
        self.category = "Data Management"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(name="in_layer",
                                 displayName="Line Layer",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        param1 = arcpy.Parameter(name="erase_layer",
                                 displayName="Erase Layer",
                                 direction="Input",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        param2 = arcpy.Parameter(name="output_layer",
                                 displayName="Output Layer",
                                 direction="Output",
                                 parameterType="Required",
                                 datatype="GPFeatureLayer")

        params = [param0, param1, param2]
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
        erase_layer = parameters[1].valueAsText
        output_layer = parameters[2].valueAsText

        in_geometries = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())
        dissolve_erase_geometry = arcpy.Dissolve_management(erase_layer, arcpy.Geometry())[0]
        erase_result_geometry = [polygon.difference(dissolve_erase_geometry) for polygon in in_geometries]
        return arcpy.SpatialJoin_analysis(erase_result_geometry, in_layer, output_layer)
