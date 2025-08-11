# Load data & initial inspection
import pandas as pd

df = pd.read_csv('train.csv')
print(df.shape)
print(df.head())
df.info()
df.describe()
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert types
df['Pclass'] = df['Pclass'].astype('category')

# Impute Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Impute Fare with median if missing
if df['Fare'].isnull().sum() > 0:
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Create HasCabin flag
df['HasCabin'] = df['Cabin'].notnull().astype(int)

# Feature engineering
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Consolidate rare titles
rare_titles = ['Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona']
df['Title'] = df['Title'].replace(rare_titles, 'Rare')
df['Title'] = df['Title'].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# Fill missing Age with median per Title
df['Age'] = df['Age'].fillna(df.groupby('Title')['Age'].transform('median'))

# Age bins
df['AgeBin'] = pd.cut(df['Age'],
                      bins=[0,12,20,40,60,120],
                      labels=['Child','Teen','YoungAdult','Adult','Senior'])

# Fare bins
df['FareBin'] = pd.qcut(df['Fare'], 4, labels=False)

print(df.head())

# Save cleaned dataset
df.to_csv(r"C:/Users/HP/Desktop/INTERNSHIP TASK/Task 5/train_cleaned.csv", index=False)