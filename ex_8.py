import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('winequality-red.csv', sep=';')

print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

print("\nSummary statistics:\n", df.describe())

plt.figure(figsize=(8,5))
sns.countplot(x='quality', data=df, palette='viridis')
plt.title('Distribution of Wine Quality Ratings')
plt.show()

df.hist(bins=15, figsize=(15,10), layout=(4,3), color='teal')
plt.suptitle('Histograms of Features')
plt.show()

plt.figure(figsize=(12,8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()

selected_features = ['alcohol', 'sulphates', 'citric acid', 'quality']
sns.pairplot(df[selected_features], hue='quality', palette='bright')
plt.suptitle('Pairplot of Selected Features vs Quality', y=1.02)
plt.show()