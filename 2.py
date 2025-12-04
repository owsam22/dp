import pandas as pd

data={
    'Name':['Aliec','Bob','Alice','David','Eve','Frank','Eve'],
    'Age':[25,30,25,40,22,29,22],
    'Score':[85,90,85,88,95,70,95],
    'Extra':['x','y','x','z','w','k','w']
}

df=pd.DataFrame(data)
print(" Original data\n \n",df)

df=df.drop_duplicates()
print("\n Data after removing duplicates\n \n",df)

import matplotlib.pyplot as plt
plt.plot(df['Name'],df['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Name vs Score')
plt.show()

df=df.drop(columns=['Extra'])

df=df.dropna()

aggregrates_df=df.groupby('Age')[['Score']].mean().reset_index()
print("\n Reduced and Aggregrates data\n \n",aggregrates_df)
