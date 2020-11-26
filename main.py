import streamlit as st
from src.GUI.main_page import MainPage
from src.GUI.menu import Menu
import bcrypt


def main():
    with open("src/login.txt", "r+") as f:
        check = f.readline() == "True"
        f.close()
    main_page = MainPage()
    main_page.call()
    if check:
        st.sidebar.success("Login successful!")
        is_clicked = st.sidebar.button("Log out")
        if is_clicked:
            with open("src/login.txt", "w") as f:
                f.write("False")
                f.close()
        main_page.clear()
        menu = Menu()
        menu.display_option()
    else:
        st.sidebar.title("Login section")
        input_password = st.sidebar.text_input("Input administrator password: ", type="password", value="")
        st.sidebar.write("Note: this is a collapsible sidebar.")
        if input_password == "password":
            with open("src/login.txt", "w") as f:
                f.write("True")
                f.close()
            st.empty()
        else:
            st.sidebar.warning("Wrong password!")
            st.stop()


if __name__ == "__main__":
    main()
