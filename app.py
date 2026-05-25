import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NHS | Institutional Portal", page_icon="📈", layout="centered")

# --- PREMIUM FINTECH CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; color: #1e293b; }
    
    /* Top Balance Card */
    .balance-card {
        background: linear-gradient(90deg, #00aeef 0%, #0072ff 100%);
        color: white; padding: 25px; border-radius: 20px;
        margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,114,255,0.2);
    }

    /* VIP Investment Cards */
    .vip-card {
        background: white; border-radius: 15px; padding: 20px;
        border: 1px solid #e2e8f0; margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .vip-header { color: #0072ff; font-weight: bold; font-size: 1.2rem; }
    .price-tag { font-size: 1.5rem; font-weight: 800; color: #1e293b; margin: 10px 0; }
    
    /* Bank Info Card */
    .bank-card {
        background: white; border-radius: 20px; padding: 25px;
        border: 1px solid #e2e8f0; margin-top: 20px;
    }
    
    /* Global Button Styling */
    div.stButton > button {
        background: #00aeef !important; color: white !important;
        border-radius: 12px !important; width: 100% !important;
        border: none !important; font-weight: bold !important;
        height: 45px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION LOGIC ---
if "registered" not in st.session_state:
    st.session_state.registered = False

# --- 1. REGISTRATION SCREEN ---
if not st.session_state.registered:
    st.markdown("<h2 style='text-align:center;'>Create account</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>Join thousands building their future on NHS.</p>", unsafe_allow_html=True)
    u_name = st.text_input("Username", placeholder="Choose username")
    phone = st.text_input("Phone number")
    pwd = st.text_input("Password", type="password")
    
    if st.button("Complete registration"):
        st.session_state.username = u_name if u_name else "Master"
        st.session_state.registered = True
        st.rerun()

# --- 2. DASHBOARD ---
else:
    tab_home, tab_invest, tab_fund = st.tabs(["🏠 Home", "💎 VIP Tiers", "💳 Fund Wallet"])

    with tab_home:
        st.markdown(f"""
            <div class="balance-card">
                <p style="margin:0; font-size:0.9rem; opacity:0.8;">Total Balance</p>
                <h1 style="margin:0; color:white;">₦ 0.00</h1>
            </div>
        """, unsafe_allow_html=True)
        st.info("📢 Notice: NHPC Tier-1 Node is now active. Start your investment to earn daily.")

    with tab_invest:
        st.markdown("### Investment Plans")
        # Fixed the number formatting here to avoid the SyntaxError
        vips = [
            {"name": "VIP 1", "price": 5000, "daily": 1150, "cycle": 30},
            {"name": "VIP 2", "price": 15000, "daily": 3500, "cycle": 20},
            {"name": "VIP 3", "price": 35000, "daily": 8200, "cycle": 20},
            {"name": "VIP 4", "price": 70000, "daily": 16500, "cycle": 20},
            {"name": "VIP 5", "price": 130000, "daily": 32000, "cycle": 20},
        ]

        for v in vips:
            total_rev = v['daily'] * v['cycle']
            st.markdown(f"""
                <div class="vip-card">
                    <div class="vip-header">{v['name']} - Infrastructure Node</div>
                    <div class="price-tag">₦ {v['price']:,}</div>
                    <p style="color:#64748b; font-size:0.9rem; margin:0;">
                        Daily Income: <b>₦ {v['daily']:,}</b><br>
                        Total Revenue: <b>₦ {total_rev:,}</b><br>
                        Cycle: <b>{v['cycle']} Days</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Invest in {v['name']}", key=v['name']):
                st.toast("Redirecting to Deposit...")

    with tab_fund:
        st.markdown("### Fund wallet")
        st.markdown(f"""
            <div class="bank-card">
                <p style="color:#64748b; margin-bottom:5px;">Bank name</p>
                <h4 style="color:#00aeef; margin:0;">PalmPay</h4>
                <p style="color:#64748b; margin-top:15px; margin-bottom:5px;">Account name</p>
                <h4 style="margin:0;">{st.session_state.username} (NHS)</h4>
                <p style="color:#64748b; margin-top:15px; margin-bottom:5px;">Account number</p>
                <h2 style="margin:0; letter-spacing:2px;">6606239732</h2>
            </div>
        """, unsafe_allow_html=True)
        
