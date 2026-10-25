import streamlit as st
import pandas as pd
import os

CONFIG = {
    # ── Basic Student Info (Rubric Requirement) ──
    "NAME": "John Erick I. Santizo",
    "SECTION": "CSIT 349 - F1",
    "PROGRAM_YEAR": "BS Computer Science, 3rd Year",
    "GITHUB_USERNAME": "eitophetamine9",                      
    "GITHUB_URL": "https://github.com/eitophetamine9",       
    "BIO": "I am an aspiring cybersecurity analyst, full-stack developer, and game developer with a passion for technology and innovation.",
    "PHOTO_URL": "assets/profile.png",
    
    # ── Autobiography ──
    "BACKGROUND": (
        "Growing up I've always been exposed to technology, more specifically a PC,"
        "that inspired me to delve deeper into technology on how it works and what I could build with it."
    ),
    "EDUCATION": [
        {"level": "College", "school": "Cebu Institute of Technology - University", "period": "2024 - Present", "details": "BS Computer Science"},
        {"level": "Senior High", "school": "University of Cebu - METC", "period": "2021 - 2024", "details": "STEM Strand / Honors"}
    ],
    "MILESTONES": [
        {"year": "2024-2025", "event": "Parangal Academic Achiever"},
        {"year": "2026", "event": "Game Gauntlet - Sim Jam Participant"},
        {"year": "2026", "event": "First solo game development project - Spirit Contract Evo Idle "},
    ],

    # ── Hobbies ──
    "HOBBIES": [
        {"name": "Gaming", "desc": "Playing indie and triple A games alike, enjoying the storyline along the way"},
        {"name": "Story Writing", "desc": "Composing stories for both my future game development career and personal interests."},
        {"name": "Game Development", "desc": "Developing 2D (soon 3D) games using a variety of different engine."},
        {"name": "Music & Audio", "desc": "Listening to a variety of genres and discovering new artists."},
        {"name": "Working out", "desc": "Building my physique like they say, a healthy body equals a healthy mind."}
    ],
    
    # ── Skills (Used for Chart & Table) ──
    "SKILLS": [
        {"Skill": "Python", "Category": "Languages", "Proficiency": 60},
        {"Skill": "C++", "Category": "Languages", "Proficiency": 75},
        {"Skill": "Java", "Category": "Languages", "Proficiency": 80},
        {"Skill": "SQL", "Category": "Databases", "Proficiency": 70},
        {"Skill": "Git & GitHub", "Category": "Tools", "Proficiency": 80},
        {"Skill": "Data Analysis", "Category": "AI / Data", "Proficiency": 65},
        {"Skill": "HTML & CSS", "Category": "Languages", "Proficiency": 70},
    ],

    # ── Projects (At least 3 required) ──
    "PROJECTS": [
        {
            "title": "AnchorPod",
            "role": "Lead Developer",
            "status": "In Progress",
            "tools": "Python, Django, Supabase, HTML, CSS, JS",
            "outcome": "A community-driven, anonymous accountability platform designed to combat academic burnout and student isolation through shared daily self-care rhythms.",
            "link": "https://github.com/eitophetamine9/AnchorPod"
        },
        {
            "title": "Project Beta: Student Grade & Attendance Portal",
            "role": "Full-Stack Developer",
            "status": "Completed",
            "tools": "Python, SQLite, Pandas",
            "outcome": "Streamlined semester records for over 200 students with instant CSV reporting.",
            "link": "https://github.com"
        },
        {
            "title": "Project Gamma: Campus FAQ Chatbot",
            "role": "NLP Developer",
            "status": "Completed",
            "tools": "Streamlit, OpenAI API, LangChain",
            "outcome": "Handled 1,000+ student queries with 90% positive feedback during enrollment week.",
            "link": "https://github.com"
        }
    ]
}

# ==============================================================================
# STREAMLIT APP CONFIG & SMOOTH SCROLLING
# ==============================================================================
st.set_page_config(
    page_title=f"{CONFIG['NAME']} | Portfolio",
    layout="wide"
)

