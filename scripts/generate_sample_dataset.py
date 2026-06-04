import pandas as pd
import numpy as np
import random
import os

def generate_synthetic_data(num_records=1000):
    np.random.seed(42)
    random.seed(42)

    data = []
    for i in range(num_records):
        extension_id = f"ext_{random.randint(100, 999)}"
        
        # Determine if this row represents a normal behavior or suspicious drift
        # 10% chance of being suspicious
        is_suspicious = random.random() < 0.10
        
        if is_suspicious:
            permissions_count = random.randint(8, 20)  # Sudden increase
            network_requests = random.randint(50, 500) # High network activity
            cookie_access = 1 # Often accesses cookies
            api_calls = random.randint(100, 300)
            label = "Suspicious"
        else:
            permissions_count = random.randint(1, 5)   # Normal permissions
            network_requests = random.randint(0, 20)   # Normal network activity
            cookie_access = random.choice([0, 0, 0, 1]) # Rarely accesses cookies
            api_calls = random.randint(5, 50)
            label = "Normal"
            
        week = random.randint(1, 4) # Representing temporal data
        
        data.append({
            "Extension_ID": extension_id,
            "Week": week,
            "Permissions_Count": permissions_count,
            "Network_Requests": network_requests,
            "Cookie_Access": cookie_access,
            "API_Calls": api_calls,
            "Label": label
        })
        
    df = pd.DataFrame(data)
    
    # Save the file
    output_dir = os.path.join("..", "data", "raw_extensions")
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "sample_dataset.csv")
    df.to_csv(output_file, index=False)
    print(f"Successfully generated {num_records} records!")
    print(f"File saved to: {output_file}")
    
    # Show a preview
    print("\nData Preview:")
    print(df.head())
    print("\nLabel Distribution:")
    print(df['Label'].value_counts())

if __name__ == "__main__":
    generate_synthetic_data()
