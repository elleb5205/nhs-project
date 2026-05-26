import streamlit as st
import random
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NHS",
    page_icon="🅝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS - FIXED VERSION ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.stDeployButton {display:none;}

.stApp{
    background:#ff6a00;
    background-image: radial-gradient(circle at top right,#ff944d,#ff6a00);
    color:white;
    padding-bottom: 100px;
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.main-header{
    padding:25px 20px;
    border-radius:0 0 30px 30px;
    background:rgba(0,0,0,0.15);
    backdrop-filter:blur(10px);
    text-align:center;
    margin:-1rem -1rem 15px -1rem;
    border:1px solid rgba(255,255,255,0.1);
}

.logo-box{
    width:75px;
    height:75px;
    background:#000000;
    border-radius:22px;
    margin:auto;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:38px;
    color:white;
    font-weight:900;
    box-shadow:0 4px 15px rgba(0,0,0,0.3);
}

.brand-name{
    font-size:36px;
    font-weight:900;
    margin-top:12px;
    letter-spacing:1px;
}

.brand-sub{
    font-size:14px;
    opacity:0.95;
    font-weight:500;
}

/* WHITE CARD */
.white-card{
    background:white;
    border-radius:25px;
    padding:22px;
    color:#111827;
    margin-bottom:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.1);
}

/* INPUTS */
.stTextInput > div > div > input{
    border-radius:15px!important;
    border:2px solid #e5e7eb!important;
    padding:15px!important;
    background:#f9fafb!important;
    color:black!important;
    font-weight:500!important;
}

.stTextInput > div > div > input:focus{
    border:2px solid #ff6a00!important;
    box-shadow:none!important;
}

/* BUTTONS */
div.stButton > button{
    width:100%;
    height:52px;
    border:none;
    border-radius:16px;
    background:#ff6a00;
    color:white;
    font-weight:700;
    font-size:16px;
    transition:all 0.2s;
}

div.stButton > button:hover{
    background:#e55a00;
    transform:translateY(-2px);
    box-shadow:0 5px 15px rgba(255,106,0,0.4);
}

/* VIP CARD */
.vip-card{
    background:white;
    border-radius:25px;
    padding:18px;
    margin-bottom:20px;
    box-shadow:0 6px 20px rgba(0,0,0,0.08);
    color:#111827;
}

.vip-img{
    width:100%;
    border-radius:20px;
    height:190px;
    object-fit:cover;
}

.vip-profit{
    color:#16a34a;
    font-size:32px;
    font-weight:900;
    margin-top:10px;
}

.vip-price{
    font-size:26px;
    font-weight:800;
    color:#111827;
    margin:5px 0;
}

/* MEMBER BOX */
.member-box{
    background:#f8fafc;
    border-radius:16px;
    padding:14px;
    margin-bottom:12px;
    color:#111827;
    font-weight:700;
    border:1px solid #e5e7eb;
}

/* TICKER */
.ticker{
    background:white;
    color:#16a34a;
    padding:12px;
    border-radius:16px;
    font-weight:700;
    margin-bottom:18px;
    box-shadow:0 4px 10px rgba(0,0,0,0.05);
}

/* DEPOSIT CARD */
.deposit-box{
    background:linear-gradient(135deg,#fff7ed,#ffedd5);
    padding:25px;
    border-radius:22px;
    border:3px solid #ff6a00;
    text-align:center;
}

/* TEAM LEVELS */
.team-level{
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
    color:white;
    position:relative;
    overflow:hidden;
}
.level1{background:linear-gradient(135deg,#8b5cf6,#6d28d9);}
.level2{background:linear-gradient(135deg,#3b82f6,#1d4ed8);}
.level3{background:linear-gradient(135deg,#1e40af,#1e3a8a);}

/* BOTTOM NAV - FIXED AT BOTTOM */
.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    width:100%;
    background:#ff7b2c;
    padding:12px 0 16px 0;
    z-index:999999;
    border-top:1px solid rgba(255,255,255,0.3);
    box-shadow:0 -4px 15px rgba(0,0,0,0.1);
}

.nav-item{
    text-align:center;
    color:white;
    font-size:12px;
    font-weight:600;
    opacity:0.8;
}
.nav-item.active{
    opacity:1;
    font-weight:800;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "register"
if "user" not in st.session_state:
    st.session_state.user = "Member"
if "balance" not in st.session_state:
    st.session_state.balance = 0.00
if "invite_code" not in st.session_state:
    st.session_state.invite_code = f"NHS{random.randint(100000,999999)}"
if "active_vip" not in st.session_state:
    st.session_state.active_vip = None

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
    st.subheader("Create Your NHS Account")

    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("First Name", placeholder="David", key="fname")
    with col2:
        lname = st.text_input("Last Name", placeholder="Okon", key="lname")
    
    email = st.text_input("Email Address", placeholder="you@email.com", key="email")
    password = st.text_input("Password", type="password", placeholder="Min 6 characters", key="pwd")
    invite = st.text_input("Invitation Code", value="NHS2026", key="invite")

    if st.button("Sign Up to NHS", key="signup"):
        if fname and email and len(password) >= 6:
            st.session_state.user = fname
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Please fill all fields. Password must be 6+ characters.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
elif st.session_state.page == "home":
    st.markdown(f"""
    <div class="main-header">
        <div style="display:flex;align-items:center;gap:12px;">
            <div class="logo-box" style="width:60px;height:60px;font-size:28px;">N</div>
            <div style="text-align:left;">
                <div style="font-size:30px;font-weight:900;">NHS</div>
                <div style="font-size:13px;opacity:0.9;">Welcome {st.session_state.user}</div>
            </div>
        </div>
        <div style="margin-top:25px;">
            <div style="font-size:15px;opacity:0.9;">Total Balance</div>
            <div style="font-size:48px;font-weight:900;">₦{st.session_state.balance:,.0f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    names = ["Precious", "Musa", "Blessing", "Chidi", "Ade", "Fatima", "David"]
    st.markdown(f"""
    <div class="ticker">
        🔥 {random.choice(names)} just withdrew ₦{random.randint(15,150)},000 successfully
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="white-card">
        <h3 style="margin-top:0;">About NHS</h3>
        <p style="line-height:1.7;color:#4b5563;">
        NHS is a digital financial growth platform built for Nigerians. 
        We provide fast Naira deposits, instant VIP activation, daily profit tracking, 
        and secure investment management. Join thousands earning daily.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### NHS VIP Plans")

    vips = [
        {"name":"VIP 1 - Porsche Plan", "price":5000, "daily":1200, "img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800"},
        {"name":"VIP 2 - Rolex Plan", "price":15000, "daily":3500, "img":"https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"},
        {"name":"VIP 3 - Real Estate Plan", "price":35000, "daily":8200, "img":"https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800"},
        {"name":"VIP 4 - Gold Reserve Plan", "price":70000, "daily":16500, "img":"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800"},
    ]

    for vip in vips:
        st.markdown(f"""
        <div class="vip-card">
            <img class="vip-img" src="{vip['img']}">
            <div class="vip-profit">₦{vip['daily']:,}</div>
            <div style="color:#6b7280;font-weight:600;">Daily Profit</div>
            <div class="vip-price">₦{vip['price']:,}</div>
            <div style="color:#6b7280;font-weight:600;">{vip['name']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Activate {vip['name']}", key=f"vip_{vip['name']}"):
            st.session_state.active_vip = vip['name']
            st.session_state.page = "deposit"
            st.rerun()

    st.markdown("""
    <div class="white-card">
        <h3 style="margin-top:0;">Recent Withdrawals</h3>
    """, unsafe_allow_html=True)

    for i in range(5):
        st.markdown(f"""
        <div class="member-box">
            +₦{random.randint(20,200)},000<br>
            <span style="color:#6b7280;font-size:13px;">user****{random.randint(1000,9999)}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROJECT/VIP PAGE ----------------
elif st.session_state.page == "project":
    st.markdown("""
    <div class="main-header">
        <div class="brand-name">NHS Projects</div>
        <div class="brand-sub">Choose Your Investment Plan</div>
    </div>
    """, unsafe_allow_html=True)

    vips = [
        {"name":"VIP1", "price":"₦5,000", "daily":"₦1,200", "cycle":"30 Days"},
        {"name":"VIP2", "price":"₦15,000", "daily":"₦3,500", "cycle":"30 Days"},
        {"name":"VIP3", "price":"₦35,000", "daily":"₦8,200", "cycle":"30 Days"},
        {"name":"VIP4", "price":"₦70,000", "daily":"₦16,500", "cycle":"30 Days"},
    ]

    for vip in vips:
        st.markdown(f"""
        <div class="white-card">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <div style="font-weight:800;font-size:18px;">{vip['name']}</div>
                    <div style="font-size:13px;color:#6b7280;margin-top:5px;">Daily profit</div>
                    <div style="color:#16a34a;font-weight:700;font-size:16px;">{vip['daily']}</div>
                    <div style="font-size:13px;color:#6b7280;margin-top:5px;">Invest cycle</div>
                    <div style="color:#16a34a;font-weight:700;">{vip['cycle']}</div>
                </div>
                <div style="text-align:right;">
                    <div style="background:#111827;color:white;padding:10px 20px;border-radius:50px;font-weight:700;">{vip['price']} Buy now</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- DEPOSIT PAGE - SHOWS YOUR ACCOUNT ----------------
elif st.session_state.page == "deposit":
    st.markdown("""
    <div class="main-header">
        <div class="brand-name">Fund Wallet</div>
        <div class="brand-sub">Deposit to activate VIP</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.active_vip:
        st.info(f"Selected: {st.session_state.active_vip}")

    st.markdown("""
    <div class="white-card">
        <h3 style="margin-top:0;">Bank Transfer Details</h3>
        <div class="deposit-box">
            <p style="margin:0;color:#6b7280;font-weight:600;">BANK NAME</p>
            <h2 style="margin:8px 0;color:#111827;font-weight:900;">MONIEPOINT</h2>
            
            <p style="margin:20px 0 0 0;color:#6b7280;font-weight:600;">ACCOUNT NUMBER</p>
            <h1 style="color:#ff6a00;margin:8px 0;font-size:36px;letter-spacing:2px;">8126419410</h1>
            
            <p style="margin:20px 0 0 0;color:#6b7280;font-weight:600;">ACCOUNT NAME</p>
            <h3 style="color:#111827;margin:8px 0;">NHS FINANCIAL LTD</h3>
        </div>
        <br>
        <div style="background:#f0fdf4;padding:16px;border-radius:16px;border:2px solid #22c55e;">
            <div style="color:#166534;font-weight:600;">✅ After payment, click "I Have Paid" below</div>
            <div style="color:#166534;font-size:13px;margin-top:5px;">Your wallet will be credited in 5-10 minutes</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("I HAVE MADE PAYMENT", key="paid"):
        st.success("Deposit received! Verification in progress. You will be credited soon.")
        st.balloons()

    if st.button("Back to Home", key="back_home"):
        st.session_state.page = "home"
        st.rerun()

# ---------------- TEAM PAGE ----------------
elif st.session_state.page == "team":
    st.markdown("""
    <div class="main-header">
        <div class="brand-name">My Team</div>
        <div class="brand-sub">Invite & Earn Together</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="white-card">
        <div style="background:#f3f4f6;padding:18px;border-radius:18px;text-align:center;">
            <div style="color:#6b7280;font-size:14px;font-weight:600;">Your Invitation Code</div>
            <div style="font-size:34px;font-weight:900;letter-spacing:3px;color:#ff6a00;">{st.session_state.invite_code}</div>
        </div>
        <div style="margin-top:15px;color:#6b7280;font-size:13px;text-align:center;">
            Share this code with friends. Earn 10% commission when they deposit.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="white-card" style="background:#fef3c7;">
        <div style="display:flex;justify-content:space-around;text-align:center;">
            <div>
                <div style="color:#92400e;font-size:13px;font-weight:600;">Team Size</div>
                <div style="font-size:28px;font-weight:900;color:#92400e;">0</div>
            </div>
            <div>
                <div style="color:#92400e;font-size:13px;font-weight:600;">Team Earnings</div>
                <div style="font-size:28px;font-weight:900;color:#92400e;">₦0</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    levels = [
        {"level": "LEVEL 1", "commission": "16%", "class": "level1"},
        {"level": "LEVEL 2", "commission": "2%", "class": "level2"},
        {"level": "LEVEL 3", "commission": "1%", "class": "level3"},
    ]

    for lvl in levels:
        st.markdown(f"""
        <div class="team-level {lvl['class']}">
            <div style="position:absolute;top:10px;left:-5px;background:#fbbf24;color:#000;padding:5px 15px;transform:rotate(-45deg);font-size:12px;font-weight:bold;">{lvl['level']}</div>
            <div style="display:flex;justify-content:space-between;margin-top:20px;">
                <div>
                    <div style="font-size:13px;opacity:0.9;">Register/Valid</div>
                    <div style="font-size:20px;font-weight:bold;">0/0</div>
                    <div style="font-size:13px;opacity:0.9;margin-top:10px;">Task rebate</div>
                    <div style="font-size:20px;font-weight:bold;">1%</div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:13px;opacity:0.9;">Commission Percentage</div>
                    <div style="font-size:20px;font-weight:bold;">{lvl['commission']}</div>
                    <div style="font-size:13px;opacity:0.9;margin-top:10px;">Total Income</div>
                    <div style="font-size:20px;font-weight:bold;">0</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- ME/PROFILE PAGE ----------------
elif st.session_state.page == "me":
    st.markdown(f"""
    <div class="main-header">
        <div style="display:flex;align-items:center;gap:12px;">
            <div class="logo-box" style="width:65px;height:65px;font-size:30px;">N</div>
            <div style="text-align:left;">
                <div style="font-size:32px;font-weight:900;">{st.session_state.user}</div>
                <div style="font-size:13px;opacity:0.9;">NHS Member</div>
            </div>
        </div>
        <div style="margin-top:25px;">
            <div style="font-size:15px;opacity:0.9;">Total Balance</div>
            <div style="font-size:48px;font-weight:900;">₦{st.session_state.balance:,.0f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="white-card">
        <div style="display:flex;justify-content:space-around;text-align:center;padding:5px 0;">
            <div style="cursor:pointer;" onclick="window.location.href='#'">💰<br><span style="font-size:12px;font-weight:600;">Recharge</span></div>
            <div style="cursor:pointer;">💸<br><span style="font-size:12px;font-weight:600;">Withdraw</span></div>
            <div style="cursor:pointer;">📊<br><span style="font-size:12px;font-weight:600;">Records</span></div>
            <div style="cursor:pointer;">🎁<br><span style="font-size:12px;font-weight:600;">Bonus</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    menu_items = ["Transaction History", "Change Password", "Customer Service", "Logout"]
    for item in menu_items:
        if st.button(item, key=f"menu_{item}", use_container_width=True):
            if item == "Logout":
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.rerun()
            elif item == "Customer Service":
                st.session_state.page = "deposit"
                st.rerun()

# ---------------- BOTTOM NAV - FIXED AT BOTTOM ----------------
if st.session_state.page!= "register":
    st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠\nHome", key="nav_home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("💎\nProject", key="nav_project", use_container_width=True):
            st.session_state.page = "project"
            st.rerun()
    with col3:
        if st.button("👥\nTeam", key="nav_team", use_container_width=True):
            st.session_state.page = "team"
            st.rerun()
    with col4:
        if st.button("👤\nMe", key="nav_me", use_container_width=True):
            st.session_state.page = "me"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
