import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
import joblib

def preprocess_data():
    input_file = os.path.join("..", "data", "raw_extensions", "sample_dataset.csv")
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run generate_sample_dataset.py first.")
        return
        
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    # 1. Handle Categorical Data
    # 'Extension_ID' is an identifier, not a feature. We can drop it for training.
    # 'Label' is our target variable. We encode Normal=0, Suspicious=1
    print("Encoding labels...")
    le = LabelEncoder()
    df['Label_Encoded'] = le.fit_transform(df['Label'])
    
    # 2. Select Features for Anomaly Detection
    features = ['Permissions_Count', 'Network_Requests', 'Cookie_Access', 'API_Calls']
    X = df[features]
    
    # 3. Normalize Data
    # Algorithms like Isolation Forest work better when data is on the same scale
    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Save the scaler so we can use it in the dashboard later
    model_dir = os.path.join("..", "models")
    os.makedirs(model_dir, exist_ok=True)
    scaler_path = os.path.join(model_dir, "scaler.pkl")
    joblib.dump(scaler, scaler_path)
    print(f"Scaler saved to: {scaler_path}")
    
    # Create a new dataframe with processed features
    df_processed = pd.DataFrame(X_scaled, columns=features)
    df_processed['Extension_ID'] = df['Extension_ID']
    df_processed['Week'] = df['Week']
    df_processed['Label'] = df['Label']
    df_processed['Label_Encoded'] = df['Label_Encoded']
    
    # Save the processed dataset
    output_file = os.path.join("..", "data", "processed", "processed_dataset.csv")
    df_processed.to_csv(output_file, index=False)
    
    print(f"\nPreprocessing Complete!")
    print(f"Processed file saved to: {output_file}")
    
    print("\nProcessed Data Preview:")
    print(df_processed.head())

if __name__ == "__main__":
    preprocess_data()
