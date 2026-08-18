# ------------------------ MAIN INITIATION(ENTRY-POINT) FILE ------------------------

# IMPORT NECESSARY PACKAGES

# import streamlit packages
import streamlit as st

def main():
    '''This function is used to set the basic configuration options for the USPC Ticketing application'''
    st.set_page_config(
        page_title="USPC Ticketer",
        page_icon="assets/USPC_LOGO.png",
        initial_sidebar_state="auto",
        layout="centered",
        menu_items={
            "Report a bug": "mailto:jeffrygeorge58@gmail.com",
            "About": "USPC Manchester's Official Ticket Booking Application v1.0 ® 2026. All Rights Reserved."
        }
    )

    nav_pages = [
        st.Page("home.py")
    ]

    ticketer_pages = st.navigation(pages=nav_pages, position="hidden")
    
    ticketer_pages.run()

if __name__ == '__main__':
    main()
