import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the datasets
try:
    train_df = pd.read_csv("Dataset.zip/Dataset/Train.csv")
    test_df = pd.read_csv("Dataset.zip/Dataset/Test.csv")
except FileNotFoundError:
    print("Ensure the dataset files are in the correct directory.")
    exit()


# Pre-process the training data
# Remove the row with a negative 'Avg_Worker_Wage_USD'
train_df = train_df[train_df['Avg_Worker_Wage_USD'] >= 0]

# Define features (X) and target (y)
features = [
    'Monthly_Output_Tonnes',
    'Yearly_Release_Count',
    'CO2_Emissions',
    'Water_Used_ML',
    'Waste_To_Landfill_Tonnes',
    'Avg_Worker_Wage_USD',
    'Weekly_Work_Hours'
]
target = 'Avg_fashion_item_Price'

X_train = train_df[features]
y_train = train_df[target]
X_test = test_df[features]

# Initialize and train the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Create the submission DataFrame
submission_df = pd.DataFrame({'Avg_fashion_item_Price': predictions})

# Save the submission file
submission_df.to_csv('Submission.csv', index=False)

print("Submission.csv file has been created successfully!")