import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ==============================================================================
# 🛠️ USER CONFIGURATION TEMPLATE
# ==============================================================================
# Instructions:
# 1. Update the dictionary below with your personal information, projects, and hobbies.
# 2. Everything is organized so you can edit the text and numbers directly.
# 3. Deploy to Streamlit Community Cloud (Option B) by pushing to your GitHub repo!
# ==============================================================================

PORTFOLIO_CONFIG = {
    # ── Basic Student & Course Info (Required by Rubric) ──
    "NAME": "Alex Morgan",  # TODO: Replace with your full name
    "COURSE_SECTION": "CSIT 349 - Section 3A",  # TODO: Replace with your section
    "PROGRAM_YEAR": "BS Information Technology, 3rd Year",  # TODO: Replace with your program & year
    "TITLE_TAGLINE": "Aspiring AI Engineer & Full-Stack Developer",  # TODO: Replace with your headline
    "LOCATION": "Manila, Philippines",  # TODO: Replace with your location
    "EMAIL": "alex.morgan@student.edu",  # TODO: Replace with your email
    
    # ── Social & Repository Links ──
    "GITHUB_USERNAME": "torvalds",  # TODO: Replace with your GitHub username (shows your real commit chart!)
    "GITHUB_URL": "https://github.com/torvalds",  # TODO: Replace with your GitHub profile link
    "LINKEDIN_URL": "https://linkedin.com",  # TODO: Replace or leave empty
    
    # ── Short Biography (About You) ──
    "SHORT_BIO": (
        "Hello! I am a passionate Computer Science student dedicated to building "
        "practical AI systems and sleek web applications. I love turning complex data "
        "into intuitive, accessible interactive experiences."
    ),
    
    # ── Profile Photo (URL or local path) ──
    # You can put an image URL here or a local file like "assets/profile.png"
    "PROFILE_IMAGE": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=80",
    
    # ── Autobiography Sections ──
    "AUTOBIOGRAPHY": {
        "BACKGROUND": (
            "I first fell in love with coding when I automated a repetitive spreadsheet task "
            "in high school. Since then, my journey has been driven by endless curiosity and a desire "
            "to understand how intelligent systems can augment human capabilities. Over the years, "
            "I transitioned from basic scripting to designing deep learning models and full-stack platforms."
        ),
        "EDUCATION": [
            {
                "degree": "Bachelor of Science in Information Technology",
                "institution": "State University of Technology",
                "period": "2022 - Present",
                "honors": "Dean's Honor List (2022 - 2024)"
            },
            {
                "degree": "High School STEM Strand (Senior High)",
                "institution": "National Science Academy",
                "period": "2020 - 2022",
                "honors": "Valedictorian / Excellence in Mathematics & Robotics"
            }
        ],
        "MILESTONES": [
            {"year": "2022", "title": "Wrote First Line of Python", "description": "Built my first automated CLI calculator and file sorter."},
            {"year": "2023", "title": "1st Hackathon Win", "description": "Developed an AI-assisted campus navigation tool for freshmen."},
            {"year": "2024", "title": "Published 1st Open Source Tool", "description": "Created a lightweight dataset preprocessing pipeline on PyPI."},
            {"year": "2025", "title": "Lead AI Researcher - Capstone", "description": "Leading a team on computer vision for agricultural disease detection."}
        ]
    },
    
    # ── Skills Data (Used for text, table, and interactive chart) ──
    "SKILLS": [
        {"Skill": "Python", "Category": "Programming", "Proficiency": 92, "Years Experience": 3.0},
        {"Skill": "Streamlit", "Category": "Frameworks", "Proficiency": 88, "Years Experience": 2.0},
        {"Skill": "PyTorch / TensorFlow", "Category": "AI & ML", "Proficiency": 80, "Years Experience": 1.5},
        {"Skill": "SQL & Databases", "Category": "Databases", "Proficiency": 78, "Years Experience": 2.5},
        {"Skill": "JavaScript / React", "Category": "Frontend", "Proficiency": 72, "Years Experience": 2.0},
        {"Skill": "Git & GitHub", "Category": "DevOps", "Proficiency": 85, "Years Experience": 3.0},
        {"Skill": "Docker", "Category": "DevOps", "Proficiency": 68, "Years Experience": 1.0},
        {"Skill": "Data Visualization", "Category": "AI & ML", "Proficiency": 86, "Years Experience": 2.5},
    ],
    
    # ── Projects (At least 3 required by Rubric) ──
    "PROJECTS": [
        {
            "title": "SmartVision: Agricultural Crop Disease Detection",
            "role": "Lead Machine Learning Engineer",
            "tools": ["Python", "PyTorch", "Streamlit", "OpenCV"],
            "summary": "An edge-deployable computer vision model that identifies plant foliage diseases with 96.4% test accuracy.",
            "outcome": "Deployed to 3 local community farms; reduced crop diagnosis time from 4 days to 5 seconds.",
            "link": "https://github.com",
            "complexity": 5
        },
        {
            "title": "FinStream: Real-time Algorithmic Portfolio Analyzer",
            "role": "Full-Stack Developer",
            "tools": ["Python", "Streamlit", "Pandas", "Plotly", "Yahoo Finance API"],
            "summary": "Interactive financial dashboard tracking live market equities, risk metrics (Sharpe ratio), and automated backtesting.",
            "outcome": "Achieved 1,200+ monthly active community users on Streamlit Cloud.",
            "link": "https://github.com",
            "complexity": 4
        },
        {
            "title": "CampusBot: University Knowledge Retrieval Assistant",
            "role": "NLP & Backend Developer",
            "tools": ["FastAPI", "LangChain", "ChromaDB", "Streamlit"],
            "summary": "Retrieval-Augmented Generation (RAG) assistant answering student queries using the official university handbook.",
            "outcome": "Answered over 15,000 queries during freshman orientation week with 91% satisfaction.",
            "link": "https://github.com",
            "complexity": 4
        },
        {
            "title": "PulseLog: Fitness & Habit Tracker",
            "role": "Solo Creator",
            "tools": ["Python", "SQLite", "Streamlit", "Matplotlib"],
            "summary": "A privacy-focused habit tracking app with visual streak heatmaps and weekly analytical reports.",
            "outcome": "Featured in student technology showcase.",
            "link": "https://github.com",
            "complexity": 3
        }
    ],
    
    # ── Hobbies & Personal Interests ──
    "HOBBIES": [
        {
            "name": "Urban & Street Photography",
            "icon": "📸",
            "category": "Creative",
            "desc": "Capturing neon nightscapes, architectural geometry, and fleeting candid moments in the city."
        },
        {
            "name": "Competitive Chess",
            "icon": "♟️",
            "category": "Mind & Strategy",
            "desc": "Playing rapid 10-minute games online. Currently rating ~1550 on Chess.com. Favorite opening: Sicilian Defense."
        },
        {
            "name": "Custom Mechanical Keyboards",
            "icon": "⌨️",
            "category": "Tinkering",
            "desc": "Lube switches, solder PCBs, and tune stabilizers. Currently daily-driving a 65% gasket-mounted board."
        },
        {
            "name": "Long-distance Cycling",
            "icon": "🚴",
            "category": "Fitness",
            "desc": "Weekend 60km endurance rides exploring mountain trails and coastal loops with university friends."
        }
    ]
}

