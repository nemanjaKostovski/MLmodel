import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import scikitplot as skplt
import seaborn as sns

df = pd.read_csv('Bazaproizvodnjaprofila1.csv')
X = df[['Rm', 'Rp', 'A%', 'Wb']].values
y = df[['Alloy']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

model = LogisticRegression(max_iter=8500)
model.fit(X_train, y_train.ravel())

y_pred = model.predict(X_test)

sns.relplot(data=df, x="Rm", y="A%", hue="Alloy", alpha=0.8)

skplt.metrics.plot_confusion_matrix(
    y_test, 
    y_pred,
    figsize=(12,12),
    text_fontsize=20,
    title_fontsize=20)

import pickle
with open('alloys_model.pkl', 'wb') as file:
    pickle.dump(model, file)
