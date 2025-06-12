# Create CSV file
import pandas as pd
pddata={"Sender":['alice@example.com','bob@example.com','alice@example.com'],
        'Receiver':['bob@example.com','alice@example.com','carol@example.com'],
        'Subject':['Hello','Meeting reminder','Project update'],
        'timestamp':['2023-08-01 10:00:00','2023-08-02 14:30:00','2023-08-03 09:15:00'],
        'Content':['Hi Bob,\nHow are you?','Hi Alice,\nDon\'t forget the meeting at 3PM.','Hi Carol,\n Here\'s the lastest project update.']}
df=pd.DataFrame(pddata)
df['timestamp']=pd.to_datetime(df['timestamp'])
df.to_csv('email_data.csv',index=False)
print("CSV file created successfully!")

# Exploratory Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('email_data.csv')
df.info()
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.dropna(inplace=True)

df['email_length'] = df['Content'].apply(len)
plt.figure(figsize=(10,6))
sns.histplot(df['email_length'], bins=30, kde=True)
plt.title('Distribution of Email Content Length')
plt.xlabel('Email Length')
plt.ylabel('Count')
plt.show()

top_senders = df['Sender'].value_counts()[:10]
plt.figure(figsize=(12,6))
sns.barplot(x=top_senders.index, y=top_senders.values)
plt.title('Top 10 email senders')
plt.xlabel('Senders')
plt.ylabel('Number of Emails')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
