# -*- coding: utf-8 -*-
"""credit_card_fd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ckbr2Cl6TwY_ftaTzCbpXawBhl2AvclE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.under_sampling import RandomUnderSampler

df = pd.read_csv('/content/creditcard.csv')

df.head()

df.tail()

df.info()

df.isnull().sum()

df=df.dropna()

print("unique value in class festure",df['Class'].unique())
df['Class'].value_counts()

fraud=df[df.Class==1]
Notfraud=df[df.Class==0]
print(fraud.shape)
print(Notfraud.shape)

Notfraud=Notfraud.sample(492)
df2=pd.concat([Notfraud,fraud],axis=0)
df2.shape

corr_mat = df2.corr(method='pearson')

# Set the figure size to 20x20 inches for better readability
plt.figure(figsize=(20, 20))

# Create the heatmap with annotations and customized appearance
sns.heatmap(corr_mat,
            annot=True,        # Annotate each cell with the correlation coefficient
            fmt="0.2f",        # Format the annotations to 2 decimal places
            square=True,       # Make each cell square-shaped
            cmap="plasma",     # Use the 'plasma' colormap
            linewidths=0.8,    # Set the width of the lines between cells to 0.8 points
            linecolor="Black") # Set the color of the lines between cells to black

# Add a title to the heatmap
plt.title("Correlation Matrix for Credit Card Fraud Detection")

# Display the heatmap
plt.show()

h_feature=corr_mat.index[abs(corr_mat['Class'])>=0.1].tolist()
h_feature.remove('Class')
h_feature

x=df2[h_feature]
y=df2['Class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=42)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

logistic=LogisticRegression(max_iter=10000)
logistic.fit(x_train,y_train)

y_pred=logistic.predict(x_test)
acc=accuracy_score(y_test,y_pred)

print(f"accuracy score = {acc}")

undersample = RandomUnderSampler(sampling_strategy='majority', random_state=42)
X_res, y_res = undersample.fit_resample(x, y)
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
# Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))