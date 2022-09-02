import pandas as pd

def filereading():
    df = pd.read_csv("sampledata.csv")
    return df

print(filereading())