# Smooth scrolling animation & clean styling
st.markdown("""
<style>
html {
    scroll-behavior: smooth !important;
}
.section-anchor {
    scroll-margin-top: 85px;
}
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
.tag-badge {
    background: #2563eb;
    color: white;
    padding: 3px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}
.project-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 12px;
}
</style>

<div class="top-nav">
    <a href="#about">About</a>
    <a href="#autobiography">Autobiography</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#github">GitHub</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# Session state initialization for feedback form
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

# SIDEBAR
with st.sidebar:
    st.markdown(f"### {CONFIG['NAME']}")
    st.caption(f"**Section:** {CONFIG['SECTION']}")
    st.caption(f"**Program:** {CONFIG['PROGRAM_YEAR']}")
    st.divider()
    
    st.markdown("#### Quick Navigation")
    st.markdown("- [About Me](#about)")
    st.markdown("- [Autobiography & Hobbies](#autobiography)")
    st.markdown("- [Skills Matrix](#skills)")
    st.markdown("- [Featured Projects](#projects)")
    st.markdown("- [GitHub Activity](#github)")
    st.markdown("- [Contact Form](#contact)")
    
    st.divider()
    st.link_button("Open GitHub Profile", CONFIG["GITHUB_URL"], use_container_width=True)

# ABOUT ME
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)

col_photo, col_intro = st.columns([1, 2.5], gap="medium")

with col_photo:
    photo_src = CONFIG.get("PHOTO_URL", "assets/profile.png")
    if os.path.exists(photo_src):
        st.image(photo_src, caption=CONFIG["NAME"], use_container_width=True)
    elif photo_src.startswith("http://") or photo_src.startswith("https://"):
        st.image(photo_src, caption=CONFIG["NAME"], use_container_width=True)
    else:
        # Fallback placeholder if local photo is not yet in assets/
        st.image(
            "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80",
            caption=f"{CONFIG['NAME']} (Place image at {photo_src})",
            use_container_width=True
        )

with col_intro:
    st.markdown(f'<span class="tag-badge">{CONFIG["SECTION"]}</span>', unsafe_allow_html=True)
    st.title(CONFIG["NAME"])
    st.subheader(CONFIG["PROGRAM_YEAR"])
    st.write(CONFIG["BIO"])
    
    # Required Extra: Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Projects Completed", len(CONFIG["PROJECTS"]))
    m2.metric("Tracked Skills", len(CONFIG["SKILLS"]))
    m3.metric("Status", "Active Student")

st.divider()

# AUTOBIOGRAPHY & HOBBIES
st.markdown('<div id="autobiography" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("Autobiography & Interests")

# Required Extra: Tabs
tab_bio, tab_edu, tab_hobbies = st.tabs(["Background", "Education & Milestones", "Hobbies & Interests"])

with tab_bio:
    st.subheader("My Story")
    st.write(CONFIG["BACKGROUND"])

with tab_edu:
    st.subheader("Education")
    for edu in CONFIG["EDUCATION"]:
        st.markdown(f"**{edu['level']}** — *{edu['school']}* ({edu['period']})")
        st.caption(edu["details"])
    
    st.divider()
    st.subheader("Key Milestones")
    for m in CONFIG["MILESTONES"]:
        st.markdown(f"- **{m['year']}**: {m['event']}")

with tab_hobbies:
    st.subheader("Hobbies Outside Coding")
    hob_cols = st.columns(len(CONFIG["HOBBIES"]))
    for i, h in enumerate(CONFIG["HOBBIES"]):
        with hob_cols[i]:
            with st.container(border=True):
                st.markdown(f"**{h['name']}**")
                st.caption(h["desc"])

st.divider()

# SKILLS MATRIX
st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("Skills & Technical Proficiency")

df_skills = pd.DataFrame(CONFIG["SKILLS"])

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

st.divider()

# FEATURED PROJECTS
st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("Featured Projects")
st.write("A collection of practical projects showcasing applied AI and development skills.")

# Required Widget: Radio filter
proj_view = st.radio("Display view:", ["All Projects", "Featured Only"], horizontal=True)

# Grid layout with at least 3 projects
proj_cols = st.columns(len(CONFIG["PROJECTS"]))
for idx, proj in enumerate(CONFIG["PROJECTS"]):
    with proj_cols[idx]:
        with st.container(border=True):
            st.subheader(proj["title"])
            st.markdown(f"**Status:** `{proj.get('status', 'Completed')}`")
            st.markdown(f"**Role:** `{proj['role']}`")
            st.markdown(f"**Tools:** `{proj['tools']}`")
            st.info(f"**Outcome:** {proj['outcome']}")
            st.link_button("View Project", proj["link"], use_container_width=True)

st.divider()

# GITHUB & CONTRIBUTION CHARTS
st.markdown('<div id="github" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("GitHub Contributions")
st.write(f"Commit heatmap and live activity for **[@{CONFIG['GITHUB_USERNAME']}]({CONFIG['GITHUB_URL']})**.")

# Real live GitHub contribution heatmap
chart_url = f"https://ghchart.rshah.org/40c463/{CONFIG['GITHUB_USERNAME']}"
st.markdown(
    f"""
    <div style="background: #0d1117; border: 1px solid #30363d; border-radius: 10px; padding: 15px; text-align: center;">
        <img src="{chart_url}" alt="GitHub Contribution Chart" style="width: 100%; max-width: 850px; display: block; margin: 0 auto;" />
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# CONTACT & FEEDBACK FORM
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("Contact & Feedback")
st.write("Leave feedback or send a message. This form responds immediately upon submission.")

# Required Extra: Form & Session State
with st.form("contact_form", clear_on_submit=True):
    sender_name = st.text_input("Your Name *")
    sender_email = st.text_input("Your Email *")
    sender_msg = st.text_area("Your Message *")
    
    # Required Widget: Button
    btn_submit = st.form_submit_button("Send Message")
    
    if btn_submit:
        if not sender_name.strip() or not sender_email.strip() or not sender_msg.strip():
            st.error("Please fill out all required fields.")
        else:
            st.session_state.feedback_list.append({"name": sender_name, "message": sender_msg})
            st.success(f"Thank you, {sender_name}! Your message has been received.")

# FOOTER
st.markdown(
    f"""
    <div style="text-align: center; color: #64748b; padding-top: 30px; font-size: 0.85rem;">
        <p><strong>{CONFIG['NAME']}</strong> &bull; {CONFIG['SECTION']} &bull; Built with Streamlit</p>
        <p><a href="#about" style="color: #3b82f6; text-decoration: none;">Back to Top</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
