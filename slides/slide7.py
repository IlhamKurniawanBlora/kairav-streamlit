import streamlit as st

def render():

    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>Education</h1>
                <p>"I am currently pursuing a Bachelor's degree in Informatics at Nahdlatul Ulama University Yogyakarta, where I am learning various topics including software development, databases, programming, and networking."</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
