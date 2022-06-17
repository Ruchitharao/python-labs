import pandas as pd

df= pd.read_csv('managers_data.csv')


manager = []
empid = []

for inx, row in df.iterrows():
    manager_name = row[0]
    empids = list(row[1:].values)
    manager += [manager_name]*len(empids)
    empid += empids

df_emp_transpose = pd.DataFrame({'Manager':manager, 'Emp Ids': empid})
print(df_emp_transpose)