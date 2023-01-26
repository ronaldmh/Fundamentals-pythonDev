import arcpy

shapefile = "D:\ProgrammerAnalyst\Semestrer3\CodeMyself\python\shp\isla.shp"

desc = arcpy.Describe(shapefile)
print("Shapefile type: " + desc.shapeType)
fields = arcpy.ListFields(shapefile)
for field in fields:
    print(field.name)