# 🎾 Pickleball Tournament Manager

A full-stack web application for organizing and managing round-robin pickleball
tournaments. Players can register, matches are auto-scheduled, and scores are submitted
directly to update standings in real-time. Built to solve a real-world workflow with a
modern React + Django stack.

---

## 📊 Status

[![codecov](https://codecov.io/github/phillip-l-rogers/pickleball/graph/badge.svg?token=W7RNQ8UJZ6)](https://codecov.io/github/phillip-l-rogers/pickleball)
[![pylint](https://img.shields.io/badge/PyLint-5.28-orange?logo=python&logoColor=white)

---

## 🚀 Features

- Create and configure tournaments with flexible settings
- Player self-registration or admin assignment
- Auto-generate round-robin match schedules
- Score submission by players or organizers
- Live leaderboard updates and standings
- Authentication and permission controls
- Clean, responsive UI built with Tailwind and React
- RESTful API powered by Django REST Framework

---

## 📸 Screenshots

<p float="left">
  <img src="screenshots/create_tournament.png" height="300"/>
  <img src="screenshots/match_schedule.png" height="300"/>
  <img src="screenshots/submit_scores.png" height="300"/>
  <img src="screenshots/standings.png" height="300"/>
</p>

---

## 🛠️ Tech Stack

- **Frontend:** React, Tailwind CSS, Vite
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (dev), PostgreSQL (prod)
- **Auth:** Django sessions, custom permissions
- **Deployment:** Render

---

## ▶️ Live Demo

- 🌐 Live site: *(coming soon)*
- 💻 GitHub repo: [github.com/phillip-l-rogers/pickleball](https://github.com/phillip-l-rogers/pickleball)

---

## 📦 Getting Started

### Backend (Django)

```bash
# Clone and set up virtual environment
git clone https://github.com/phillip-l-rogers/pickleball.git
cd pickleball-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install and run
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend (React)

```bash
cd ../pickleball-frontend
npm install
npm run dev
```

Visit http://localhost:5173/ to run locally.

---

## 🧪 Tips for Testing

- Log in or register to create tournaments
- Add players and simulate match results
- Use multiple users to test score entry
- Try running a full tournament start-to-finish

---

## 📁 Folder Structure

```bash
pickleball/
├── pickleball-backend/     # Django + DRF
│   ├── manage.py
│   ├── api/                # Tournament logic
│   └── requirements.txt
├── pickleball-frontend/    # React app
│   ├── src/
│   └── package.json
```

---

## ✨ Motivation
This project was built to bring structure and automation to informal pickleball 
tournaments. It reflects my strengths in backend architecture, API design, and building
user-focused tools — and it’s a great example of applying full-stack skills to solve
real-world problems.

---

## 📬 Contact

- 📧 Email: phillip.l.rogers.29@gmail.com
- 💼 LinkedIn: https://linkedin.com/in/phillip-rogers-b76329365