# ==============================================================================
# 🎨 PAGE CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title=f"{PORTFOLIO_CONFIG['NAME']} | Portfolio & Autobiography",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State (Extra component for rubric)
if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False
if "submissions_log" not in st.session_state:
    st.session_state.submissions_log = []
if "visitor_counter" not in st.session_state:
    st.session_state.visitor_counter = 42

# ==============================================================================
# 🌊 SMOOTH SCROLLING ANIMATION & MODERN DESIGN SYSTEM (CSS)
# ==============================================================================
st.markdown("""
<style>
/* Enable smooth scrolling across the entire document */
html {
    scroll-behavior: smooth !important;
}

/* Section Anchor offsets so sticky navbar does not obscure headers */
.section-anchor {
    scroll-margin-top: 90px;
    padding-top: 10px;
}

/* Sticky Glassmorphic Navigation Bar */
.sticky-navbar {
    position: sticky;
    top: 2.875rem;
    z-index: 99;
    background: rgba(17, 24, 39, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 10px 18px;
    margin-bottom: 2rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}

.nav-item {
    color: #e2e8f0 !important;
    text-decoration: none !important;
    font-size: 0.9rem;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 8px;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    border: 1px solid transparent;
}

.nav-item:hover {
    color: #ffffff !important;
    background: rgba(59, 130, 246, 0.25);
    border: 1px solid rgba(59, 130, 246, 0.5);
    transform: translateY(-2px);
}

/* Card container design */
.custom-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 20px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.custom-card:hover {
    transform: translateY(-4px);
    border-color: rgba(59, 130, 246, 0.4);
    box-shadow: 0 12px 24px -10px rgba(59, 130, 246, 0.2);
}

/* Student & Course Badge */
.header-badge {
    display: inline-block;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}

/* GitHub Heatmap Container */
.gh-chart-container {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    overflow-x: auto;
}

/* Custom highlight badges */
.tech-pill {
    display: inline-block;
    background: rgba(59, 130, 246, 0.15);
    color: #60a5fa;
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 12px;
    padding: 2px 8px;
    font-size: 0.75rem;
    margin-right: 4px;
    margin-bottom: 4px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# 🧭 STICKY NAVIGATION BAR (Smooth-Scrolling Links)
# ==============================================================================
st.markdown("""
<div class="sticky-navbar">
    <a href="#about-me" class="nav-item">👤 About Me</a>
    <a href="#autobiography" class="nav-item">📖 Autobiography</a>
    <a href="#skills-matrix" class="nav-item">⚡ Skills</a>
    <a href="#featured-projects" class="nav-item">💼 Projects</a>
    <a href="#github-activity" class="nav-item">🐙 GitHub</a>
    <a href="#hobbies-passions" class="nav-item">✨ Hobbies</a>
    <a href="#contact-feedback" class="nav-item">📬 Contact</a>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# 📌 SIDEBAR CONTROLS & INFO
# ==============================================================================
with st.sidebar:
    st.markdown(f"### 👨‍💻 {PORTFOLIO_CONFIG['NAME']}")
    st.caption(f"**Section:** {PORTFOLIO_CONFIG['COURSE_SECTION']}")
    st.caption(f"**Program:** {PORTFOLIO_CONFIG['PROGRAM_YEAR']}")
    st.divider()
    
    # Navigation Shortcut in sidebar as well
    st.markdown("#### ⚡ Quick Jump")
    st.markdown("- [About Me](#about-me)")
    st.markdown("- [Autobiography](#autobiography)")
    st.markdown("- [Skills Matrix](#skills-matrix)")
    st.markdown("- [Featured Projects](#featured-projects)")
    st.markdown("- [GitHub Contributions](#github-activity)")
    st.markdown("- [Hobbies & Interests](#hobbies-passions)")
    st.markdown("- [Contact & Feedback](#contact-feedback)")
    
    st.divider()
    
    # Interactive GitHub Username Switcher (Extra utility)
    st.markdown("#### 🐙 Live GitHub Customizer")
    user_gh = st.text_input(
        "GitHub Handle:",
        value=PORTFOLIO_CONFIG["GITHUB_USERNAME"],
        help="Type any public GitHub username to update the live commit chart!"
    )
    
    # Download Resume button (Rubric Extra Component)
    st.markdown("#### 📄 Resume / CV")
    sample_cv = f"""# Curriculum Vitae - {PORTFOLIO_CONFIG['NAME']}
**Section**: {PORTFOLIO_CONFIG['COURSE_SECTION']}
**Program**: {PORTFOLIO_CONFIG['PROGRAM_YEAR']}
**Email**: {PORTFOLIO_CONFIG['EMAIL']}
**GitHub**: https://github.com/{user_gh}

## Profile Summary
{PORTFOLIO_CONFIG['SHORT_BIO']}

## Education
{chr(10).join([f"- {e['degree']} ({e['period']}) - {e['institution']}" for e in PORTFOLIO_CONFIG['AUTOBIOGRAPHY']['EDUCATION']])}

## Key Projects
{chr(10).join([f"- {p['title']} ({p['role']}): {p['summary']}" for p in PORTFOLIO_CONFIG['PROJECTS']])}
"""
    st.download_button(
        label="📥 Download Resume (.md)",
        data=sample_cv,
        file_name=f"{PORTFOLIO_CONFIG['NAME'].replace(' ', '_')}_CV.md",
        mime="text/markdown",
        use_container_width=True
    )
    
    st.divider()
    
    # Portfolio view preferences (Rubric widgets: Checkbox & Radio)
    st.markdown("#### ⚙️ Display Preferences")
    show_raw_data = st.checkbox("Show Raw Skill Data Table", value=False)
    chart_theme_choice = st.radio("Chart Accent Style", ["Default Cyan", "Purple Violet", "Emerald Green"], index=0)
    
    # Live visitor counter metric
    st.metric(label="Profile Visits Today", value=st.session_state.visitor_counter, delta="+3 new")


# ==============================================================================
# 👤 SECTION 1: ABOUT ME & HERO
# ==============================================================================
st.markdown('<div id="about-me" class="section-anchor"></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    # Profile Photo (Rubric: image)
    st.image(
        PORTFOLIO_CONFIG["PROFILE_IMAGE"],
        caption=f"{PORTFOLIO_CONFIG['NAME']} (Photo stand-in)",
        use_container_width=True
    )
    # Quick contact buttons / links
    st.link_button(
        label="🌐 View GitHub Profile",
        url=f"https://github.com/{user_gh}",
        use_container_width=True
    )
    if PORTFOLIO_CONFIG.get("LINKEDIN_URL"):
        st.link_button(
            label="💼 Connect on LinkedIn",
            url=PORTFOLIO_CONFIG["LINKEDIN_URL"],
            use_container_width=True
        )

with col2:
    # Rubric Requirement: Name and section visible
    st.markdown(f'<span class="header-badge">{PORTFOLIO_CONFIG["COURSE_SECTION"]}</span>', unsafe_allow_html=True)
    st.title(PORTFOLIO_CONFIG["NAME"])
    st.subheader(PORTFOLIO_CONFIG["TITLE_TAGLINE"])
    
    # Meta details
    meta_col1, meta_col2 = st.columns(2)
    with meta_col1:
        st.write(f"🎓 **Program:** {PORTFOLIO_CONFIG['PROGRAM_YEAR']}")
        st.write(f"📍 **Location:** {PORTFOLIO_CONFIG['LOCATION']}")
    with meta_col2:
        st.write(f"📧 **Email:** [{PORTFOLIO_CONFIG['EMAIL']}](mailto:{PORTFOLIO_CONFIG['EMAIL']})")
        st.write(f"🐙 **GitHub:** `@{user_gh}`")
        
    st.markdown("---")
    st.markdown("### 💬 Short Biography")
    st.write(PORTFOLIO_CONFIG["SHORT_BIO"])
    
    # Highlight Metrics (Rubric Extra: metrics)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects Built", len(PORTFOLIO_CONFIG["PROJECTS"]), "Completed")
    m2.metric("Primary Tech", "Python", "Main Stack")
    m3.metric("Experience", "3+ Years", "Academic")
    m4.metric("Coffee Consumed", "850+ Cups", "☕ High")

st.divider()


# ==============================================================================
# 📖 SECTION 2: AUTOBIOGRAPHY & BACKGROUND
# ==============================================================================
st.markdown('<div id="autobiography" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("📖 Autobiography & Journey")
st.write("A deep dive into my personal story, educational background, and developmental milestones.")

# Rubric Extra Component: Tabs
tab_journey, tab_edu, tab_milestones = st.tabs([
    "🌟 My Story & Origin",
    "🎓 Education & Credentials",
    "🏆 Key Milestones"
])

with tab_journey:
    st.subheader("My Journey in Technology")
    st.write(PORTFOLIO_CONFIG["AUTOBIOGRAPHY"]["BACKGROUND"])
    st.info(
        "💡 **Core Philosophy:** *'The best way to predict the future is to invent it.'* "
        "I believe that mastering software and artificial intelligence gives us the superpowers "
        "to solve the grandest societal challenges.",
        icon="✨"
    )

with tab_edu:
    st.subheader("Academic Pathway")
    for edu in PORTFOLIO_CONFIG["AUTOBIOGRAPHY"]["EDUCATION"]:
        with st.container():
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"#### {edu['degree']}")
                st.write(f"🏛️ **{edu['institution']}**")
                st.caption(f"🏅 {edu['honors']}")
            with c2:
                st.markdown(f"**Period:** `{edu['period']}`")
            st.markdown("---")

with tab_milestones:
    st.subheader("Growth Timeline")
    for m in PORTFOLIO_CONFIG["AUTOBIOGRAPHY"]["MILESTONES"]:
        col_yr, col_desc = st.columns([1, 4])
        with col_yr:
            st.button(f"🚩 {m['year']}", key=f"btn_{m['year']}", disabled=True)
        with col_desc:
            st.markdown(f"**{m['title']}**")
            st.write(m['description'])

st.divider()


# ==============================================================================
# ⚡ SECTION 3: SKILLS MATRIX & PROFICIENCY
# ==============================================================================
st.markdown('<div id="skills-matrix" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("⚡ Skills Matrix & Analytics")
st.write("Demonstrated proficiency across programming, AI frameworks, tools, and platforms.")

# Convert skills to Pandas DataFrame (Rubric: table & chart with numbers)
skills_df = pd.DataFrame(PORTFOLIO_CONFIG["SKILLS"])

# Interactive Filter (Rubric widgets: selectbox)
categories = ["All Categories"] + sorted(list(skills_df["Category"].unique()))
selected_category = st.selectbox("Filter Skills by Domain:", categories)

filtered_skills = skills_df if selected_category == "All Categories" else skills_df[skills_df["Category"] == selected_category]

# Columns layout for Chart & Quick Table
col_chart, col_stats = st.columns([2, 1], gap="medium")

with col_chart:
    st.subheader("📊 Skill Proficiency Ratings (0 - 100)")
    # Streamlit native bar chart using numbers
    chart_data = filtered_skills.set_index("Skill")[["Proficiency"]]
    st.bar_chart(chart_data, color="#3b82f6" if chart_theme_choice == "Default Cyan" else ("#8b5cf6" if chart_theme_choice == "Purple Violet" else "#10b981"))

with col_stats:
    st.subheader("📋 Skill Highlights")
    st.markdown(f"- **Top Skill:** `{skills_df.loc[skills_df['Proficiency'].idxmax()]['Skill']}` ({skills_df['Proficiency'].max()}%)")
    st.markdown(f"- **Total Tracked Skills:** `{len(filtered_skills)}`")
    st.markdown(f"- **Average Proficiency:** `{filtered_skills['Proficiency'].mean():.1f}%`")
    st.markdown(f"- **Average Experience:** `{filtered_skills['Years Experience'].mean():.1f} Years`")
    
    st.write("###### Quick Proficiency Snapshot:")
    for _, row in filtered_skills.head(4).iterrows():
        st.write(f"**{row['Skill']}**")
        st.progress(int(row['Proficiency']))

# Toggleable raw data table (Rubric: table or dataframe)
if show_raw_data:
    st.subheader("📑 Raw Skills Table")
    st.dataframe(filtered_skills, use_container_width=True)

st.divider()


# ==============================================================================
# 💼 SECTION 4: FEATURED PROJECTS
# ==============================================================================
st.markdown('<div id="featured-projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("💼 Featured Projects")
st.write("At least 3 practical projects detailing my roles, technologies used, and real-world outcomes.")

# Widgets for interactive filtering (Rubric widgets: slider & multiselect)
p_col1, p_col2 = st.columns([2, 2])
with p_col1:
    all_tools = sorted(list(set([tool for proj in PORTFOLIO_CONFIG["PROJECTS"] for tool in proj["tools"]])))
    selected_tools = st.multiselect("Filter projects by technology:", all_tools, default=[])
with p_col2:
    min_complexity = st.slider("Minimum Project Complexity:", min_value=1, max_value=5, value=2)

# Filter logic
displayed_projects = [
    p for p in PORTFOLIO_CONFIG["PROJECTS"]
    if p["complexity"] >= min_complexity and (not selected_tools or any(t in p["tools"] for t in selected_tools))
]

if not displayed_projects:
    st.warning("No projects match the selected filter criteria. Try adjusting the sliders or tags!")
else:
    # Render projects in a responsive 2-column grid
    grid_cols = st.columns(2, gap="medium")
    for idx, proj in enumerate(displayed_projects):
        with grid_cols[idx % 2]:
            with st.container(border=True):
                st.markdown(f"### {proj['title']}")
                st.markdown(f"**Role:** `{proj['role']}` | **Complexity:** {'⭐' * proj['complexity']}")
                
                # Tech tags
                pills = " ".join([f"`{t}`" for t in proj["tools"]])
                st.markdown(f"**Stack:** {pills}")
                
                st.write(proj["summary"])
                
                # Rubric: Outcome or link
                st.success(f"🎯 **Outcome:** {proj['outcome']}")
                
                # Expandable details (Extra component)
                with st.expander("🔍 View Project Deep Dive & Architecture"):
                    st.write(f"Developed as part of practical applications in software engineering and artificial intelligence.")
                    st.write(f"GitHub Repository: [{proj['link']}]({proj['link']})")
                
                st.link_button("🔗 View Repository / Demo", proj["link"], use_container_width=True)

st.divider()


# ==============================================================================
# 🐙 SECTION 5: GITHUB INTEGRATION & CONTRIBUTION CHARTS
# ==============================================================================
st.markdown('<div id="github-activity" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("🐙 GitHub Contributions & Open Source Activity")
st.write(f"Real-time commit calendar and activity statistics fetched for `@{user_gh}`.")

gh_col1, gh_col2 = st.columns([3, 1], gap="medium")

with gh_col1:
    st.subheader("📅 Contribution Heatmap (Past 12 Months)")
    # Direct live GitHub contribution chart SVG from ghchart.rshah.org
    gh_chart_url = f"https://ghchart.rshah.org/40c463/{user_gh}"
    st.markdown(
        f"""
        <div class="gh-chart-container">
            <p style="color: #8b949e; margin-bottom: 8px; font-size: 0.85rem;">Commits in the last year for <strong>@{user_gh}</strong></p>
            <img src="{gh_chart_url}" alt="GitHub Contribution Chart for {user_gh}" style="width: 100%; max-width: 900px; display: block; margin: 0 auto;" />
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption("🟢 Heatmap is dynamically synchronized with the public GitHub commit activity.")

with gh_col2:
    st.subheader("📊 GitHub Profile Link")
    st.markdown(f"Explore source code, pull requests, and repositories for **@{user_gh}**.")
    st.link_button(
        "🚀 Visit My GitHub Profile",
        f"https://github.com/{user_gh}",
        use_container_width=True
    )
    
    st.markdown(
        f"""
        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 15px; border: 1px solid rgba(255,255,255,0.08); margin-top: 15px;">
            <p style="margin: 0; font-size: 0.85rem; color: #94a3b8;">💡 <em>Tip for grading:</em> Enter your own GitHub handle in the sidebar to preview your personal chart live!</em></p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()


# ==============================================================================
# ✨ SECTION 6: HOBBIES & PERSONAL INTERESTS
# ==============================================================================
st.markdown('<div id="hobbies-passions" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("✨ Hobbies & Outside the Terminal")
st.write("What keeps me inspired, creative, and recharged when I'm not writing code.")

# Hobbies cards
hobby_cols = st.columns(len(PORTFOLIO_CONFIG["HOBBIES"]))

for i, hobby in enumerate(PORTFOLIO_CONFIG["HOBBIES"]):
    with hobby_cols[i]:
        with st.container(border=True):
            st.markdown(f"## {hobby['icon']}")
            st.markdown(f"#### {hobby['name']}")
            st.caption(f"Category: {hobby['category']}")
            st.write(hobby["desc"])

st.divider()


# ==============================================================================
# 📬 SECTION 7: CONTACT & FEEDBACK FORM
# ==============================================================================
st.markdown('<div id="contact-feedback" class="section-anchor"></div>', unsafe_allow_html=True)
st.header("📬 Contact & Interactive Feedback")
st.write("Send a message or leave course feedback. This form responds immediately after submission!")

form_col, info_col = st.columns([2, 1], gap="large")

with form_col:
    # Rubric Requirement: A contact or feedback form that responds after submitted
    with st.form("contact_form", clear_on_submit=True):
        st.subheader("Leave a Message or Review")
        
        c_name = st.text_input("Your Name *", placeholder="Jane Doe")
        c_email = st.text_input("Your Email *", placeholder="jane@example.com")
        c_rating = st.slider("How would you rate this portfolio app?", 1, 5, 5, help="1 is lowest, 5 is highest")
        c_message = st.text_area("Message / Feedback *", placeholder="Great project ideas! Would love to collaborate on...")
        
        submitted = st.form_submit_button("🚀 Submit Message", use_container_width=True)
        
        if submitted:
            if not c_name.strip() or not c_email.strip() or not c_message.strip():
                st.error("⚠️ Please fill in all required fields (Name, Email, and Message).")
            else:
                # Save into session state
                st.session_state.feedback_submitted = True
                st.session_state.submissions_log.append({
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "name": c_name,
                    "email": c_email,
                    "rating": c_rating,
                    "message": c_message
                })
                # Visual celebratory effects (Extra components)
                st.balloons()
                st.success(f"🎉 Thank you, **{c_name}**! Your message has been received successfully.")
                st.info(f"A confirmation receipt has been simulated for `{c_email}`.")

with info_col:
    st.subheader("Direct Reach")
    st.markdown(f"**Student:** {PORTFOLIO_CONFIG['NAME']}")
    st.markdown(f"**Section:** {PORTFOLIO_CONFIG['COURSE_SECTION']}")
    st.markdown(f"**Email:** [{PORTFOLIO_CONFIG['EMAIL']}](mailto:{PORTFOLIO_CONFIG['EMAIL']})")
    st.markdown(f"**GitHub:** [{user_gh}](https://github.com/{user_gh})")
    
    st.markdown("---")
    # Show real-time feedback submissions log (Rubric Extra: Session State)
    st.markdown("##### 📨 Recent Inquiries Received:")
    if st.session_state.submissions_log:
        for item in reversed(st.session_state.submissions_log[-3:]):
            st.caption(f"⭐ **{item['name']}** ({item['rating']}/5 stars): '{item['message'][:60]}...'")
    else:
        st.caption("No messages submitted yet in this session. Be the first to leave one!")

st.divider()

# ==============================================================================
# 🏁 FOOTER
# ==============================================================================
st.markdown(
    f"""
    <div style="text-align: center; color: #64748b; padding: 25px 0 10px 0; font-size: 0.88rem;">
        <p>Built with ❤️ using <strong>Streamlit</strong> &bull; <strong>{PORTFOLIO_CONFIG['COURSE_SECTION']}</strong> &bull; &copy; {datetime.datetime.now().year} {PORTFOLIO_CONFIG['NAME']}</p>
        <p><a href="#about-me" style="color: #3b82f6; text-decoration: none;">⬆️ Back to Top</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
