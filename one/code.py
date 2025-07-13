import pandas as pd

#1
df = pd.read_csv(r"data.csv")
df["Join_Date"]=pd.to_datetime(df["Join_Date"])

#2
df2 = df[(df["Salary"] > 5000) & (df["Join_Date"].dt.year >= 2020 )]


#3
df3 = df2.groupby("Department")["Salary"].mean()

#4
df4 = df3.to_frame().sort_values(by = "Salary", ascending = False)
print(df4)
