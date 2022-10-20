import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1eymQW8paKYI7EUvBuNqtaMqv8rcMW5ROE_4nOS1BAMo')
worksheet = sh.sheet1

# res = worksheet.get_all_records()
# res = worksheet.get_all_values()
# res = worksheet.col_values(1)
# res = worksheet.get('A2:C2')
# print(res)

# user = ["Susan", 25, "Sydney"]
# worksheet.append_row(user)

# worksheet.update_cell(6, 2, 28)

worksheet.delete_rows(1)