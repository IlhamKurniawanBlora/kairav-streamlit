import streamlit as st

def render():

    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>Certifications & Training</h1>
                <p>I have completed courses in:</p>
                <ul>
                    <li>Web Development Bootcamp by RGI Surabaya</li>
                    <li>Graphic Design by Dinperinaker Blora</li>
                </ul>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
