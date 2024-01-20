import numpy as np
import pandas as pd

sep = ';'
coding = 'windows-1251'
filePath1 = 'resources/file1.csv'
filePath2 = 'resources/file2.csv'
filePathResult = 'result/result_file.csv'

if __name__ == "__main__":
    fileDataFrame1 = pd.read_csv(filePath1, encoding=coding, sep=sep)
    fileDataFrame2 = pd.read_csv(filePath2, encoding=coding, sep=sep)

    titleRow = fileDataFrame1.columns.tolist()

    fileDataFrame1.replace(np.nan, 'None', inplace=True)
    fileDataFrame2.replace(np.nan, 'None', inplace=True)

    csvContentList1 = fileDataFrame1.values.tolist()
    csvContentList2 = fileDataFrame2.values.tolist()

    csvContentSet1 = set(map(tuple, csvContentList1))
    csvContentSet2 = set(map(tuple, csvContentList2))

    df = pd.DataFrame(list(csvContentSet1.symmetric_difference(csvContentSet2)), columns=titleRow)

    df.to_csv(filePathResult, encoding=coding, sep=sep, index=False)
