# Task 5: Exploratory Data Analysis (EDA)

# Objective:
- Extract insights using visual and statistical exploration.

# Dataset
**Titanic Dataset** → train.csv

# Steps Performed
1. **Data Loading**
   - Load `train.csv` into a pandas DataFrame.

2. **Data Cleaning**
   - Removed duplicate rows.
   - Converted `Pclass` column to categorical type.
   - Filled missing `Embarked` values with the mode.
   - Filled missing `Fare` values with the median.
   - Created `HasCabin` binary feature.

3. **Feature Engineering**
   - Extracted passenger title from the `Name` column.
   - Created `FamilySize` from `SibSp` and `Parch`.
   - Created `IsAlone` feature.
   - Binned ages into categories (`Child`, `Teen`, `YoungAdult`, `Adult`, `Senior`).
   - Binned fares into quartiles.

4. **Saving Outputs**
   - Saved cleaned dataset as `train_cleaned.csv`.
   - Saved visualizations in `figures/` folder.

## Files in This Project
- **train.csv** →  Titanic dataset.
- **train_cleaned.csv** → Cleaned and processed dataset.
- **train.py** → Python script for cleaning.

