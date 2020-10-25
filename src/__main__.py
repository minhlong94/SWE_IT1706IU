import streamlit as st
from src import GUI


def main():
    """Simple Login App"""

    st.title("Simple Login App")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        GUI.LoginPage.login_page()


if __name__ == '__main__':
    main()
