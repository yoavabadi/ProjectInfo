'''-------------------------------------------------------------------------------
 Tool Name:   FlipLines
 Source Name: FlipLines.py
 Version:     ArcGIS 10.1
 License:     Apache 2.0
 Author:      Yoav Abadi
 Updated by:  Yoav Abadi
 Description: Flip polyline's end and start vertices.
 History:     Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import arcpy


class FlipLines(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Flip Lines"
        self.description = "Flip polyline's end and start vertices."
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

        polyline_geometries = arcpy.CopyFeatures_management(in_layer, arcpy.Geometry())

        flipped_lines = list()
        for line in polyline_geometries:
            line_array = line.getPart(0)  # single-part polyline => one line array (more then one element - multipart)
            reverse_line = arcpy.Polyline(
                arcpy.Array([line_array.getObject(i) for i in range(len(line_array) - 1, -1, -1)]))
            flipped_lines.append(reverse_line)
        return arcpy.CopyFeatures_management(flipped_lines, out_layer)

