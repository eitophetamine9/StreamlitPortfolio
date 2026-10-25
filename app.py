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
        "Growing up I've always been exposed to technology, more specifically a PC, "
        " that inspired me to delve deeper into technology on how it works and what I could build with it."
        " I may not be the sharpest tool in the shed, but I am able to adapt to changes granted I put effort it."
    ),
    "EDUCATION": [
        {"level": "College", "school": "Cebu Institute of Technology - University", "period": "2024 - Present", "details": "BS Computer Science"},
        {"level": "Senior High", "school": "University of Cebu - METC", "period": "2021 - 2024", "details": "STEM Strand"}
    ],
    "MILESTONES": [
        {"year": "2024-2025", "event": "Parangal Academic Achiever"},
        {"year": "2025", "event": "Finished our first game for capstone - Luck in the Dungeon"},
        {"year": "2026", "event": "First solo game development project - Spirit Contract Evo Idle "},
        {"year": "2026", "event": "Game Gauntlet - Sim Jam Participant"},
    ],

    # ── Hobbies ──
    "HOBBIES": [
        {"name": "Gaming", "desc": "Playing indie and triple A games alike, enjoying the storyline along the way. Comfort hobby"},
        {"name": "Story Writing", "desc": "Composing stories for both my future game development career and personal interests."},
        {"name": "Game Development", "desc": "Developing 2D (soon 3D) games using a variety of different engine. Still learning from the ground up"},
        {"name": "Music & Audio", "desc": "Listening to a variety of genres and discovering new artists. Really gets me through rough days"},
        {"name": "Working out", "desc": "Building my physique like they say, a healthy body equals a healthy mind. Another personal favorite hobby of mine."}
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
            "role": "Full-Stack Developer",
            "status": "In Progress",
            "tools": "Python, Django, Supabase, HTML, CSS, JS",
            "outcome": "A community-driven, anonymous accountability platform designed to combat academic burnout and student isolation through shared daily self-care rhythms.",
            "link": "https://github.com/eitophetamine9/AnchorPod"
        },
        {
            "title": "Spirit Contract Evo | Idle",
            "role": "Full-Stack Developer",
            "status": "In Progress",
            "tools": "HTML, JS, Pixi.js, Vite",
            "outcome": "A mobile-first, dark fantasy Idle RPG built with vanilla JavaScript (ES2022+), Pixi.js 2.5D viewports, and reactive state management.",
            "link": "https://github.com/eitophetamine9/SpiritContractEvoIdle"
        },
        {
            "title": "Phlegmatic",
            "role": "Full-Stack Developer",
            "status": "In Progress",
            "tools": "C++, Raylib, CMake",
            "outcome": "A top-down view 2D RPG built in C++ and Raylib.",
            "link": "https://github.com/eitophetamine9/Phlegmatic"
        },
        {
            "title": "Luck in the Dungeon",
            "role": "Lead Developer",
            "status": "Completed",
            "tools": "Java, Java Swing",
            "outcome": "A Java-based puzzle game with gacha / rng elements involved needed for progression.",
            "link": "https://github.com/eitophetamine9/Luck-in-the-Dungeon"
        },
        {
            "title": "CyberType",
            "role": "Lead Developer",
            "status": "Completed",
            "tools": "C#, Blazor WebApp, TailwindCSS",
            "outcome": "A browser-based, run-based survival typing game built with Blazor WebAssembly (.NET 10), pure C# game loops, and Tailwind CSS v4 styling.",
            "link": "https://github.com/eitophetamine9/MidtermAppDev"
        }
    ],

    # ── Certificates ──
    "CERTIFICATES": [
        {
            "title": "Certificate of Achievement",
            "issuer": "Platform / Organization",
            "date": "2024",
            "image": "assets/cert1.png",  # Save image in assets/
            "description": "Description of the certificate, course, or competition honor."
        },
        {
            "title": "Cybersecurity / Course Credential",
            "issuer": "Issuing Body",
            "date": "2025",
            "image": "assets/cert2.png",  # Save image in assets/
            "description": "Details about completed training, coursework, or hands-on labs."
        },
        {
            "title": "Programming & Development Certificate",
            "issuer": "Platform / University",
            "date": "2025",
            "image": "assets/cert3.png",  # Save image in assets/
            "description": "Demonstrated technical skills in software engineering and development."
        },
        {
            "title": "Specialized Workshop / Hackathon Honor",
            "issuer": "Event Organizer / Institution",
            "date": "2026",
            "image": "assets/cert4.png",  # Save image in assets/
            "description": "Recognition for participation, innovation, or excellence."
        }
    ]
}

