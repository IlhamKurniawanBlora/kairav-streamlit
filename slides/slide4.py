import streamlit as st

def render():

    st.markdown(
        """
        <div class="fullscreen">
            <div>
                <h1>My Recent Projects</h1>
                <p>Kairav Portfolio
                    <a href="https://kairav-portfolio.vercel.app" target="_blank" class="project-link">Visit Project</a>
                </p>
                <p>MinnaEdu 
                    <a href="https://minnaedu.vercel.app" target="_blank" class="project-link">Visit Project</a>
                </p>
                <p>For a complete list of my projects, visit my 
                    <a href="https://github.com/IlhamKurniawanBlora" target="_blank" class="github-link">GitHub</a>.
                </p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
