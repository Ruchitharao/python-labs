import pandas as pd
from db import execute_values


def main():
    df = pd.read_csv('managers_data.csv')
    manager = []
    empid = []
    for inx, row in df.iterrows():
        manager_name = row[0]
        empids = list(row[1:].dropna().values)
        manager += [manager_name] * len(empids)
        empid += empids

    # data = pd.DataFrame(manager, columns=['Manager'])
    # data["Manager"] = data["Manager"].str.upper().str.title()
    # manager = data["manager"].values.tolist()

    df_emp_transpose = pd.DataFrame({'Manager': manager, 'EmpId': empid})
    df_emp_transpose["Manager"]= df_emp_transpose["Manager"].str.upper().str.title()
    print(df_emp_transpose)
    execute_values(df_emp_transpose, "managers")



if __name__ == "__main__":
     main()
