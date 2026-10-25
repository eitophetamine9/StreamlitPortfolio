# ==============================================================================
# PORTFOLIO CONFIGURATION & DATA STORE
# ==============================================================================

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
        "that inspired me to delve deeper into technology on how it works and what I could build with it. "
        "I may not be the sharpest tool in the shed, but I am able to adapt to changes granted I put effort in."
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
            "title": "C Certification",
            "issuer": "CodeChum",
            "date": "2025",
            "image": "assets/cert3.png",  
            "description": "Award."
        },
        {
            "title": "Java Certification",
            "issuer": "CodeChum",
            "date": "2025",
            "image": "assets/cert2.png", 
            "description": "Award."
        },
        {
            "title": "PSITE - Cebu ICT Student Congress 2026",
            "issuer": "PSIT Central Visayas",
            "date": "2026",
            "image": "assets/cert4.png",  
            "description": "Participant."
        },
        {
            "title": "OWASP - Cybersecurity APEX 2026",
            "issuer": "OWASP",
            "date": "2026",
            "image": "assets/cert1.png",  
            "description": "Participant."
        }
    ]
}
