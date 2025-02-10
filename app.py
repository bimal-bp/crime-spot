import streamlit as st
import pickle
import os

# Define model file path
model_path = "Model/model.pkl"

# Load the pre-trained model
try:
    if os.path.exists(model_path):
        with open(model_path, "rb") as file:
            best_rf_model = pickle.load(file)
        st.success("Model loaded successfully!")
    else:
        best_rf_model = None
        st.error(f"Model file not found: {model_path}. Please ensure it exists in the directory.")
except FileNotFoundError:
    best_rf_model = None
    st.error(f"Model file not found: {model_path}. Please check the file location.")
except pickle.UnpicklingError:
    best_rf_model = None
    st.error("Error loading model: The file may be corrupted or not a valid pickle file.")
except Exception as e:
    best_rf_model = None
    st.error(f"Unexpected error loading model: {e}")
