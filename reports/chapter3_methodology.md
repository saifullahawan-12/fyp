# Chapter 3: Methodology

## 3.1 Overview of the Proposed Architecture
The proposed system architecture for detecting malicious ownership transactions is designed in a modular fashion, consisting of four primary phases: Data Collection, Data Preprocessing, Behavior Modeling (Anomaly Detection), and the Alert Generation Dashboard. For the Phase 1 (Semester 7) prototype, the architecture relies on synthetic behavioral data to train and validate the core machine learning engine before scaling to live browser data in Phase 2.

## 3.2 Data Collection Strategy
Because real-world datasets of compromised extensions are difficult to obtain and often lack continuous temporal logs, a synthetic dataset was generated to simulate the real-world behavior of browser extensions over a period of weeks. The script `generate_sample_dataset.py` was developed to create 1,000 extension behavior logs. 
The dataset captures four primary features:
- **Permissions_Count:** The number of permissions requested by the extension (e.g., accessing tabs, storage, or web requests).
- **Network_Requests:** The volume of external network requests made by the extension per week.
- **Cookie_Access:** A binary indicator (0 or 1) representing whether the extension accesses browser cookies.
- **API_Calls:** The frequency of interaction with sensitive browser APIs.

The dataset mimics "Behavioral Drift" by injecting anomalies (approximately 10% of the dataset) where extensions suddenly exhibit dramatic spikes in network requests and permission counts, representing the behavior of an extension that has just undergone a malicious ownership transaction.

## 3.3 Data Preprocessing
Machine learning algorithms are sensitive to the scale of the input data. Therefore, the raw behavioral data was cleaned and normalized using `preprocess.py`. 
- **Encoding:** The categorical target labels ("Normal" and "Suspicious") were transformed into numerical formats (0 and 1) using Scikit-Learn's `LabelEncoder`.
- **Feature Scaling:** The numerical features (`Permissions_Count`, `Network_Requests`, etc.) were standardized using `StandardScaler`. This transforms the data so that each feature has a mean of 0 and a standard deviation of 1. This step is crucial for distance-based anomaly detection algorithms to ensure no single feature disproportionately influences the model. The fitted scaler was saved to disk to ensure live tests in the dashboard are scaled identically.

## 3.4 Behavior Modeling using Isolation Forest
To detect behavioral drift, an unsupervised anomaly detection algorithm—the **Isolation Forest**—was selected. 
Unlike traditional classifiers that attempt to build a profile of "normal" data, an Isolation Forest works by isolating anomalies. It does this by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of that feature. 
Since anomalies are "few and different," they require fewer random splits to be isolated from the rest of the dataset compared to normal points. 
This makes Isolation Forest highly effective and computationally lightweight for detecting zero-day extension threats. If a benign extension is updated by a malicious buyer, its sudden spike in network activity and permissions will place it far outside the dense cluster of normal behavior, allowing the model to instantly flag it as a highly suspicious anomaly without needing a predefined malware signature.
