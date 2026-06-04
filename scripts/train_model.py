import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os
import joblib

def train_isolation_forest():
    # 1. Load Processed Data
    input_file = os.path.join("..", "data", "processed", "processed_dataset.csv")
    if not os.path.exists(input_file):
        print("Data not found. Run preprocess.py first.")
        return
        
    df = pd.read_csv(input_file)
    
    # 2. Prepare Training Data
    # Isolation Forest is unsupervised for training, so we only give it the features
    features = ['Permissions_Count', 'Network_Requests', 'Cookie_Access', 'API_Calls']
    X = df[features]
    y_true = df['Label_Encoded'] # 0: Normal, 1: Suspicious
    
    # 3. Initialize and Train Model
    print("Training Isolation Forest Model...")
    # contamination is the expected proportion of outliers (we generated ~10%)
    model = IsolationForest(n_estimators=100, contamination=0.10, random_state=42)
    
    # Fit the model and predict
    # IF returns 1 for normal, -1 for anomaly. We convert this to 0 for normal, 1 for anomaly.
    predictions = model.fit_predict(X)
    y_pred = np.where(predictions == 1, 0, 1)
    
    # Calculate Anomaly Scores
    scores = model.decision_function(X)
    df['Anomaly_Score'] = scores
    df['Predicted_Label'] = y_pred
    
    # 4. Evaluate Model
    print("\n--- Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=["Normal", "Suspicious"]))
    
    # 5. Save the Model and Results Data
    model_dir = os.path.join("..", "models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "isolation_forest.pkl")
    joblib.dump(model, model_path)
    print(f"\nModel saved to: {model_path}")
    
    # Save the dataframe with predictions so the dashboard can read it
    results_path = os.path.join("..", "data", "processed", "results_dataset.csv")
    df.to_csv(results_path, index=False)
    print(f"Results dataset saved to: {results_path}")
    
    # 6. Generate Plots for Report
    report_dir = os.path.join("..", "reports")
    os.makedirs(report_dir, exist_ok=True)
    
    # Plot 1: Anomaly Score Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Anomaly_Score', hue='Label', bins=50, kde=True)
    plt.title("Distribution of Anomaly Scores (Normal vs Suspicious)")
    plt.xlabel("Anomaly Score (Lower means more anomalous)")
    plt.ylabel("Frequency")
    plot1_path = os.path.join(report_dir, "anomaly_scores_dist.png")
    plt.savefig(plot1_path)
    plt.close()
    
    # Plot 2: Scatter plot of Permissions vs Network Requests
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Permissions_Count', y='Network_Requests', 
                    hue='Predicted_Label', palette={0: 'blue', 1: 'red'}, alpha=0.6)
    plt.title("Isolation Forest Detection: Permissions vs Network Requests")
    plt.xlabel("Permissions Count (Scaled)")
    plt.ylabel("Network Requests (Scaled)")
    # Re-label legend
    plt.legend(title='Prediction', labels=['Suspicious', 'Normal'])
    plot2_path = os.path.join(report_dir, "anomaly_scatter.png")
    plt.savefig(plot2_path)
    plt.close()
    
    print(f"Plots saved to: {report_dir}")

if __name__ == "__main__":
    train_isolation_forest()
