import streamlit as st

def apply_custom_styles():
    """Injects modern Plus Jakarta Sans typography, dark slate theme, and smooth scroll styles."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Modern Typography */
    html, body, [class*="css"], [data-testid="stAppViewContainer"], .stMarkdown, .stText, p, div, span, label, input, button, select, textarea {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        letter-spacing: -0.01em;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
    }

    code, kbd, samp, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Subtle Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #0b1120 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown p {
        font-size: 0.9rem;
    }

    /* Smooth Scrolling & Anchor Offset */
    html {
        scroll-behavior: smooth !important;
    }
    .section-anchor {
        scroll-margin-top: 85px;
    }

    /* Top Sticky Navigation Bar */
    .top-nav {
        position: sticky;
        top: 2.8rem;
        z-index: 99;
        background: rgba(15, 23, 42, 0.88);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 8px 16px;
        margin-bottom: 25px;
        display: flex;
        justify-content: center;
        gap: 14px;
        flex-wrap: wrap;
    }
    .top-nav a {
        color: #e2e8f0 !important;
        text-decoration: none !important;
        font-size: 0.9rem;
        font-weight: 500;
        padding: 5px 12px;
        border-radius: 6px;
        transition: background 0.2s ease;
    }
    .top-nav a:hover {
        background: rgba(59, 130, 246, 0.3);
        color: #ffffff !important;
    }

    /* Badges & Tags */
    .tag-badge {
        background: #2563eb;
        color: white;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }

    /* Project Cards & Equal Height Helpers */
    .project-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .proj-title {
        font-size: 1.25rem;
        font-weight: 700;
        min-height: 3.2rem;
        display: flex;
        align-items: center;
        margin-bottom: 0.3rem;
    }
    .proj-tools {
        min-height: 2.8rem;
        margin-bottom: 0.5rem;
    }
    .proj-outcome {
        background: rgba(30, 41, 59, 0.45);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 10px;
        padding: 12px 14px;
        min-height: 120px;
        margin-bottom: 15px;
        font-size: 0.88rem;
        line-height: 1.5;
        color: #cbd5e1;
    }

    /* GitHub Heatmap Container */
    .gh-container {
        background: #0d1117;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 24px 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: border-color 0.2s ease;
    }
    .gh-container:hover {
        border-color: rgba(59, 130, 246, 0.45);
    }
    .gh-chart-img {
        width: 100%;
        max-width: 1100px;
        height: auto;
        display: block;
        margin: 0 auto;
        transition: transform 0.2s ease;
        cursor: pointer;
    }
    .gh-chart-img:hover {
        transform: scale(1.01);
    }

    /* Buttons & Interactive Components */
    div.stButton > button, div.stLinkButton > a {
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    div.stLinkButton > a:hover {
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35) !important;
        transform: translateY(-1px);
    }
    button[data-baseweb="tab"] {
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)


def render_top_navbar():
    """Renders the top sticky smooth-scroll navigation bar."""
    st.markdown("""
    <div class="top-nav">
        <a href="#about">About</a>
        <a href="#autobiography">Autobiography</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#certificates">Certificates</a>
        <a href="#github">GitHub</a>
        <a href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)


def render_footer(config):
    """Renders the subtle footer."""
    st.markdown(
        f"""
        <div style="text-align: center; color: #64748b; padding-top: 40px; padding-bottom: 20px; font-size: 0.85rem;">
            <p><strong>{config['NAME']}</strong> &bull; {config['SECTION']} &bull; Built with Streamlit</p>
            <p><a href="#about" style="color: #3b82f6; text-decoration: none;">Back to Top</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
