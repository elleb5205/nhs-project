import streamlit as st

# --- [DO NOT EDIT: UI & THEME] ---
st.set_page_config(page_title="NHS | Institutional Portal", page_icon="📈", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1e293b; font-family: 'Inter', sans-serif; }
    
    /* Registration Input Styling */
    label { font-weight: 600 !important; color: #475569 !important; }
    .stTextInput > div > div > input { background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px; }

    /* Bottom Navigation Bar */
    .nav-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: white; border-top: 1px solid #e2e8f0; 
               display: flex; justify-content: space-around; padding: 10px 0; z-index: 1000; }
    
    /* VIP Cards */
    .vip-card { background: white; border-radius: 20px; padding: 20px; margin-bottom: 25px; 
               border: 1px solid #f1f5f9; text-align: center; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    .vip-img { width: 100%; border-radius: 15px; height: 200px; object-fit: cover; margin-bottom: 15px; }
    
    /* Payment Details */
    .pay-box { background: #f0f9ff; border: 1.5px dashed #00aeef; border-radius: 15px; padding: 20px; margin-top: 20px; }

    /* Buttons */
    div.stButton > button { background: #00aeef !important; color: white !important; border-radius: 30px !important; 
                           width: 100% !important; height: 50px !important; font-weight: bold !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# --- APP NAVIGATION LOGIC ---
if "page" not in st.session_state: st.session_state.page = "register"
if "username" not in st.session_state: st.session_state.username = ""

# --- [STAGE 1: REGISTRATION] ---
if st.session_state.page == "register":
    st.markdown("<h2 style='text-align:center;'>Create account</h2>", unsafe_allow_html=True)
    f_name = st.text_input("First Name", placeholder="Put your first name here")
    l_name = st.text_input("Last Name", placeholder="Put your last name here")
    email = st.text_input("Email Address", placeholder="Put your email address here")
    u_name = st.text_input("Username", placeholder="Put your username here")
    pwd = st.text_input("Password", type="password", placeholder="Put your password here")
    
    if st.button("COMPLETE REGISTRATION"):
        if f_name and l_name and u_name:
            st.session_state.username = u_name
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Please fill all fields to secure your account.")

# --- [STAGE 2: HOME SCREEN] ---
elif st.session_state.page == "home":
    st.markdown(f"### Welcome to NHS, {st.session_state.username}")
    st.image("https://images.unsplash.com/photo-1560520653-9e0e4c89eb11?auto=format&fit=crop&w=800", caption="NHS Global Capital Management")
    st.info("Institutional Grade High-Yield Portfolios. Verified by NHPC.")
    
    # Simple Bottom Nav Simulation
    col1, col2, col3 = st.columns(3)
    if col1.button("🏠 Home"): st.session_state.page = "home"; st.rerun()
    if col2.button("💎 Invest"): st.session_state.page = "invest"; st.rerun()
    if col3.button("👤 My"): st.session_state.page = "my"; st.rerun()

# --- [STAGE 3: INVESTMENT PAGE] ---
elif st.session_state.page == "invest":
    st.markdown("## Investment Portfolios")
    
    # VIP List with Images and Cycles
    vips = [
        {"name": "VIP 1 - Luxury Car", "price": 5000, "daily": 1150, "cycle": 30, "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500"},
        {"name": "VIP 2 - Luxury Watch", "price": 15000, "daily": 3500, "cycle": 20, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"},
        {"name": "VIP 3 - Real Estate", "price": 35000, "daily": 8200, "cycle": 20, "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500"},
        {"name": "VIP 4 - High-end Phone", "price": 70000, "daily": 16500, "cycle": 20, "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},
        {"name": "VIP 5 - Gold Reserve", "price": 130000, "daily": 32000, "cycle": 20, "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=500"},
    ]

    for v in vips:
        st.markdown(f"""
            <div class="vip-card">
                <img src="{v['img']}" class="vip-img">
                <h3 style="margin:0; color:#00aeef;">{v['name']}</h3>
                <h2 style="margin:10px 0;">₦ {v['price']:,}</h2>
                <p>Profit: <b>₦ {v['daily']:,} / Day</b> | Cycle: <b>{v['cycle']} Days</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Activate {v['name']}", key=v['name']):
            st.session_state.page = "payment"
            st.rerun()

# --- [STAGE 4: PAYMENT PAGE] ---
elif st.session_state.page == "payment":
    st.markdown("### Deposit Funds")
    st.write("Transfer the investment amount to the details below to activate your node.")
    
    st.markdown(f"""
        <div class="pay-box">
            <p style="color:#64748b; margin:0;">BANK NAME</p>
            <h4 style="margin:0;">Moniepoint</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">ACCOUNT NAME</p>
            <h4 style="margin:0;">{st.session_state.username} (NHS)</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">ACCOUNT NUMBER</p>
            <h2 style="margin:0; color:#00aeef; letter-spacing:2px;">8126419410</h2>
        </div>
        <div class="pay-box" style="border-color: #f7931a;">
            <p style="color:#64748b; margin:0;">COIN WALLET (BEP20)</p>
            <p style="font-size:0.8rem; word-break:break-all;"><b>0x7b3336E08e8E37E468f78087263b610F584C1C4f</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE TRANSFERRED"):
        st.success("Verification in progress. Your VIP node will activate shortly.")
        if st.button("Back to Home"): st.session_state.page = "home"; st.rerun()
