# 🚀 CSIT 349: Autobiography and Portfolio App

An interactive, responsive personal portfolio and autobiography web application built with **Streamlit**. Designed according to the **CSIT 349 - Applied AI** course rubric for full marks and the **+10 Option B bonus points**.

---

## 🌟 Key Features & Rubric Checklist

- **About You**: Full name, program, section, contact details, short biography, and profile photo stand-in.
- **Autobiography**: Deep dive into your personal story, academic credentials, and interactive career milestones timeline using `st.tabs`.
- **Skills Matrix & Analytics**: Interactive domain filter (`st.selectbox`), proficiency bar chart (`st.bar_chart`) with numeric values, and toggleable raw data table (`st.checkbox` + `st.dataframe`).
- **Projects Showcase**: 4 projects with role, technology stack tags, summary, outcome, and repository link, filterable by tech (`st.multiselect`) and complexity (`st.slider`).
- **GitHub Integration**: Direct GitHub link, live GitHub contribution graph heatmap (`ghchart.rshah.org`), and interactive GitHub username switcher in the sidebar.
- **Hobbies & Interests**: Dedicated cards displaying personal hobbies, categories, and descriptions.
- **Interactive Feedback Form**: Functional contact form (`st.form` & `st.form_submit_button`) with immediate response, feedback session logging (`st.session_state`), and celebratory animations (`st.balloons`).
- **Smooth Scrolling Animation**: Glassmorphic sticky top navigation bar with anchor tags and CSS `scroll-behavior: smooth` for fluid navigation.
- **Bonus Extras Included**: Downloadable resume button (`st.download_button`), metrics (`st.metric`), custom theme styles, expanders, and session state.

---

## ⚙️ How to Personalize Your Details

All personal information is cleanly organized in a single configuration block at the very top of [`app.py`](app.py):

1. Open [`app.py`](app.py).
2. Locate the **`PORTFOLIO_CONFIG`** dictionary near line 14.
3. Edit the following fields with your personal details:
   - `NAME`: Your full name.
   - `COURSE_SECTION`: Your course section (e.g., `CSIT 349 - Section 3A`).
   - `PROGRAM_YEAR`: Your degree program and year level.
   - `GITHUB_USERNAME`: Your GitHub username (this automatically renders your real contribution chart!).
   - `SHORT_BIO`: Your personal summary.
   - `AUTOBIOGRAPHY`: Your journey, education history, and milestones.
   - `SKILLS`: Your technical skills with numeric proficiencies (0-100).
   - `PROJECTS`: Your own titles, roles, tools, and outcomes.
   - `HOBBIES`: Your personal hobbies, icons, and descriptions.

---

## 💻 Running the App Locally

Ensure you have Python 3.10+ installed:

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```
*(If `streamlit` command is not in your system PATH, run `python -m streamlit run app.py`)*

Then open your browser at `http://localhost:8501`.

---

## 🌐 Option B (Bonus +10 Points): Deploy to Streamlit Community Cloud

To earn the bonus points, deploy your app to Streamlit Community Cloud so it opens publicly even when your computer is off:

### Step 1: Initialize Git and Commit
```bash
git init
git add .
git commit -m "feat: complete autobiography and portfolio app"
```

### Step 2: Push to a Public GitHub Repository
1. Go to [GitHub](https://github.com/new) and create a new **public** repository (e.g. `streamlit-portfolio`).
2. Run the commands shown by GitHub to push your local repository:
   ```bash
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/streamlit-portfolio.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy to Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
2. Click **"New app"** (or **"Deploy an app"**).
3. Select your repository: `<YOUR_GITHUB_USERNAME>/streamlit-portfolio`.
4. Set Main file path: `app.py`.
5. Click **"Deploy"**.
6. Once deployed, copy your public `.streamlit.app` URL and submit it!
