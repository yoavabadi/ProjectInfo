'''-------------------------------------------------------------------------------
 Tool Name:   SymmetricDifference
 Source Name: SymmetricDifference.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Creates a Symmetric Difference layer
 from source layer and overlay layer
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class SymmetricDifference(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Symmetric Difference"
        self.description = "Creates a Symmetric Difference layer " \
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

        param1 = arcpy.Parameter(name="symmetric_layer",
                                 displayName="Symmetric Difference Layer",
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
        symmetric_layer = parameters[1].valueAsText
        output_layer = parameters[2].valueAsText

        in_geometry = arcpy.Dissolve_management(in_layer, arcpy.Geometry())[0]
        symmetric_difference_geometry = arcpy.Dissolve_management(symmetric_layer, arcpy.Geometry())[0]
        symmetric_difference_geometry = [in_geometry.symmetricDifference(symmetric_difference_geometry)]
        symmetric_difference_geometry = arcpy.Dissolve_management(symmetric_difference_geometry,
                                                                  arcpy.Geometry(), multi_part="SINGLE_PART")
        return arcpy.SpatialJoin_analysis(symmetric_difference_geometry, in_layer, output_layer)
