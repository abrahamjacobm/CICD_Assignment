import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
#--- to remove------
import os
#-------------
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the CSV file
csv_file_path = os.path.join(script_dir, 'data', 'train.csv')

# Load the CSV file
df = pd.read_csv(csv_file_path)
#df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

model = LogisticRegression().fit(X, y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
