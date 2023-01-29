# Comming back to arcpy library
import arcpy



shapefile = r"D:\ProgrammerAnalyst\Semestrer3\CodeMyself\python\shp"

if shapefile != "":
    print("OK")

'''

desc = arcpy.Describe(shapefile)
print("Shapefile type: " + desc.shapeType)
fields = arcpy.ListFields(shapefile)
for field in fields:
    print(field.name)

'''
