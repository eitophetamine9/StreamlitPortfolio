import streamlit as st
import os

def render_sidebar(config):
    """Renders a subtle, non-intrusive sidebar satisfying the rubric requirement."""
    with st.sidebar:
        # Profile thumbnail if available
        if os.path.exists(config.get("PHOTO_URL", "")):
            st.image(config["PHOTO_URL"], width=90)
        
        st.markdown(f"### {config['NAME']}")
        st.caption(f"**{config['SECTION']}**")
        st.caption(f"{config['PROGRAM_YEAR']}")
        
        st.divider()
        
        st.markdown("#### Quick Jump")
        st.markdown("- [About Me](#about)")
        st.markdown("- [Autobiography](#autobiography)")
        st.markdown("- [Skills Matrix](#skills)")
        st.markdown("- [Featured Projects](#projects)")
        st.markdown("- [Certificates](#certificates)")
        st.markdown("- [GitHub Contributions](#github)")
        st.markdown("- [Contact Form](#contact)")
        
        st.divider()
        st.link_button("GitHub Profile", config["GITHUB_URL"], use_container_width=True)
