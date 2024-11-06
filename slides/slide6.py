import streamlit as st

def render():
    st.markdown(
        """
         <div class="fullscreen">
            <div>
                <h1>Skills and Technologies</h1>
                <p>Here are some of the programming languages, frameworks, and tools I frequently work with:</p>
                <ul>
                    <li>Python</li>
                    <li>JavaScript (JS)</li>
                    <li>TypeScript (TS)</li>
                    <li>SQL</li>
                    <li>Vue.js</li>
                    <li>Nuxt.js</li>
                    <li>Flutter</li>
                    <li>Streamlit</li>
                    <li>Laravel</li>
                    <li>Flask</li>
                    <li>Django</li>
                </ul>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
