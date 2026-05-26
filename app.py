import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NHS",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"]{
    font-family: 'Segoe UI', sans-serif;
}

.stApp{
    background:#ff6a00;
    background-image: radial-gradient(circle at top right,#ff944d,#ff6a00);
    color:white;
}

/* HEADER */
.main-header{
    padding:20px;
    border-radius:0 0 25px 25px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    text-align:center;
    margin-bottom:15px;
}

.logo-box{
    width:90px;
    height:90px;
    background:black;
    border-radius:25px;
    margin:auto;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:40px;
    color:white;
    font-weight:bold;
}

.brand-name{
    font-size:38px;
    font-weight:800;
    margin-top:10px;
}

.brand-sub{
    font-size:14px;
    opacity:0.9;
}

/* WHITE CARD */
.white-card{
    background:white;
    border-radius:25px;
    padding:20px;
    color:#111827;
    margin-bottom:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}

/* INPUTS */
input{
    border-radius:15px !important;
    border:1px solid #e5e7eb !important;
    padding:14px !important;
    background:#f9fafb !important;
    color:black !important;
}

/* BUTTONS */
div.stButton > button{
    width:100%;
    height:50px;
    border:none;
    border-radius:15px;
    background:#ff6a00;
    color:white;
    font-weight:bold;
    font-size:16px;
}

/* VIP CARD */
.vip-card{
    background:white;
    border-radius:25px;
    padding:15px;
    margin-bottom:20px;
    box-shadow:0 6px 20px rgba(0,0,0,0.08);
}

.vip-img{
    width:100%;
    border-radius:20px;
    height:180px;
    object-fit:cover;
}

.vip-profit{
    color:#22c55e;
    font-size:30px;
    font-weight:800;
}

.vip-price{
    font-size:24px;
    font-weight:700;
}

/* MEMBER BOX */
.member-box{
    background:#f8fafc;
    border-radius:15px;
    padding:12px;
    margin-bottom:10px;
    color:#111827;
    font-weight:700;
}

/* BOTTOM NAV */
.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    width:100%;
    background:#ff7b2c;
    display:flex;
    justify-content:space-around;
    padding:12px;
    z-index:999999;
    border-top:1px solid rgba(255,255,255,0.2);
}

.nav-item{
    text-align:center;
    color:white;
    font-size:13px;
    font-weight:600;
}

/* LIVE TICKER */
.ticker{
    background:white;
    color:#16a34a;
    padding:10px;
    border-radius:15px;
    font-weight:bold;
    margin-bottom:15px;
    animation: blink 1s infinite alternate;
}

@keyframes blink{
    from{opacity:0.8;}
    to{opacity:1;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "register"

if "user" not in st.session_state:
    st.session_state.user = "Member"

# ---------------- REGISTER PAGE ----------------
if st.session_state.page == "register":

    st.markdown("""
    <div class="main-header">
        <div class="logo-box">N</div>
        <div class="brand-name">NHS</div>
        <div class="brand-sub">Nigeria Helping Support</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="white-card">', unsafe_allow_html=True)

    st.subheader("Create Account")

    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    invite = st.text_input("Invitation Code", value="NHS2026")

    if st.button("Sign Up"):
        st.session_state.user = fname
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
elif st.session_state.page == "home":

    st.markdown(f"""
    <div class="main-header">
        <div style="display:flex;align-items:center;gap:10px;">
            <div class="logo-box" style="width:60px;height:60px;font-size:25px;">N</div>
            <div>
                <div style="font-size:28px;font-weight:800;">NHS</div>
                <div style="font-size:13px;">Welcome {st.session_state.user}</div>
            </div>
        </div>

        <div style="margin-top:20px;">
            <div style="font-size:14px;">Total Balance</div>
            <div style="font-size:45px;font-weight:800;">₦0</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    names = ["David", "Musa", "Precious", "Daniel", "Chinedu", "Blessing"]

    st.markdown(f"""
    <div class="ticker">
    🔥 {random.choice(names)} just withdrew ₦{random.randint(15,150)},000 successfully
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="white-card">
        <h3>Company Description</h3>
        <p>
        NHS is a digital financial growth platform designed for modern users.
        Fast deposits, smooth dashboard experience, premium VIP access and
        secure investment management system.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("VIP Plans")

    vips = [
        {
            "name":"VIP 1",
            "price":"₦5,000",
            "daily":"₦1,200",
            "img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800"
        },
        {
            "name":"VIP 2",
            "price":"₦15,000",
            "daily":"₦3,500",
            "img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=800"
        },
        {
            "name":"VIP 3",
            "price":"₦35,000",
            "daily":"₦8,200",
            "img":"https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800"
        },
        {
            "name":"VIP 4",
            "price":"₦70,000",
            "daily":"₦16,500",
            "img":"https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?w=800"
        },
        {
            "name":"VIP 5",
            "price":"₦120,000",
            "daily":"₦30,000",
            "img":"https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=800"
        }
    ]

    for vip in vips:

        st.markdown(f"""
        <div class="vip-card">
            <img class="vip-img" src="{vip['img']}">
            <br><br>
            <div class="vip-profit">{vip['daily']}</div>
            <div>Daily Profit</div>

            <div class="vip-price">{vip['price']}</div>
            <div>{vip['name']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Activate {vip['name']}", key=vip['name']):
            st.session_state.page = "deposit"
            st.rerun()

    st.markdown("""
    <div class="white-card">
        <h3>Member List</h3>
    """, unsafe_allow_html=True)

    for i in range(6):
        st.markdown(f"""
        <div class="member-box">
            +₦{random.randint(20,900)},000<br>
            user****{random.randint(1000,9999)}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DEPOSIT PAGE ----------------
elif st.session_state.page == "deposit":

    st.markdown("""
    <div class="main-header">
        <div class="brand-name">Deposit</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="white-card">

        <h3>Bank Deposit</h3>

        <div style="
            background:#fff7ed;
            padding:20px;
            border-radius:20px;
            border:2px solid #ff6a00;
        ">

            <p style="margin:0;color:#6b7280;">BANK NAME</p>
            <h2 style="margin-top:5px;">MONIEPOINT</h2>

            <p style="margin:0;color:#6b7280;">ACCOUNT NUMBER</p>
            <h1 style="color:#ff6a00;">8126419410</h1>

        </div>

        <br>

        <div style="
            background:#f0fdf4;
            padding:15px;
            border-radius:15px;
            border:1px solid #22c55e;
        ">
            Upload proof after transfer for verification.
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("I HAVE MADE PAYMENT"):
        st.success("Payment verification processing successfully.")

    if st.button("Back Home"):
        st.session_state.page = "home"
        st.rerun()

# ---------------- BOTTOM NAV ----------------
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item">🏠<br>Home</div>
    <div class="nav-item">💎<br>VIP</div>
    <div class="nav-item">👥<br>Team</div>
    <div class="nav-item">👤<br>Me</div>
</div>
""", unsafe_allow_html=True)
