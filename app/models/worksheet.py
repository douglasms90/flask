from openpyxl import load_workbook


class createWorksheet():
  def __init__(self, path_xlsx):
    self.workbook = load_workbook(path_xlsx)
    self.worksheet = self.workbook.active

  def add_ob(self, ob, row):
    self.worksheet.cell(column=1, row=row).value = ob["column1"] # Quantidade
    self.worksheet.cell(column=2, row=row).value = ob["column2"] # Id
    self.worksheet.cell(column=3, row=row).value = ob["column3"] # Tomador
    self.worksheet.cell(column=4, row=row).value = ob["column4"] # Tipo
    self.worksheet.cell(column=5, row=row).value = ob["column5"] # Gerada
    self.worksheet.cell(column=6, row=row).value = ob["column6"] # Cliente
    self.worksheet.cell(column=7, row=row).value = ob["column7"] # Cobrança Vinculada / Defeito
    self.worksheet.cell(column=8, row=row).value = ob["column8"] # Distribuida
    self.worksheet.cell(column=9, row=row).value = ob["column9"] # Cidade
    self.worksheet.cell(column=10, row=row).value = ob["column10"] # Bairro
    self.worksheet.cell(column=11, row=row).value = ob["column11"] # Defeito

  def add_into_sheet(self, obj_list):
    for i, ob in enumerate(obj_list):
      self.add_ob(ob, i + 2)
  
  def save(self, path_file):
    self.workbook.save(path_file)