# C++ code snippets
Various code snippets for Blender

* ### blender_copyBoneTransforms.py
    
  Copies bone transforms from **InputObj** to **Armature** object.

  ##### Keep in mind:
    *Global Transforms Only: The script copies global transforms, not local ones. Make sure to align root bones properly before running the script.
-   *Matching Bones**: Only bones with matching names will be copied. Any bones without a match will need manual adjustment.
