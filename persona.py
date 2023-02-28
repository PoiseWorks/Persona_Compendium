import openpyxl


class Persona:  # Class for persona formatted info
    def __init__(self, name, arcana, level, main_attribute):
        self.name = name
        self.arcana = arcana
        self.level = level
        self.main_attribute = main_attribute

    def info(self):
        return (f"Name: {self.name}\n"
                f"Arcana: {self.arcana}\n"
                f"Level: {self.level}\n"
                f"Main attribute: {self.main_attribute}")


Compendium = {}  # The dict with all the personas


# Getting the info from an Excel sheet

wb = openpyxl.load_workbook("datasets/Compendium.xlsx")
ws = wb.active
cell_range = 'A1:D243'
persona_list = [[cell.value for cell in row] for row in ws[cell_range]]

# Putting the info in the dict

for a in persona_list:
    Compendium[a[0]] = Persona(a[0],
                               a[1],
                               a[2],
                               a[3])

# Persona images

Images = {}

Images["Alice"] = "images/Alice.png"

