import streamlit as st
import os

def render_certificates(config):
    """Renders the Certificates section in a 2x2 grid with local image support."""
    st.markdown('<div id="certificates" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("Certificates & Achievements")
    st.write("Accredited certifications, workshop completions, and academic credentials.")

    for row_idx in range(0, len(config["CERTIFICATES"]), 2):
        row_certs = config["CERTIFICATES"][row_idx:row_idx + 2]
        cols = st.columns(2)
        for col_idx, cert in enumerate(row_certs):
            with cols[col_idx]:
                with st.container(border=True):
                    img_path = cert.get("image", "")
                    if os.path.exists(img_path):
                        st.image(img_path, caption=cert["title"], use_container_width=True)
                    else:
                        st.markdown(
                            f"""
                            <div style="background: rgba(30, 41, 59, 0.4); border: 2px dashed rgba(59, 130, 246, 0.35); border-radius: 10px; padding: 40px 15px; text-align: center; margin-bottom: 12px;">
                                <p style="color: #93c5fd; font-weight: 600; margin: 0 0 6px 0;">Certificate Image</p>
                                <p style="color: #64748b; font-size: 0.8rem; margin: 0;">Save image to <code>{img_path}</code></p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    st.subheader(cert["title"])
                    st.markdown(f"**Issuer:** `{cert['issuer']}` | **Date:** `{cert['date']}`")
                    st.caption(cert["description"])
