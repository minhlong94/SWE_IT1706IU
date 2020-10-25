import streamlit as st

# Security
import hashlib


def _make_hashes(password):
    return hashlib.sha256(password).hexdigest()


def _check_hashes(password, hashed_password):
    if _make_hashes(password) == hashed_password:
        return hashed_password
    return False


def login_page():
    st.subheader("Login Section")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
