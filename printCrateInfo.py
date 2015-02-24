#!BPY

"""
Name: Crate
Blender: 259
Group: 'Export'
Tooltip: 'Prints vertices and polygons to console'
"""

"""
Reference:
http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Export_scripts
"""

import bpy

crateMesh = bpy.data.meshes["Crate"];
vertices = list(crateMesh.vertices);
polygons = list(crateMesh.polygons);

for v in vertices:
    print(v.co)
    
for p in polygons:
    string = "polygon"
    for v in list(p.vertices):
        string += " %i" % (v)
        
    print(string)