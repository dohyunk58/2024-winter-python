from openpyxl import load_workbook

wb = load_workbook('./2024-winter-python/day6/3000words.xlsx',
                   read_only=False,  # 읽기 전용(읽기 전용에 최적화되어 파일을 불러온다)
                   # False면 셀안 공식을 가져오고 True면 공식 적용된 값만을 불러온다.
                   data_only=True, # True: 수식이 아닌 값을 가져옴
                   )
sheet1 = wb['Sheet1']  # Sheet1 시트를 가져오기.

sheet1['E2'].value = 'one' #E2의 값을 "one"으로 변경
wb.save(filename='./2024-winter-python/day6/study.xlsx') #study.xlsx로 새로쓰기.