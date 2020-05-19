from openpyxl import Workbook
wb = Workbook()
ws = wb.active
fp = open('data.txt', 'r')
list_row = fp.readlines()
list_source = []
ws['A1']='mingzi'
for i in list_row:
    list_source.append(i.split())
for row in list_source:
    ws.append(row)
wb.save("sample.xlsx")