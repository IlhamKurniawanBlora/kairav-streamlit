import streamlit as st

def render():

    st.markdown(
        """
       <div class="fullscreen">
            <div>
                <h1>My Hobbies</h1>
                <p>Apart from web development, I enjoy various activities that keep me inspired and refreshed. Here are a few of my hobbies:</p>
                <ul>
                    <li>Reading Tech Blogs</li>
                    <li>Photography</li>
                    <li>Cooking</li>
                    <li>Gaming</li>
                </ul>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
