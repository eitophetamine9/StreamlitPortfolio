import streamlit as st

def render_autobiography(config):
    """Renders the Autobiography & Hobbies section using tabs."""
    st.markdown('<div id="autobiography" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("Autobiography & Interests")

    # Required Extra: Tabs
    tab_bio, tab_edu, tab_hobbies = st.tabs(["Background", "Education & Milestones", "Hobbies & Interests"])

    with tab_bio:
        st.subheader("My Story")
        st.write(config["BACKGROUND"])

    with tab_edu:
        st.subheader("Education")
        for edu in config["EDUCATION"]:
            st.markdown(f"**{edu['level']}** — *{edu['school']}* ({edu['period']})")
            st.caption(edu["details"])
        
        st.divider()
        st.subheader("Key Milestones")
        for m in config["MILESTONES"]:
            st.markdown(f"- **{m['year']}**: {m['event']}")

    with tab_hobbies:
        st.subheader("Hobbies & Interests")
        hob_cols = st.columns(len(config["HOBBIES"]))
        for i, h in enumerate(config["HOBBIES"]):
            with hob_cols[i]:
                with st.container(border=True):
                    st.markdown(f"**{h['name']}**")
                    st.caption(h["desc"])
