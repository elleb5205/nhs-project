import streamlit as st

# --- [DO NOT EDIT: UI & THEME] ---
st.set_page_config(page_title="NHS | Institutional Portal", page_icon="📈", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    
    /* Registration & Login Styling */
    .auth-card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }
    
    /* Investment Cards */
    .vip-card {
        background: white; border-radius: 20px; padding: 20px;
        margin-bottom: 20px; border: 1px solid #e2e8f0;
        text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .vip-img { width: 100%; border-radius: 15px; margin-bottom: 15px; height: 180px; object-fit: cover; }
    .vip-price { font-size: 1.8rem; font-weight: 800; color: #0072ff; }
    
    /* Payment Details Card */
    .pay-card {
        background: #f1f5f9; border-left: 5px solid #0072ff;
        padding: 20px; border-radius: 10px; margin-top: 20px;
    }
    
    /* Global Button */
    div.stButton > button {
        background: linear-gradient(90deg, #00aeef 0%, #0072ff 100%) !important;
        color: white !important; border-radius: 12px !important;
        width: 100% !important; border: none !important;
        height: 50px !important; font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION LOGIC ---
if "page" not in st.session_state:
    st.session_state.page = "register"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# --- [STAGE 1: PROFESSIONAL REGISTRATION] ---
if st.session_state.page == "register":
    st.markdown("<h1 style='text-align:center; color:#1e293b;'>Create account</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>Join thousands of others building their future.</p>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1: f_name = st.text_input("First name")
        with col2: l_name = st.text_input("Last name")
        
        u_name = st.text_input("Username")
        email = st.text_input("Email address")
        phone = st.text_input("Phone number")
        pwd = st.text_input("Password", type="password")
        
        if st.button("Complete registration"):
            if u_name and pwd:
                st.session_state.user_name = u_name
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Please fill in all required fields.")

# --- [STAGE 2: DASHBOARD & INVESTMENTS] ---
elif st.session_state.page == "dashboard":
    st.markdown(f"### Welcome back, **{st.session_state.user_name}** 👋")
    
    tab1, tab2 = st.tabs(["💎 Investment Portfolios", "💳 My Wallet"])
    
    with tab1:
        # VIP 1 - Expensive Car
        with st.container():
            st.markdown("""
                <div class="vip-card">
                    <img src="https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=500" class="vip-img">
                    <div style="color:#64748b; font-weight:bold;">VIP 1 - AUTOMOTIVE ASSET</div>
                    <div class="vip-price">₦ 5,000</div>
                    <p>Daily Income: <b>₦ 1,150</b> | Term: <b>30 Days</b></p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Invest in VIP 1", key="v1"):
                st.session_state.page = "payment"
                st.rerun()

        # VIP 2 - Luxurious Wristwatch
        with st.container():
            st.markdown("""
                <div class="vip-card">
                    <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500" class="vip-img">
                    <div style="color:#64748b; font-weight:bold;">VIP 2 - LUXURY CHRONOGRAPH</div>
                    <div class="vip-price">₦ 15,000</div>
                    <p>Daily Income: <b>₦ 3,500</b> | Term: <b>20 Days</b></p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Invest in VIP 2", key="v2"):
                st.session_state.page = "payment"
                st.rerun()

        # VIP 3 - Gold Reserve
        with st.container():
            st.markdown("""
                <div class="vip-card">
                    <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=500" class="vip-img">
                    <div style="color:#64748b; font-weight:bold;">VIP 3 - PRECIOUS METALS</div>
                    <div class="vip-price">₦ 35,000</div>
                    <p>Daily Income: <b>₦ 8,200</b> | Term: <b>20 Days</b></p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Invest in VIP 3", key="v3"):
                st.session_state.page = "payment"
                st.rerun()

# --- [STAGE 3: PROFESSIONAL PAYMENT PAGE] ---
elif st.session_state.page == "payment":
    st.markdown("### 💳 Deposit & Fund Account")
    st.write("Complete your transfer below to activate your investment.")
    
    st.markdown(f"""
        <div class="pay-card">
            <p style="margin:0; font-size:0.8rem; color:#64748b;">BANK TRANSFER</p>
            <h4 style="margin:5px 0;">Bank: <b>PalmPay</b></h4>
            <h4 style="margin:5px 0;">A/C Name: <b>{st.session_state.user_name} (NHS)</b></h4>
            <h2 style="margin:10px 0; color:#0072ff; letter-spacing:2px;">6606239732</h2>
        </div>
        
        <div class="pay-card" style="border-left-color: #f7931a; margin-top:20px;">
            <p style="margin:0; font-size:0.8rem; color:#64748b;">CRYPTO DEPOSIT (USDT/BEP20)</p>
            <p style="margin:5px 0; font-size:0.9rem; word-break: break-all;">
                Address: <b>0x7b3336E08e8E37E468f78087263b610F584C1C4f</b>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I have made payment"):
        st.success("Transaction submitted for verification!")
        if st.button("Return to Home"):
            st.session_state.page = "dashboard"
            st.rerun()
    
