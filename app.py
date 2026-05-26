import streamlit as st
import random

# --- [1. APP CONFIG] ---
st.set_page_config(page_title="NHS | Financial Growth", layout="centered")

# --- [2. ADVANCED CSS: MATCHING SCREENSHOT STYLE] ---
st.markdown("""
    <style>
    /* Professional Theme */
    .stApp { background-color: #f4f7fa; color: #1e293b; }
    
    /* Input Visibility Fix */
    input { color: #000000 !important; background-color: #ffffff !important; border: 1px solid #d1d5db !important; }

    /* Header & Branding */
    .brand-header { background: linear-gradient(135deg, #004e92 0%, #000428 100%); padding: 30px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin-bottom: 20px; }
    
    /* Realistic VIP Cards */
    .vip-card { background: white; border-radius: 20px; padding: 15px; margin-bottom: 20px; border: 1px solid #e5e7eb; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; }
    .vip-badge { background: #ffd700; color: #000; padding: 5px 15px; border-radius: 50px; font-weight: bold; font-size: 0.8rem; }
    .vip-price { font-size: 1.8rem; font-weight: 800; color: #004e92; margin: 10px 0; }
    
    /* Live Payout Ticker (Auto-scrolling effect) */
    .ticker-wrap { background: #ffffff; border-top: 2px solid #004e92; padding: 10px; position: fixed; bottom: 60px; left: 0; width: 100%; z-index: 100; box-shadow: 0 -5px 10px rgba(0,0,0,0.05); }
    .ticker-item { font-size: 0.85rem; font-weight: bold; color: #16a34a; white-space: nowrap; overflow: hidden; }

    /* Bottom Navigation */
    .bottom-nav { position: fixed; bottom: 0; left: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid #e5e7eb; z-index: 1000; }
    
    /* Buttons */
    div.stButton > button { background: #004e92 !important; color: white !important; border-radius: 15px !important; border: none !important; font-weight: bold !important; height: 45px !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

# --- [3. SESSION LOGIC] ---
if "page" not in st.session_state: st.session_state.page = "reg"
if "user" not in st.session_state: st.session_state.user = "Member"

# --- [4. PAGE: REGISTRATION] ---
if st.session_state.page == "reg":
    st.markdown("<div class='brand-header'><h1>NHS</h1><p>Nigerian Help Support</p></div>", unsafe_allow_html=True)
    st.markdown("### Create Your Account")
    
    f_name = st.text_input("First Name", placeholder="Enter your first name")
    l_name = st.text_input("Last Name", placeholder="Enter your last name")
    u_name = st.text_input("Username", placeholder="Choose username")
    email = st.text_input("Email", placeholder="Enter email address")
    pwd = st.text_input("Password", type="password", placeholder="Enter secure password")
    
    if st.button("COMPLETE REGISTRATION"):
        if u_name and pwd:
            st.session_state.user = u_name
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Missing required details.")

# --- [5. PAGE: HOME SCREEN] ---
elif st.session_state.page == "home":
    st.markdown(f"<div class='brand-header'><h3>Welcome, {st.session_state.user}</h3><p>Current Balance: ₦0.00</p></div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1579621970795-87f9c7216289?w=800", caption="NHS Global Investment Hub")
    
    st.markdown("""
        <div style="background:white; padding:20px; border-radius:15px; border:1px solid #e5e7eb;">
            <h4 style="color:#004e92;">Company Description</h4>
            <p style="font-size:0.9rem;">NHS (Nigerian Help Support) is an institutional-grade asset management system. We facilitate growth by connecting retail capital to luxury asset nodes. Secure, verified, and daily returns.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("💎 Go to VIP Portfolio"): st.session_state.page = "invest"; st.rerun()

    # Live Payout Ticker Simulation
    users = ["Okon***", "Musa***", "Blessing***", "Chidi***", "Ade***"]
    st.markdown(f"<div class='ticker-wrap'><div class='ticker-item'>🚀 LIVE PAYOUT: {random.choice(users)} just withdrew ₦{random.randint(10,80)},000 via Moniepoint</div></div>", unsafe_allow_html=True)

# --- [6. PAGE: INVEST] ---
elif st.session_state.page == "invest":
    st.markdown("### Luxury Investment Nodes")
    
    vips = [
        {"name": "VIP 1 - Porsche Node", "price": "5,000", "daily": "1,150", "cycle": "30", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400"},
        {"name": "VIP 2 - Rolex Node", "price": "15,000", "daily": "3,500", "cycle": "20", "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
        {"name": "VIP 3 - Real Estate", "price": "35,000", "daily": "8,200", "cycle": "20", "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400"},
        {"name": "VIP 4 - Gold Reserve", "price": "70,000", "daily": "16,500", "cycle": "20", "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
    ]

    for v in vips:
        st.markdown(f"""
            <div class="vip-card">
                <span class="vip-badge">ACTIVE PLAN</span>
                <img src="{v['img']}" style="width:100%; border-radius:15px; height:180px; object-fit:cover; margin-top:10px;">
                <h4 style="margin:10px 0;">{v['name']}</h4>
                <div class="vip-price">₦ {v['price']}</div>
                <p>Profit: <b>₦ {v['daily']} / Day</b><br>Term: {v['cycle']} Days</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Invest in {v['name']}", key=v['name']):
            st.session_state.page = "pay"
            st.rerun()

# --- [7. PAGE: PAYMENT] ---
elif st.session_state.page == "pay":
    st.markdown("### Secure Deposit")
    st.markdown(f"""
        <div style="background:#f0f9ff; border:2px solid #004e92; padding:25px; border-radius:20px;">
            <p style="color:#64748b; margin:0;">BANKING PARTNER</p>
            <h4 style="margin:0;">Moniepoint</h4>
            <p style="margin:15px 0 0 0; color:#64748b;">A/C NAME</p>
            <h4 style="margin:0;">{st.session_state.user} (NHS-Node)</h4>
            <p style="margin:15px 0 0 0; color:#64748b;">ACCOUNT NUMBER</p>
            <h2 style="margin:0; color:#004e92; letter-spacing:2px;">8126419410</h2>
        </div>
        <br>
        <div style="background:#fff7ed; padding:15px; border-radius:15px; border:1px solid #f7931a;">
            <p style="margin:0; font-size:0.8rem; color:#9a3412;"><b>USDT BEP20 ADDRESS:</b><br>
            0x7b3336E08e8E37E468f78087263b610F584C1C4f</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE TRANSFERRED"):
        st.success("Verification in progress. System will update in 10 mins.")
        if st.button("Return to Dashboard"):
            st.session_state.page = "home"
            st.rerun()
    
