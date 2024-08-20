import pandas as pd
import os

folderPath = 'large_test_data/simExcel'

excels = os.listdir(folderPath)

for excel in excels:
    excelPath = os.path.join(folderPath, excel)

    df = pd.read_excel(excelPath)
    df_sorted = df.sort_values(by='Comp score', ascending=False)
    df_sorted.to_excel(excelPath, index=False)
