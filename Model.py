import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("Pos_Pakaging_Quan_Day1.csv")
df_model = df.copy()
#print(df_model)


# Separate features and target

#print(X)
X = df_model[['Quan_pag_max_day', 'month', 'Quan_pos', 'Time_length', 'Differ_mean', 'Differ_median_day_pos_pag']]
y = df_model['Re_es']
numerical_cols = X.columns


preprocessor = ColumnTransformer(
    transformers=[
        ('num', MinMaxScaler(), numerical_cols)  # Standardize numerical features
    ])

X_encoded = preprocessor.fit_transform(X)

# Fit the LOF model to identify outliers
lof = LocalOutlierFactor(n_neighbors=15, contamination=0.05)  # You can adjust n_neighbors and contamination as needed
outlier_labels = lof.fit_predict(X_encoded)


# Filter out the outliers
X_no_outliers = X[outlier_labels != -1]
y_no_outliers = y[outlier_labels != -1]

model = Pipeline(steps=[
('preprocessor', preprocessor),
# 0.69, 0.6, 15
('regressor', GradientBoostingRegressor(n_estimators= 100, learning_rate= 0.15))
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_no_outliers, y_no_outliers, test_size=0.3, random_state= 42)

# Train the model
model.fit(X_train, y_train)



with open('model.pkl', 'wb') as file:
    joblib.dump(model, 'model.pkl')
    
# input_data = [[60, 11, 720, 30, 408.571429, 5.0]]
# input_df = pd.DataFrame(input_data, columns=X_train.columns)

# # Nạp mô hình đã lưu
# loaded_model = joblib.load('model.pkl')

# # Thực hiện dự đoán
# result = loaded_model.predict(input_df)
# print(result)