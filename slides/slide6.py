import streamlit as st

def render():
    st.markdown(
        """
         <div class="fullscreen">
            <div>
                <h1>Skills and Technologies</h1>
                <p>Here are some of the programming languages, frameworks, and tools I frequently work with:</p>
                <ul>
                    <li>HTML</li>
                    <li>CSS</li>
                    <li>JS</li>
                    <li>PHP</li>
                    <li>SCSS</li>
                    <li>PY</li>
                    <li>SQL</li>
                    <li>TS</li>
                    <li>DART</li>
                </ul>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
