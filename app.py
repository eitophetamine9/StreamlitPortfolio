import streamlit as st
from config import CONFIG
from styles import apply_custom_styles, render_top_navbar, render_footer
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.autobiography import render_autobiography
from components.skills import render_skills
from components.projects import render_projects
from components.certificates import render_certificates
from components.github_section import render_github
from components.contact import render_contact

def main():
    # ── Page Configuration ──
    st.set_page_config(
        page_title=f"{CONFIG['NAME']} | Portfolio",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # ── Session State Initialization ──
    if "feedback_list" not in st.session_state:
        st.session_state.feedback_list = []

    # ── Custom Styling & Top Sticky Navigation ──
    apply_custom_styles()
    render_top_navbar()

    render_sidebar(CONFIG)

    # ── Main Sections ──
    render_hero(CONFIG)
    st.divider()

    render_autobiography(CONFIG)
    st.divider()

    render_skills(CONFIG)
    st.divider()

    render_projects(CONFIG)
    st.divider()

    render_certificates(CONFIG)
    st.divider()

    render_github(CONFIG)
    st.divider()

    render_contact(CONFIG)

    # ── Footer ──
    render_footer(CONFIG)

if __name__ == "__main__":
    main()
