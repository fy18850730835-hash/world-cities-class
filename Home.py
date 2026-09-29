import streamlit as st

st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 World Cities App")

st.markdown("""
    Welcome to the World Cities Application!
    
    This app helps you explore and discover information about cities around the world.
    Click the button below to get started exploring cities.
""")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Go to Cities Explorer", key="explore_button", use_container_width=True):
        st.switch_page("pages/app.py")

st.markdown("---")
st.markdown("""
    ### Features
    - Explore cities worldwide
    - Discover city information and statistics
    - Learn about different regions
    
    Navigate to the **Cities Explorer** page using the button above or the sidebar.
""")
