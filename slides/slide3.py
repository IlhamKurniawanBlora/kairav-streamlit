import streamlit as st

def render():
    # Menggunakan div dengan kelas fullscreen untuk menampung konten
    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>My Services</h1>
                <ul>
                    <li>Frontend Development</li>
                    <li>Backend Development</li>
                    <li>Version Control and Collaboration</li>
                    <li>Database Management</li>
                    <li>CI/CD and Automation</li>
                </ul>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
