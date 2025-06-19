import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('mpg').dropna()  

print("Original DataFrame head:")
print(df.head())

df_filtered = df[['mpg', 'cylinders', 'horsepower', 'weight']]

df_filtered = df_filtered[(df_filtered['mpg'] > 20) & (df_filtered['horsepower'] < 150)]

print("\nFiltered DataFrame head:")
print(df_filtered.head())

plt.figure(figsize=(10,6))
sns.scatterplot(data=df_filtered, x='horsepower', y='mpg', hue='cylinders', palette='viridis', s=100)

plt.title('Filtered Car Data: MPG vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('Miles Per Gallon (MPG)')
plt.grid(True)
plt.legend(title='Cylinders')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='cylinders', y='mpg', data=df_filtered, hue='cylinders', palette='Set2')

plt.title('MPG Distribution by Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Miles Per Gallon (MPG)')
plt.show()
