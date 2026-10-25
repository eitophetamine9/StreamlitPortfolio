import streamlit as st
import os

def render_hero(config):
    """Renders the About Me / Hero section with photo, bio, and metrics."""
    st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)

    col_photo, col_intro = st.columns([1, 2.5], gap="medium")

    with col_photo:
        photo_src = config.get("PHOTO_URL", "assets/profile.png")
        if os.path.exists(photo_src):
            st.image(photo_src, caption=config["NAME"], use_container_width=True)
        elif photo_src.startswith("http://") or photo_src.startswith("https://"):
            st.image(photo_src, caption=config["NAME"], use_container_width=True)
        else:
            st.image(
                "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80",
                caption=f"{config['NAME']} (Place image at {photo_src})",
                use_container_width=True
            )

    with col_intro:
        st.markdown(f'<span class="tag-badge">{config["SECTION"]}</span>', unsafe_allow_html=True)
        st.title(config["NAME"])
        st.subheader(config["PROGRAM_YEAR"])
        st.write(config["BIO"])
        
        # Required Extra: Metrics
        m1, m2 = st.columns(2)
        m1.metric("Projects", len(config["PROJECTS"]))
        m2.metric("Status", "Active Student")
