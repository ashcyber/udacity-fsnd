"""
    udacity fsnd 
    lesson2 practice program 2
    Renaming Files 
"""
location = "C:/Users/agsxpro/Downloads/prank/prank/"


import os
def rename_files():
    list_files = os.listdir(location)
    for i in list_files:
        new_name = i.translate(None, '0123456789')
        os.rename(location + i,location + new_name)
        
rename_files()
