# The "Zero to Hero" Code Cheatsheet for Your Viva

If the panel asks you "How does the code work?", do not panic! You do not need to read the code line-by-line to them. You just need to explain the **logic** of what each file does in simple English. 

Here is exactly how to explain the 4 main Python scripts we wrote:

---

## 1. `generate_sample_dataset.py` (The Fake Data Maker)
**What it does:** It creates our raw data.
**How to explain it:** 
> *"To train a Machine Learning model, we needed thousands of examples of browser extension behavior. Since real-world data of compromised extensions is hard to find, I wrote a Python script using the `random` library to simulate 1,000 extensions. I programmed it so 90% of them have 'normal' numbers (like 2 permissions, 10 network requests) and 10% have 'suspicious' numbers (like 20 permissions, 5,000 network requests). It saves all this into a CSV file."*

## 2. `preprocess.py` (The Translator & Balancer)
**What it does:** It cleans the data so the AI can understand it.
**How to explain it:** 
> *"Machine Learning models only understand math, not English. This script does two things using the `scikit-learn` library. First, it uses a **LabelEncoder** to translate the words 'Normal' and 'Suspicious' into the numbers 0 and 1. Second, it uses a **StandardScaler**. If an extension has 5 permissions but 5,000 network requests, the AI might think network requests are more important just because the number is bigger. The scaler shrinks all numbers down into a balanced format (decimals between -3 and 3) so the AI treats all features fairly."*

## 3. `train_model.py` (The AI Brain)
**What it does:** It trains the Isolation Forest algorithm and creates the graphs.
**How to explain it:** 
> *"This is the core of the project. I used the `IsolationForest` algorithm from the `scikit-learn` library. I fed the preprocessed data into the model. The model works by drawing lines through the data; the extensions with normal numbers cluster together, but the extensions with crazy high numbers (the anomalies) get isolated quickly. After training, the script tests the model, prints out our 98% accuracy score, uses a library called `matplotlib` to draw the scatter plot graphs, and finally saves the trained model as a `.pkl` file using `joblib`."*

## 4. `dashboard.py` (The User Interface)
**What it does:** It builds the website and connects it to the AI.
**How to explain it:** 
> *"I used a Python library called `Streamlit` to build the web dashboard. Streamlit is great because it lets you build websites purely in Python without needing HTML/CSS. When a user goes to the 'Test Live Extension' tab and types in numbers, the script loads my saved `.pkl` AI model. It takes the user's numbers, scales them using the exact same scaler from step 2, and asks the AI to predict (1 for normal, -1 for anomaly). Based on that prediction, the dashboard instantly flashes a green Safe or red Suspicious message."*

---

### 💡 Quick Keyword Dictionary for the Panel
If they ask you what a specific word means:
- **`scikit-learn` (sklearn):** The main Python library used for Machine Learning. It contains the Isolation Forest algorithm.
- **`pandas`:** A Python library we used to read and edit the CSV (Excel-like) data tables.
- **`matplotlib` & `seaborn`:** The Python libraries we used to draw the charts and graphs.
- **`joblib`:** A library used to "save" the trained AI brain to the hard drive so we don't have to retrain it every time we open the dashboard.
- **`.pkl` (Pickle File):** The file format used by Python to save the trained Machine Learning model.
