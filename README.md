# 🚀 John Erick I. Santizo — Autobiography & Portfolio App

An interactive, responsive personal portfolio and autobiography web application built with **Streamlit**.  
Developed for **CSIT 349 - Applied AI (Section F1)** adhering to all rubric criteria and configured for **Option B (+10 Bonus Points)** deployment on Streamlit Community Cloud.

---

## 👨‍💻 Student Information
- **Name:** John Erick I. Santizo
- **Course & Section:** CSIT 349 - F1
- **Program & Year:** BS Computer Science, 3rd Year
- **Institution:** Cebu Institute of Technology - University
- **GitHub:** [@eitophetamine9](https://github.com/eitophetamine9)
- **Role Focus:** Aspiring Cybersecurity Analyst, Full-Stack Developer, Game Developer

---

## 🌟 Rubric & Features Overview

| Requirement | Implementation Details |
| :--- | :--- |
| **About You** | Profile photo (`assets/profile.png`), program & year, section badge, and personal bio. |
| **Autobiography** | Interactive `st.tabs` covering personal journey, academic history, milestones, and personal hobbies. |
| **Skills Matrix** | Technical proficiency chart (`st.bar_chart`), category filter (`st.selectbox`), proficiency slider (`st.slider`), and toggleable table (`st.dataframe`). |
| **Featured Projects** | 2x2 grid layout showcasing 5 projects with roles, tools, descriptions, and repository links. |
| **Certificates** | 2x2 showcase displaying 4 accredited certifications (C, Java, PSITE, OWASP) with images. |
| **GitHub Integration** | Direct profile link + full-width live commit activity heatmap (`ghchart.rshah.org`). |
| **Feedback Form** | Centered compact `st.form` storing feedback dynamically with `st.session_state`. |
| **Sidebar & Layout** | Subtle sidebar with quick navigation and full-width multi-column layouts (`st.columns`). |
| **Aesthetics** | Smooth-scrolling sticky navbar, dark slate theme, and **Plus Jakarta Sans** typography. |

---

## 📂 Project Architecture

The codebase has been refactored into a modular, clean component architecture:

```
StreamlitPortfolio/
├── app.py                     # Main application entry point orchestrating all components
├── config.py                  # Centralized data store (biography, skills, projects, certs)
├── styles.py                  # Custom CSS (Google Fonts, dark theme, sticky navbar, cards)
├── components/
│   ├── __init__.py
│   ├── sidebar.py             # Subtle sidebar component (rubric compliance)
│   ├── hero.py                # Hero section with avatar, info, and metrics
│   ├── autobiography.py       # Autobiography, education, milestones, & hobbies tabs
│   ├── skills.py              # Interactive skill analytics (chart + table)
│   ├── projects.py            # Featured projects 2x2 grid
│   ├── certificates.py        # 2x2 certificates grid
│   ├── github_section.py      # GitHub profile link and live commit heatmap
│   └── contact.py             # Centered, compact feedback form
├── assets/
│   ├── profile.png            # Profile photo
│   ├── cert1.png              # OWASP Cybersecurity APEX 2026
│   ├── cert2.png              # Java Certification (CodeChum)
│   ├── cert3.png              # C Certification (CodeChum)
│   └── cert4.png              # PSITE Student Congress 2026
├── requirements.txt           # Python dependencies for Streamlit Community Cloud
└── README.md                  # Documentation and deployment guide
```

---

## 💻 Running the App Locally

Ensure Python 3.10+ is installed:

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the Streamlit application
streamlit run app.py
```
*(If `streamlit` command is not in your system PATH, run `python -m streamlit run app.py`)*

Open **`http://localhost:8501`** in your browser.

---

## ☁️ Option B (Bonus +10 Points): Deploy to Streamlit Community Cloud

Follow these steps to deploy your repository publicly:

### Step 1: Create a Public GitHub Repository
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g. `StreamlitPortfolio`).
3. Make sure it is set to **Public** and leave "Initialize this repository with a README" unchecked.

### Step 2: Push Your Local Code to GitHub
Open PowerShell in this project folder and run:

```powershell
git remote add origin https://github.com/eitophetamine9/<YOUR_REPO_NAME>.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
2. Click **"New app"** (or **"Deploy an app"**).
3. Select your repository: `eitophetamine9/<YOUR_REPO_NAME>`.
4. Ensure **Main file path** is set to: `app.py`.
5. Click **"Deploy"**.
6. Once built, copy your live public URL (e.g. `https://<YOUR_APP>.streamlit.app`) and submit it to get the **+10 bonus points**!
