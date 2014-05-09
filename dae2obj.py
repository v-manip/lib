# simple script to batch convert collada to obj.
# run as:
# blender --background --python dae2obj.py -- input_file output_file
 
import os
import sys
import glob
import bpy
 
if len(sys.argv) != 7:
	print("Must provide input and output file")
else:
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()
	bpy.ops.wm.collada_import(filepath=sys.argv[5])
	bpy.ops.export_scene.obj(filepath=sys.argv[6])
