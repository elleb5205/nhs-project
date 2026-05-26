import streamlit as st
import random
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NHS | Financial Growth",
    page_icon="🅝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS - NHS ORANGE THEME ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#ff6a00;
    background-image: radial-gradient(circle at top right,#ff944d,#ff6a00);
    color:white;
    padding-bottom: 90px;
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
input{
    border-radius:15px !important;
    border:2px solid #e5e7eb !important;
    padding:15px !important;
    background:#f9fafb !important;
    color:black !important;
    font-weight:500 !important;
}

input:focus{
    border:2px solid #ff6a00 !important;
    box-shadow:none !important;
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

/* LIVE TICKER */
.ticker{
    background:white;
    color:#16a34a;
    padding:12px;
    border-radius:16px;
    font-weight:700;
    margin-bottom:18px;
    box-shadow:0 4px 10px rgba(0
