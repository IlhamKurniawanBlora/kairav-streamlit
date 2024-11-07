import streamlit as st

def render():

    st.markdown(
        """
       <div class="fullscreen">
            <div>
                <h1>Contact Me</h1>
                <p>Feel free to reach out to me for any inquiries or freelance work opportunities.</p>
                <p>
                    <a href="mailto:ilhamkurniawanjateng@gmail.com" style="text-decoration: none; color: black;">
                        ✉️ Email
                    </a>
                </p>
                <p>
                    <a href="https://www.instagram.com/ilhamkrnwan__" target="_blank" style="text-decoration: none; color: black;">
                        📷 Instagram
                    </a>
                </p>
                <p>
                    <a href="https://www.linkedin.com/in/yourusername" target="_blank" style="text-decoration: none; color: black;">
                        💼 LinkedIn
                    </a>
                </p>
                <p>
                    <a href="https://github.com/IlhamKurniawanBlora" target="_blank" style="text-decoration: none; color: black;">
                        🖥️ GitHub
                    </a>
                </p>
            </div>
        </div>

        """, 
        unsafe_allow_html=True
    )
