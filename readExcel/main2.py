# from openpyxl import load_workbook
# import openpyxl



# if __name__ == '__main__':
#     # 生成一个 Workbook 的实例化对象，wb即代表一个工作簿（一个 Excel 文件）
#     wb = openpyxl.Workbook()
#     # 获取活跃的工作表，ws代表wb(工作簿)的一个工作表
#     # 下面这个是之后要保存的结果表
#     ws = wb.active
#
#     # ws['A1'] = '(x,y)'
#     # ws['B1'] = '强度'
#     path1 = "D:\\Projects\\readExcel\\2022-1-28\\X-wave-1v.xlsx"
#     path2 = "D:\\Projects\\readExcel\\2022-1-28\\Y-Sn-1V.xlsx"
#     resultpath = "D:\\Projects\\readExcel\\2022-1-28\\result-1.xlsx"
#     # 1.打开 Excel 表格并获取表格名称
#     workbook1 = load_workbook(filename=path1)
#     workbook2 = load_workbook(filename=path2)
#     # 2.通过 sheet 名称获取表格
#     sheet1 = workbook1["Sheet1"]
#     sheet2 = workbook2["Sheet1"]
#     # 3.获取表格的尺寸大小(几行几列数据) 这里所说的尺寸大小，指的是 excel 表格中的数据有几行几列，针对的是不同的 sheet 而言。
#     print('sheet1.dimensions:'+sheet1.dimensions)  # 类似 "A0:B2"
#     print('sheet2.dimensions:'+sheet2.dimensions)
#     # 4.2sheet.cell(row=, column=)方式
#     # 5. 获取一系列格子
#     # 获取 整个矩形表格 区域的值
#     # cell1 = sheet1["A1:B2"]
#     # cell2 = sheet2["A1:B2"]
#
#     cell1 = sheet1[sheet1.dimensions]
#     cell2 = sheet2[sheet2.dimensions]
#
#     # count = 0
#     r = 2
#     # i[0] i[1] 表示 cell1 第i行 1、2 格; cell2同理
#     for i in cell1:  # 遍历 cell1 每一行，i 代表行
#         c = 2
#         # 设置列表头
#         ws.cell(row=r, column=1, value=i[0].value)
#         for j in cell2:
#             if r == 2:  # 当在第二行时，设置行表头
#                 ws.cell(row=1, column=c, value=j[0].value)
#             # ws.cell(row=r, column=c, value=str(i[0].value)+','+str(j[0].value))
#             ws.cell(row=r, column=c, value=i[1].value*j[1].value)
#             c += 1  # 先固定行
#             # print(str(i[0].value)+" "+str(j[0].value))
#             # count += 1
#             # if count == 10:
#             #     break
#         r += 1
#     wb.save(resultpath)
#     workbook1.save(path1)
#     workbook2.save(path2)
#     print("end")
