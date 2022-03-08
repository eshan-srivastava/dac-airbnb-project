# Input Folder

This folder contains your cleaned and split datasets. After basic preprocessing and EDA has been done, we split the 'data/final_train.csv' into three datasets:

**1. `input/train.csv`:** Contains data to be used for model training only.
<br>

**2. `input/validation.csv`:** Contains the data that you use to evaluate your model's performance **WHILE TRAINING**
<br>

**3. `input/test.csv`:** Contains data to be used for evaluating model performance **AFTER TRAINING**. This is supposed to simulate unseen data that your model will come across.
<br>


This folder may also contain word embeddings, processed audio files, images etc. The idea is that this folder contains the inputs that you can directly feed into the model with **NO FURTHER PROCESSING**.