import streamlit as st

def render_github(config):
    """Renders the GitHub contributions section with direct link and commit heatmap."""
    st.markdown('<div id="github" class="section-anchor"></div>', unsafe_allow_html=True)

    gh_head_col, gh_btn_col = st.columns([3, 1])
    with gh_head_col:
        st.header("GitHub Contributions")
        st.caption(f"Live activity and commit heatmap for **[@{config['GITHUB_USERNAME']}]({config['GITHUB_URL']})**")
    with gh_btn_col:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        st.link_button("Open GitHub Profile", config["GITHUB_URL"], use_container_width=True)

    # Real live GitHub contribution heatmap
    chart_url = f"https://ghchart.rshah.org/40c463/{config['GITHUB_USERNAME']}"
    st.markdown(
        f"""
        <div class="gh-container">
            <a href="{config['GITHUB_URL']}" target="_blank" title="Click to view @{config['GITHUB_USERNAME']} on GitHub" style="text-decoration: none;">
                <img src="{chart_url}" alt="GitHub Contribution Chart for {config['GITHUB_USERNAME']}" class="gh-chart-img" />
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
