import streamlit as st

def render():
    # Menampilkan konten dalam layout full screen
    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>About Me</h1>
                <p>"I am a passionate web developer from Yogyakarta, dedicated to creating user-friendly and accessible websites. I am always excited to learn new technologies and aim to deliver improved user experiences through my work."</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
