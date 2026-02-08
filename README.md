# 📱 Mobile Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

A machine learning web application that predicts mobile phone prices based on specifications like RAM, battery, and camera quality. Built with **Streamlit** for an interactive user interface.

## ✨ Features
*   **Real-time Prediction:** Estimate prices instantly using a trained Linear Regression model.
*   **Data Insights:** Comprehensive EDA including outlier detection and feature scaling.
*   **User-Friendly Dashboard:** Simple sliders to adjust phone parameters.
*   **Robust Pipeline:** Automated preprocessing and model training scripts.

## 🚀 Quick Start

1.  **Install Dependencies:**
    ```bash
    pip install pandas numpy scikit-learn streamlit joblib matplotlib seaborn
    ```

2.  **Train Model:**
    Run the training script to generate `model.pkl`:
    ```bash
    python train_model.py
    ```

3.  **Run App:**
    Launch the Streamlit dashboard:
    ```bash
    streamlit run app.py
    ```

## � Project Structure

*   `app.py`: Main application code.
*   `train_model.py`: Script to train and save the model.
*   `run_pipeline.py`: Full ML pipeline with evaluation metrics.
*   `Cellphone.csv`: The dataset used for training.
*   `notebooks/`: Includes EDA and model training notebooks.

---
*Predict efficiently with Python & Streamlit.*
