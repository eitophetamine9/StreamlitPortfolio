import streamlit as st
import pandas as pd

def render_skills(config):
    """Renders the Skills matrix with interactive selectbox, slider, bar chart, and dataframe."""
    st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("Skills & Technical Proficiency")

    df_skills = pd.DataFrame(config["SKILLS"])

    # Required Widgets: Selectbox & Slider
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        cats = ["All"] + sorted(list(df_skills["Category"].unique()))
        selected_cat = st.selectbox("Filter by Category:", cats)
    with f_col2:
        min_prof = st.slider("Minimum Proficiency Level:", 0, 100, 50)

    # Filter dataframe
    filtered_df = df_skills if selected_cat == "All" else df_skills[df_skills["Category"] == selected_cat]
    filtered_df = filtered_df[filtered_df["Proficiency"] >= min_prof]

    # Required: Chart with numbers
    st.subheader("Proficiency Ratings (0-100)")
    if not filtered_df.empty:
        st.bar_chart(filtered_df.set_index("Skill")[["Proficiency"]], color="#3b82f6")
    else:
        st.info("No skills match the current filter.")

    # Required Widget: Checkbox + Table/Dataframe
    show_table = st.checkbox("Show skills data table", value=True)
    if show_table:
        st.dataframe(filtered_df, use_container_width=True)
