# -*- coding: utf-8 -*-
"""Titanic_survival_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xu1M8_laVyOz3Pr8N0g8KBl2OHKbdZAz
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv('/Titanic-Dataset.csv')

df.head()

df.tail()

df.info()

df.isnull().sum()

df.drop(columns=['Age','Cabin'],inplace=True)

df.columns

df.head(10)

survive_count = df['Survived'].sum()
death_count = (df['Survived']==0).sum()
# Labels and values
labels = ['Survived', 'Death']
values = [survive_count, death_count]

# Create bar chart
plt.bar(labels, values, color=['blue', 'red'])

# Add labels and title
plt.xlabel('Boolean Value')
plt.ylabel('Count')
plt.title('Count of survivors and death')

# Show the plot
plt.show()

sns.barplot(x='Sex',y='Survived',data=df)
df.groupby('Sex',as_index=False).Survived.mean()

correlation_matrix = df[['Fare', 'Survived']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

"""Train Data"""

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Verify the conversion
print(df.head())

x = df[['Pclass','Sex']]
y = df[['Survived']]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Reshape y_train and y_test
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

from sklearn.linear_model import LogisticRegression
log = LogisticRegression(random_state=0)
log.fit(x_train,y_train)

"""Model Prediction"""

pred = print(log.predict(x_test))

print(y_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
y_pred = log.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')