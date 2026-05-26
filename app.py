import streamlit as st
import random
from datetime import datetime

# --- [1. APP CONFIG] ---
st.set_page_config(
    page_title="NHS | Financial Growth",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- [2. ADVANCED CSS: PROFESSIONAL BLUE THEME] ---
st.markdown("""
<style>
/* Hide Streamlit default stuff */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Professional Theme */
.stApp {
    background-color: #f4f7fa;
    color: #1e293b;
    padding-bottom: 120px; /* Space for nav + ticker */
}

/* Input Visibility Fix */
input {
    color: #000000!important;
    background-color: #ffffff!important;
    border: 1px solid #d1d5db!important;
    border-radius: 12px!important;
}

/* Header & Branding */
.brand-header {
    background: linear-gradient(135deg, #004e92 0%, #000428 100%);
    padding: 30px 20px;
    border-radius: 0 0 30px 30px;
    color: white;
    text-align: center;
    margin: -1rem -1rem 20px -1rem;
}

.balance-amount {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 10px 0;
}

/* Realistic VIP Cards */
.vip-card {
    background: white;
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.vip-badge {
    background: #ffd700;
    color: #000;
    padding: 5px 15px;
    border-radius: 50px;
    font-weight: bold;
    font-size: 0.8rem;
    display: inline-block;
}

.vip-price {
    font-size: 1.8rem;
    font-weight: 800;
    color: #004e92;
    margin: 10px 0;
}

/* Live Payout Ticker */
.ticker-wrap {
    background: #ffffff;
    border-top: 2px solid #004e92;
    padding: 10px 15px;
    position: fixed;
    bottom: 70px;
    left: 0;
    width: 100%;
    z-index: 100;
    box-shadow: 0 -5px 10px rgba(0,0,0,0.05);
}

.ticker-item {
    font-size: 0.85rem;
    font-weight: bold;
    color: #16a34a;
    animation: scroll 20s linear infinite;
}

@keyframes scroll {
    0% { transform: translateX(100%); }
    100% { transform: translateX(-100%); }
}

/* Bottom Navigation */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    display: flex;
    justify-content: space-around;
    padding: 12px 0;
    border-top: 1px solid #e5e7eb;
    z-index: 1000;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
}

.nav-btn {
    background: none!important;
    border: none!important;
    color: #64748b!important;
    font-size: 0.75rem!important;
    padding: 5px!important;
    height: auto!important;
}
.nav-btn.active {
    color: #004e92!important;
    font-weight: bold!important;
}

/* Buttons */
div.stButton > button {
    background: #004e92!important;
    color: white!important;
    border-radius: 15px!important;
    border: none!important;
    font-weight: bold!important;
    height: 45px!important;
    width: 100%!important;
    transition: all 0.3s;
}
div.stButton > button:hover {
    background: #003d73!important;
    transform: translateY(-2px);
}

/* Deposit card */
.deposit-card {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border: 2px solid #004e92;
    padding: 25px;
    border-radius: 20px;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION LOGIC] ---
if "page" not in st.session_state:
    st.session_state.page = "reg"
if "user" not in st.session_state:
    st.session_state.user = "Member"
if "balance" not in st.session_state:
    st.session_state.balance = 0.00
if "active_plan" not in st.session_state:
    st.session_state.active_plan = None

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
        if u_name and pwd and f_name:
            st.session_state.user = u_name
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Please fill all required details.")

# --- [5. PAGE: HOME SCREEN] ---
elif st.session_state.page == "home":
    st.markdown(f"""
    <div class='brand-header'>
        <h3>Welcome, {st.session_state.user}</h3>
        <p>Current Balance</p>
        <div class='balance-amount'>₦{st.session_state.balance:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1579621970795-87f9c7216289?w=800", use_container_width=True)

    st.markdown("""
    <div style="background:white; padding:20px; border-radius:15px; border:1px solid #e5e7eb; margin: 20px 0;">
        <h4 style="color:#004e92; margin-top:0;">Company Description</h4>
        <p style="font-size:0.9rem; line-height:1.6;">NHS (Nigerian Help Support) is an institutional-grade asset management system. We facilitate growth by connecting retail capital to luxury asset nodes. Secure, verified, and daily returns.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💎 VIP Portfolio"):
            st.session_state.page = "invest"
            st.rerun()
    with col2:
        if st.button("💰 Deposit Funds"):
            st.session_state.page = "pay"
            st.rerun()

# --- [6. PAGE: INVEST] ---
elif st.session_state.page == "invest":
    st.markdown("### Luxury Investment Nodes")
    st.markdown("Choose a plan to start earning daily")

    vips = [
        {"name": "VIP 1 - Porsche Node", "price": 5000, "daily": 1150, "cycle": "30", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400"},
        {"name": "VIP 2 - Rolex Node", "price": 15000, "daily": 3500, "cycle": "20", "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
        {"name": "VIP 3 - Real Estate", "price": 35000, "daily": 8200, "cycle": "20", "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400"},
        {"name": "VIP 4 - Gold Reserve", "price": 70000, "daily": 16500, "cycle": "20", "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400"},
    ]

    for v in vips:
        st.markdown(f"""
        <div class="vip-card">
            <span class="vip-badge">ACTIVE PLAN</span>
            <img src="{v['img']}" style="width:100%; border-radius:15px; height:180px; object-fit:cover; margin:10px 0;">
            <h4 style="margin:10px 0;">{v['name']}</h4>
            <div class="vip-price">₦ {v['price']:,}</div>
            <p>Profit: <b>₦ {v['daily']:,} / Day</b><br>Term: {v['cycle']} Days</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Invest in {v['name']}", key=v['name']):
            st.session_state.active_plan = v['name']
            st.session_state.page = "pay"
            st.rerun()

# --- [7. PAGE: PAYMENT] ---
elif st.session_state.page == "pay":
    st.markdown("### Secure Deposit")

    st.markdown(f"""
    <div class="deposit-card">
        <p style="color:#64748b; margin:0; font-size:0.9rem;">BANKING PARTNER</p>
        <h2 style="margin:5px 0 15px 0; color:#000428;">MONIEPOINT</h2>

        <p style="margin:15px 0 0 0; color:#64748b; font-size:0.9rem;">ACCOUNT NUMBER</p>
        <h1 style="margin:0; color:#004e92; letter-spacing:2px; font-size:2rem;">8126419410</h1>

        <p style="margin:15px 0 0 0; color:#64748b; font-size:0.9rem;">A/C NAME</p>
        <h4 style="margin:0;">NHS INVESTMENT LTD</h4>
    </div>
    """, unsafe_allow_html=True)

    st.info("📋 Copy the account number above and transfer from your bank app. Your deposit reflects in 5-10 mins after confirmation.")

    if st.session_state.active_plan:
        st.warning(f"Selected Plan: {st.session_state.active_plan}")

    if st.button("I HAVE TRANSFERRED"):
        st.success("Verification in progress. Our system will credit your wallet in 10 mins.")
        st.balloons()

    if st.button("Return to Dashboard"):
        st.session_state.page = "home"
        st.rerun()

# --- [8. PAGE: PROFILE] ---
elif st.session_state.page == "profile":
    st.markdown("### My Profile")

    st.markdown(f"""
    <div style="background:white; padding:20px; border-radius:15px; text-align:center; margin-bottom:20px;">
        <div style="width:80px; height:80px; background:#004e92; border-radius:50%; margin:0 auto 15px auto; display:flex; align-items:center; justify-content:center; color:white; font-size:2rem; font-weight:bold;">
            {st.session_state.user[0].upper()}
        </div>
        <h3 style="margin:0;">{st.session_state.user}</h3>
        <p style="color:#64748b;">Member since {datetime.now().strftime('%B %Y')}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Logout"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# --- [9. LIVE TICKER + BOTTOM NAV] ---
if st.session_state.page!= "reg":
    users = ["Okon***", "Musa***", "Blessing***", "Chidi***", "Ade***", "Fatima***"]
    amounts = [15000, 25000, 80000, 35000, 120000, 45000]
    st.markdown(f"""
    <div class='ticker-wrap'>
        <div class='ticker-item'>🚀 LIVE: {random.choice(users)} just withdrew ₦{random.choice(amounts):,} via Moniepoint • {datetime.now().strftime('%H:%M')}</div>
    </div>
    """, unsafe_allow_html=True)

    # Bottom Navigation
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🏠\nHome", key="nav_home"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("💎\nVIP", key="nav_vip"):
            st.session_state.page = "invest"
            st.rerun()
    with col3:
        if st.button("💰\nDeposit", key="nav_pay"):
            st.session_state.page = "pay"
            st.rerun()
    with col4:
        if st.button("👤\nMe", key="nav_me"):
            st.session_state.page = "profile"
            st.rerun()
