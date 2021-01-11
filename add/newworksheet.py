from openpyxl import Workbook 


wb = Workbook()

ws = wb.active

ws.append(['O.S', 'Defeito', 'Tipo', 'Gerada', 'Cliente', 'Cobrança Vinculada', 'Distribuída', 'Cidade', 'Bairro', 'Técnico Responsável'])

wb.save("sample.xlsx")
