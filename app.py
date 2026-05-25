import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- PAGE CONFIGURATION & PREMIUM THEME ---
st.set_page_config(
    page_title="NHS | Create Account",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match your "Light & Professional" screenshot
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%);
        color: #1e293b;
    }
    
    /* Center the login box */
    .main-box {
        background-color: white;
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
        border: 1px solid #f1f5f9;
        margin-top: 20px;
    }
    
    h1, h2, h3 {
        color: #0f172a;
        font-family: 'Inter', sans-serif;
        text-align: center;
    }

    /* Styling the Input Labels */
    label {
        font-weight: 500 !important;
        color: #475569 !important;
        margin-bottom: 8px !important;
    }

    /* Styling Input Fields */
    .stTextInput > div > div > input {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 12px;
        color: #1e293b;
    }

    /* The "Complete Registration" Blue Button */
    div.stButton > button:first-child {
        background: #00aeef;
        background-color: #00aeef;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 15px 0px;
        font-size: 18px;
        font-weight: 600;
        width: 100%;
        margin-top: 20px;
        box-shadow: 0 4px 14px 0 rgba(0,174,239,0.39);
    }
    
    div.stButton > button:first-child:hover {
        background-color: #0096ce;
        border: none;
        color: white;
    }

    /* Footer Text */
    .footer-link {
        text-align: center;
        margin-top: 25px;
        color: #64748b;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "registered" not in st.session_state:
    st.session_state.registered = False

# --- REGISTRATION PAGE (The Screenshot Look) ---
if not st.session_state.registered:
    st.markdown("<h3>Create account</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>Join thousands of others building their future on our platform.</p>", unsafe_allow_html=True)
    
    # Create the form layout exactly like the image
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First name", placeholder="First name")
        with col2:
            last_name = st.text_input("Last name", placeholder="Last name")
            
        username = st.text_input("Username", placeholder="Choose username")
        email = st.text_input("Email address", placeholder="you@example.com")
        phone = st.text_input("Phone number", placeholder="08012345678")
        referral = st.text_input("Referral (optional)", value="okonaneozeng")
        password = st.text_input("Password", placeholder="Choose password", type="password")
        
        if st.button("Complete registration"):
            if first_name and last_name and username and email and password:
                st.session_state.username = username
                st.session_state.registered = True
                st.rerun()
            else:
                st.error("Please fill in all required fields.")
                
    st.markdown("<div class='footer-link'>Already have an account? <span style='color:#00aeef; font-weight:600;'>Sign in</span></div>", unsafe_allow_html=True)

# --- MAIN APP (After Registration) ---
else:
    # Here is where the Invest, Home, and My tabs go
    st.title(f"Welcome to NHS, {st.session_state.username}")
    st.info("Your account is now active and approved by NHPC.")
    # (The rest of your Invest/My code would go here)
    