# STREAMLIT APP CONFIG & SMOOTH SCROLLING

st.set_page_config(
    page_title=f"{CONFIG['NAME']} | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Smooth scrolling animation & clean styling
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

/* Hide sidebar completely */
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}
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

/* Streamlit Button & Component Consistency */
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

# Session state initialization for feedback form
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []


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
    m1, m2 = st.columns(2)
    m1.metric("Projects", len(CONFIG["PROJECTS"]))
    m2.metric("Status", "Active Student")

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

# 2x2 grid layout with uniform box heights
displayed_projects = CONFIG["PROJECTS"]
if proj_view == "Featured Only":
    featured = [p for p in CONFIG["PROJECTS"] if p.get("status") == "Completed" or "AnchorPod" in p.get("title", "")]
    if featured:
        displayed_projects = featured

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

st.divider()

# CERTIFICATES
st.markdown('<div id="certificates" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("Certificates & Achievements")
st.write("Accredited certifications, workshop completions, and academic credentials.")

for row_idx in range(0, len(CONFIG["CERTIFICATES"]), 2):
    row_certs = CONFIG["CERTIFICATES"][row_idx:row_idx + 2]
    cols = st.columns(2)
    for col_idx, cert in enumerate(row_certs):
        with cols[col_idx]:
            with st.container(border=True):
                img_path = cert.get("image", "")
                if os.path.exists(img_path):
                    st.image(img_path, caption=cert["title"], use_container_width=True)
                else:
                    # Elegant placeholder indicating where to place the image
                    st.markdown(
                        f"""
                        <div style="background: rgba(30, 41, 59, 0.4); border: 2px dashed rgba(59, 130, 246, 0.35); border-radius: 10px; padding: 40px 15px; text-align: center; margin-bottom: 12px;">
                            <p style="color: #93c5fd; font-weight: 600; margin: 0 0 6px 0;">Certificate Image Stand-in</p>
                            <p style="color: #64748b; font-size: 0.8rem; margin: 0;">Save image to <code>{img_path}</code></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                st.subheader(cert["title"])
                st.markdown(f"**Issuer:** `{cert['issuer']}` | **Date:** `{cert['date']}`")
                st.caption(cert["description"])

st.divider()

# GITHUB & CONTRIBUTION CHARTS
st.markdown('<div id="github" class="section-anchor"></div>', unsafe_allow_html=True)

gh_head_col, gh_btn_col = st.columns([3, 1])
with gh_head_col:
    st.header("GitHub Contributions")
    st.caption(f"Live activity and commit heatmap for **[@{CONFIG['GITHUB_USERNAME']}]({CONFIG['GITHUB_URL']})**")
with gh_btn_col:
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    st.link_button("Open GitHub Profile", CONFIG["GITHUB_URL"], use_container_width=True)

# Real live GitHub contribution heatmap
chart_url = f"https://ghchart.rshah.org/40c463/{CONFIG['GITHUB_USERNAME']}"
st.markdown(
    f"""
    <div class="gh-container">
        <a href="{CONFIG['GITHUB_URL']}" target="_blank" title="Click to view @{CONFIG['GITHUB_USERNAME']} on GitHub" style="text-decoration: none;">
            <img src="{chart_url}" alt="GitHub Contribution Chart for {CONFIG['GITHUB_USERNAME']}" class="gh-chart-img" />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# CONTACT & FEEDBACK FORM
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)

# Centered compact card layout
c_left, c_center, c_right = st.columns([1, 2.2, 1])

with c_center:
    with st.container(border=True):
        st.subheader("Contact & Feedback")
        st.caption("Leave feedback or send a message. This form responds immediately upon submission.")
        
        with st.form("contact_form", clear_on_submit=True):
            n_col, e_col = st.columns(2)
            with n_col:
                sender_name = st.text_input("Name *", placeholder="Your Name")
            with e_col:
                sender_email = st.text_input("Email *", placeholder="you@email.com")
            
            sender_msg = st.text_area("Message *", placeholder="Write your message here...", height=110)
            btn_submit = st.form_submit_button("Send Message", use_container_width=True)
            
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
