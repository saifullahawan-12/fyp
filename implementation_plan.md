# Viva Presentation UI: Streamlit Dashboard Plan

You make a great point! Presenting just black-and-white terminal code during a Viva is often not very impressive to professors. They usually want to see a user interface (UI) to understand what the project actually *does*.

According to your original roadmap (Phase 11), a dashboard was planned for Semester 8, but since it is very easy to do, **we can build a simple one right now for your Semester 7 Viva!** 

## User Review Required

I propose we build a simple web app using **Streamlit** (as mentioned in your roadmap). It is a Python library specifically designed for making ML dashboards easily. 

**What the dashboard will have:**
1. A clean web page with a sidebar.
2. A table showing the browser extensions and their behavior (Network requests, permissions, etc.).
3. A "Risk Score" and "Status" (Normal vs. Suspicious) for each extension based on our Isolation Forest model.
4. The beautiful charts we generated earlier, displayed right on the website.

**Question for you:** Would you like me to go ahead and build this Streamlit dashboard right now so you have a proper website to show during your presentation? 

## Proposed Changes

### 1. Install Streamlit
- I will run `pip install streamlit` in your environment.

### 2. Create the Dashboard Script
- I will create `scripts/dashboard.py`.
- This script will use Streamlit to load your `processed_dataset.csv` and display the data and charts interactively.

## Verification Plan
1. Once built, I will give you the exact command (`streamlit run scripts/dashboard.py`) to start the website locally on your computer.
2. You can open it in your browser and verify that it looks professional for your Viva.
