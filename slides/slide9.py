import streamlit as st

def render():

    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>Testimonials</h1>
                <p>"Ilham is a great developer with a keen eye for detail and design. He was a key part of our team in building the new company website." – KAIRAV</p>
                <p>"Working with Ilham was a fantastic experience. His dedication and problem-solving skills helped bring our educational platform to life in a way that’s both user-friendly and visually appealing." – MinnaEdu</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
