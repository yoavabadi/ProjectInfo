'''-------------------------------------------------------------------------------
 Toolbox Name: ProjectInfo
 Source Name:  ProjectInfo.pyt
 Version:      ArcGIS 10.1
 License:      Apache 2.0
 Author:       Yoav Abadi
 Updated by:   Yoav Abadi
 Description:

 History:      Initial coding - 16/09/2018, version 1.0
 Updated:
-------------------------------------------------------------------------------'''
import sys
import os

tools_dir = os.path.join(os.path.dirname(__file__), 'tools')
sys.path.append(tools_dir)
# Do not compile .pyc files for the tool modules.
sys.dont_write_bytecode = True

from SplitLines import SplitLines
from ConvexHull import ConvexHull
from Erase import Erase
from SymmetricDifference import SymmetricDifference
from PolygonToLine import PolygonToLine
from AggregatePolygons import AggregatePolygons
from SimplifyFeatures import SimplifyFeatures


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "ProjectInfoToolbox"
        self.alias = "Project Info Tool box"
        # List of tool classes associated with this toolbox
        self.tools = [SplitLines, ConvexHull, Erase, SymmetricDifference,
                      PolygonToLine, AggregatePolygons, SimplifyFeatures]
