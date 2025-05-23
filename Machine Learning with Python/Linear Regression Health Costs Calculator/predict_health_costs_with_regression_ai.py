# -*- coding: utf-8 -*-
"""freeCodeCamp_predict_health_costs_with_regression_AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n84-y4LV11hqZPc7Q7gT3-im_pw5R5xA
"""

# Commented out IPython magic to ensure Python compatibility.
# Import libraries. You may or may not use all of these.
!pip install -q git+https://github.com/tensorflow/docs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

# Import data
!wget https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv
dataset = pd.read_csv('insurance.csv')

# Create mappings for each categorical data
sex_mapping = {index:value for value, index in enumerate(dataset.sex.unique())}
smoker_mapping = {index:value for value, index in enumerate(dataset.smoker.unique())}
region_mapping = {index:value for value, index in enumerate(dataset.region.unique())}

# Replace categorical data in the dataset in place
dataset['sex'].replace(sex_mapping, inplace=True)
dataset['smoker'].replace(smoker_mapping, inplace=True)
dataset['region'].replace(region_mapping, inplace=True)

dataset = dataset.sample(frac=1).reset_index(drop=True)

# Calculate the number of rows for training and testing datasets
total_rows = dataset.shape[0]
train_size = int(0.8 * total_rows)

# Separate the dataset into training and testing datasets
train_dataset = dataset[:train_size]
test_dataset = dataset[train_size:]

train_labels = train_dataset.pop("expenses")
test_labels = test_dataset.pop("expenses")

# Creating the model
normalizer = layers.Normalization()
normalizer.adapt(np.array(train_dataset))

model = keras.Sequential([
    normalizer,
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1)
])

model.compile(
    optimizer = 'adam',
    loss = 'mae',
    metrics = ['mae', 'mse']
)
model.build()
model.summary()

# Training the model
history = model.fit(
    train_dataset,
    train_labels,
    epochs=100
)

# RUN THIS CELL TO TEST YOUR MODEL. DO NOT MODIFY CONTENTS.
# Test model by checking how well the model generalizes using the test set.
loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} expenses".format(mae))

if mae < 3500:
  print("You passed the challenge. Great job!")
else:
  print("The Mean Abs Error must be less than 3500. Keep trying.")

# Plot predictions.
test_predictions = model.predict(test_dataset).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)