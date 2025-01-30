import pandas as pd
data = pd.read_csv('username.csv')
df = pd.DataFrame(data)
print("les 5 premières lignes :")
print(df.head())
#print(df)
avg_age = df['Age'].mean()
print(avg_age)
