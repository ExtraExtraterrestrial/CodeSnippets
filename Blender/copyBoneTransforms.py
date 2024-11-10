import bpy
from mathutils import Matrix

outputObj_name = 'Armature'
inputObj_name = 'InputObj'

outputObj = bpy.data.objects[outputObj_name]
inputObj = bpy.data.objects[inputObj_name]

bpy.ops.object.mode_set(mode='OBJECT')

output_matrix_global = outputObj.matrix_world
input_matrix_global = inputObj.matrix_world
inverse_output_matrix_global = output_matrix_global.inverted()

bpy.ops.object.mode_set(mode='EDIT')

for oBone in outputObj.data.edit_bones:
    for iBone in inputObj.data.edit_bones:
        if oBone.name == iBone.name:
            input_head_global = input_matrix_global @ iBone.head
            input_tail_global = input_matrix_global @ iBone.tail
            oBone.head = inverse_output_matrix_global @ input_head_global
            oBone.tail = inverse_output_matrix_global @ input_tail_global

bpy.ops.object.mode_set(mode='OBJECT')