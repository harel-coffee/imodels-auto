# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] tags=[]
# # Setup

# %%
# %load_ext autoreload
# %autoreload 2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree, DecisionTreeClassifier
from sklearn import metrics

# installable with: `pip install imodels`
import sys,os
sys.path.append(os.path.expanduser('~/imodels'))

import imodels
from imodels import FIGSClassifier
import demo_helper
np.random.seed(13)

# %% [markdown] pycharm={"name": "#%% md\n"}
# Let's start by loading some data in...  
# Note, weed to still load the reg dataset first to get the same splits as in `imodels_demo.ipynb` due to the call to random

# %% pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
# ames housing dataset: https://www.openml.org/search?type=data&status=active&id=43926
X_train_reg, X_test_reg, y_train_reg, y_test_reg, feat_names_reg = demo_helper.get_ames_data()

# diabetes dataset: https://www.openml.org/search?type=data&sort=runs&id=37&status=active
X_train, X_test, y_train, y_test, feat_names = demo_helper.get_diabetes_data()
    # feat_names meanings:
    # ["#Pregnant", "Glucose concentration test", "Blood pressure(mmHg)",
    # "Triceps skin fold thickness(mm)",
    # "2-Hour serum insulin (mu U/ml)", "Body mass index", "Diabetes pedigree function", "Age (years)"]

# load some data
# print('Regression data training', X_train_reg.shape, 'Classification data training', X_train.shape)

# %% [markdown] tags=[]
# # FIGS

# %%
model_figs = FIGSClassifier(max_rules=7)

# %% pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
# specify a decision tree with a maximum depth
model_figs.fit(X_train, y_train, feature_names=feat_names);

# %%
# calculate mse on the training data
# probs = figs.predict_proba(X_test)
# print(f'test mse: {np.mean(np.square(preds-y)):0.2f}')
# demo_helper.viz_classification_preds(probs, y_test)

# %%
print(model_figs)

# %%
print(model_figs.print_tree(X_train, y_train))

# %%
model_figs.plot(fig_size=7)

# %% [markdown] tags=[]
# # DEV

# %%
# figs_tree = model_figs.trees_[0]

# %%
from imodels.tree.viz_utils import extract_sklearn_tree_from_figs
dt = extract_sklearn_tree_from_figs(model_figs, tree_num=0, n_classes=2)

# %%
plot_tree(dt, feature_names=feat_names);

# %% [markdown]
# ## `sklearn` Comparison

# %%
model_sklearn = DecisionTreeClassifier(max_depth=10, random_state=42)
model_sklearn.fit(X_train, y_train);

# %%
plot_tree(model_sklearn, feature_names=feat_names, max_depth=2);
