import streamlit as st

def render():
    # Menggunakan div dengan kelas fullscreen untuk menampung konten slide 1
    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>Welcome to My Portfolio</h1>
                <p>Hi, I'm Ilham Kurniawan, an aspiring web developer. Welcome to my portfolio!</p>
                <p>Here you'll find my projects, skills, and more about my journey in web development.</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )


