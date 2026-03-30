import pandas as pd

df = pd.read_csv("sales_data.csv")
df.fillna(0, inplace=True)
df['total_amount'] = df['price'] * df['quantity']
df.to_csv("processed_data.csv", index=False)

print("ETL Pipeline executed successfully!")
