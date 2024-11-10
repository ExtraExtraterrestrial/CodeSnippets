# UE5 code snippets
Various code snippets for Unreal Engine 5

* ### UE5Utils_deleteCppClass.py
  This script is designed to remove the files of a specific C++ class.  It targets the files with the same name and with .cpp, .hpp, .h extensions in the analogous directories (ex. public/abc/def.cpp and private/abc/def.h). All these files are moved to a folder named UE5Utils_deleted located in the project's main directory.

  It also deletes the intermediate folder and the .sln files in the project directory.

  Once run, you can check the box "delete permanently" to delete the files normally.

  ##### Keep in mind:
  * The program doesn't overwrite the deleted file
  * If the program isn't set to delete the files permanently and files with matching names are present in the UE5Utils_deleted folder, the older files are renamed with a time signature prefix
