## In this script, we'll explore how to transform some of the the remaining features so we can use them in our model


## Introduction

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
print(train_null_counts)
df_no_mv = train[train_null_counts[train_null_counts==0].index]


## Categorical variables

text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    print(col+":", len(train[col].unique()))
    train[col] = train[col].astype('category')
    
train['Utilities'].cat.codes.value_counts()


## Dummy Coding

dummy_cols = pd.DataFrame()
for col in text_cols:
    col_dummies = pd.get_dummies(train[col])
    train = pd.concat([train, col_dummies], axis=1)
    del train[col]
    
print(train.shape)


## Transforming Improper Numerical Features

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
df_missing_values = train[train_null_counts[(train_null_counts>0) & (train_null_counts<584)].index]

print(df_missing_values.isnull().sum())
print(df_missing_values.dtypes)


## Imputing Missing Values

float_cols = df_missing_values.select_dtypes(include=['float'])
float_cols = float_cols.fillna(df_missing_values.mean())

print(float_cols.isnull().sum())

train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']



## END
