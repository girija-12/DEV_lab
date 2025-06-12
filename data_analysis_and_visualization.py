import pandas as pd
import matplotlib.pyplot as plt
data={'Name': ['Liora Voss', 'Zaden Kline', 'Talia Moss', 'Joren Vale', 'Selene Frost'],
      'Age':[28,28,29,28,29],
      'Survival_Score':[96,97,85,79,80]}
df=pd.DataFrame(data)
print("Dataframe:\n",df)
print("\nData Analysis:")
print("Mean Age:",df['Age'].mean())
print("Maximum Survival Score:",df['Survival_Score'].max())
print("Minimum Survival Score:",df['Survival_Score'].min())
plt.figure(figsize=(8,4))
plt.bar(df['Name'],df['Survival_Score'])
plt.xlabel('Name')
plt.ylabel('Survival Score')
plt.title('Survival Score of Players')
plt.show()
