import streamlit as st

def render_projects(config):
    """Renders the Featured Projects section in an equal-sized 2x2 grid."""
    st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("Featured Projects")
    st.write("A collection of personal and practical projects and development skills.")

    # Required Widget: Radio filter
    proj_view = st.radio("Display view:", ["All Projects", "Featured Only"], horizontal=True)

    displayed_projects = config["PROJECTS"]
    if proj_view == "Featured Only":
        featured = [p for p in config["PROJECTS"] if p.get("status") == "Completed" or "AnchorPod" in p.get("title", "")]
        if featured:
            displayed_projects = featured

    # 2x2 grid layout with uniform box heights
    for row_idx in range(0, len(displayed_projects), 2):
        row_projects = displayed_projects[row_idx:row_idx + 2]
        cols = st.columns(2)
        for col_idx, proj in enumerate(row_projects):
            with cols[col_idx]:
                with st.container(border=True):
                    st.markdown(f'<div class="proj-title">{proj["title"]}</div>', unsafe_allow_html=True)
                    st.markdown(f"**Status:** `{proj.get('status', 'Completed')}`")
                    st.markdown(f"**Role:** `{proj['role']}`")
                    st.markdown(f'<div class="proj-tools"><strong>Tools:</strong> <code>{proj["tools"]}</code></div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="proj-outcome"><strong>Description:</strong> {proj["outcome"]}</div>', unsafe_allow_html=True)
                    st.link_button("View Project", proj["link"], use_container_width=True)
