# -*- coding: utf-8 -*-
"""House price sales predictions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OwgrvuDblj9FU3z0Y6Rp9qqPXUW0UgjW
"""

from google.colab import drive
drive.mount("/content/House_Sales_Price_Prediction_2")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
import joblib  # Import joblib for model saving

# Calculate Relative Absolute Error (RAE)
def relative_absolute_error(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mean_target = y_true.mean()
    rae = mae / mean_target
    return rae

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the pyplot module from matplotlib for data visualization
import matplotlib.pyplot as plt

# Import the train_test_split function from scikit-learn for splitting the dataset
from sklearn.model_selection import train_test_split

# Read the CSV file containing the training data into a pandas DataFrame
train_data = pd.read_csv("/content/House_Sales_Price_Prediction_2/MyDrive/sales_price train.csv")

# Display the DataFrame (in an interactive environment like Jupyter Notebook, this would show the DataFrame)
train_data  # Note: This line is effective in an interactive environment like Jupyter Notebook.
            # If running as a script, you might want to use `print(train_data)` to see the output.

test_data=pd.read_csv("/content/House_Sales_Price_Prediction_2/MyDrive/sales_price test.csv")
(test_data)

import pandas as pd
from sklearn.model_selection import train_test_split

# Load your data (uncomment and modify the paths as necessary)
# train_data = pd.read_csv('path_to_train_data.csv')
# test_data = pd.read_csv('path_to_test_data.csv')

# Drop rows with missing target values
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)

# Separate target from predictors
y = train_data.SalePrice
X = train_data.drop(['SalePrice'], axis=1)

# Select only numerical columns (exclude object type)
X = X.select_dtypes(exclude=['object'])
X_test = test_data.select_dtypes(exclude=['object'])

# Split the data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

X_train.head()

(X_train.shape)

missing_value_count_num=(X_train.isnull().sum())
(missing_value_count_num[missing_value_count_num>0])

# Import the RandomForestRegressor class from the sklearn.ensemble module
from sklearn.ensemble import RandomForestRegressor

# Import the mean_absolute_error function from the sklearn.metrics module
from sklearn.metrics import mean_absolute_error

# Define a function to train a model and calculate the mean absolute error
def score_datasets(X_train, X_valid, y_train, y_valid):
    # Initialize the RandomForestRegressor model with 100 trees, a random state for reproducibility, and a max depth of 7
    model_1 = RandomForestRegressor(n_estimators=100, random_state=0, max_depth=7)

    # Fit the model to the training data (X_train, y_train)
    model_1.fit(X_train, y_train)

    # Predict the target values for the validation data (X_valid)
    preds = model_1.predict(X_valid)

    # Calculate and return the mean absolute error between the predicted and actual target values for the validation set
    return mean_absolute_error(y_valid, preds)

# Identify columns in the training set that contain missing values
missing_value_names = [col for col in X_train.columns
                       if X_train[col].isnull().any()]

# Drop columns with missing values from the training set
reduced_X_train = X_train.drop(missing_value_names, axis=1)

# Drop the same columns with missing values from the validation set
reduced_X_valid = X_valid.drop(missing_value_names, axis=1)

# Train a Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Print a header message to indicate the following output is for the MAE after dropping columns with missing values
print("MAE (Drop columns with missing values):")

# Call the function `score_datasets` with the reduced training and validation sets (after dropping columns with missing values),
# and the corresponding target values, then print the resulting MAE (Mean Absolute Error)
print(score_datasets(reduced_X_train, reduced_X_valid, y_train, y_valid))

from sklearn.impute import SimpleImputer
import pandas as pd

# Instantiate the SimpleImputer with a specified strategy (e.g., 'mean')
my_imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the training data and transform it
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))

# Transform the validation data
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Restore the original column names
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

print("MAE (Imputation):")
print(score_datasets(imputed_X_train, imputed_X_valid, y_train, y_valid))

# Calculate and print RAE for the validation set
rae_valid = relative_absolute_error(y_valid, preds_valid)
print("RAE (Your approach):")
print(rae_valid)

# Create a SimpleImputer object with the strategy of replacing missing values with the mean
final_imputer = SimpleImputer(strategy='mean')

# Impute missing values in the training set using the mean, and convert the result into a DataFrame
final_X_train = pd.DataFrame(final_imputer.fit_transform(X_train))

# Impute missing values in the test set using the mean (using the same imputer object as the training set), and convert the result into a DataFrame
final_X_test = pd.DataFrame(final_imputer.transform(X_test))

# Set the column names of the imputed training set to be the same as the original training set
final_X_train.columns = X_train.columns

# Set the column names of the imputed test set to be the same as the original test set
final_X_test.columns = X_test.columns

# Fit the final model on the entire training data
final_model = RandomForestRegressor(n_estimators=100, random_state=0)
final_model.fit(final_X_train, y_train)

# Save the final model using joblib
joblib.dump(final_model, 'final_model.joblib')

# Make predictions on the test data
final_preds_test = final_model.predict(final_X_test)

# Save test predictions to file
output_final = pd.DataFrame({'Id': test_data.index, 'SalePrice': final_preds_test})
output_final.to_csv('submission_final.csv', index=False)
print(output_final)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
import joblib

# Calculate Relative Absolute Error (RAE)
def relative_absolute_error(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mean_target = y_true.mean()
    rae = mae / mean_target
    return rae

# Load your data
train_data = pd.read_csv('/content/House_Sales_Price_Prediction_2/MyDrive/sales_price train.csv')
test_data = pd.read_csv('/content/House_Sales_Price_Prediction_2/MyDrive/sales_price test.csv')

# Drop rows with missing target values
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)

# Separate target from predictors
y = train_data.SalePrice
X = train_data.drop(['SalePrice'], axis=1)

# Select only numerical columns (exclude object type)
X = X.select_dtypes(exclude=['object'])
X_test = test_data.select_dtypes(exclude=['object'])

# Handle missing values by imputation
my_imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(my_imputer.fit_transform(X))
X_test_imputed = pd.DataFrame(my_imputer.transform(X_test))
X_imputed.columns = X.columns
X_test_imputed.columns = X_test.columns

# Split the data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X_imputed, y, train_size=0.8, test_size=0.2, random_state=0)

# Train a Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Calculate and print RAE for Linear Regression model
linear_preds_valid = linear_model.predict(X_valid)
linear_rae_valid = relative_absolute_error(y_valid, linear_preds_valid)
print("RAE (Linear Regression):", linear_rae_valid)

# Save the final model using joblib
joblib.dump(linear_model, 'linear_model.joblib')

# Make predictions on the test data
final_preds_test = linear_model.predict(X_test_imputed)

# Save test predictions to file
output_final = pd.DataFrame({'Id': test_data.index, 'SalePrice': final_preds_test})
output_final.to_csv('submission_final.csv', index=False)
print(output_final)

# Plot regression plot for each numeric column against SalePrice
plt.figure(figsize=(15, 10))
for column in X_imputed.columns:
    sns.regplot(x=column, y=y, data=train_data, scatter_kws={'alpha':0.3})
    plt.xlabel(column)
    plt.ylabel('SalePrice')
    plt.title(f'Regression plot of {column} against SalePrice')
    plt.show()