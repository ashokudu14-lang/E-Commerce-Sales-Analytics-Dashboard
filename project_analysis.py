import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SampleSuperstore.csv', encoding='latin1')

df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

sales_by_category = df.groupby('Category')['Sales'].sum()
print(sales_by_category)

sales_by_category.plot(kind='bar', figsize=(8,5))
plt.title('Sales by Category')
plt.tight_layout()
plt.show()
