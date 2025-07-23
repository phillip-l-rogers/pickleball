# 🎾 Pickleball Tournament Manager

**Built for [CS50’s Web Programming with Python and JavaScript (CS50W)](https://cs50.harvard.edu/web/).**  
A full-stack web app for creating and managing round-robin pickleball tournaments. 
Features include player registration, automatic match scheduling, score submissions, 
and dynamic standings.

---

## 🚀 Features

- Create round-robin tournaments with customizable settings
- Player self-registration or admin invitations
- Automatically generate match schedules based on number of players
- Record and update match scores
- Live leaderboard and standings based on wins/losses
- Admin dashboard to manage tournaments and participants
- RESTful API backend built with Django REST Framework
- React-based frontend with responsive UI

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

- **Frontend:** React, Tailwind CSS
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (dev), PostgreSQL (prod)
- **API:** RESTful architecture
- **Auth:** Django authentication, token/session-based

---

## ▶️ Live Demo

- 🌐 Live site: *(coming soon)*
- 📺 Video demo: *(coming soon)*

---

## 🧪 Testing Tips

- Register as a new user and create a tournament
- Add yourself and others as players
- Start the tournament to generate the match schedule
- Submit scores to update standings
- Try accessing the admin view for full control

---

## 📦 Setup Instructions

### Backend (Django)

1. **Clone the repository and navigate to the backend:**

   ```bash
   git clone https://github.com/phillip-l-rogers/pickleball.git
   cd pickleball-backend
   ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Frontend (React)

1. **Open a new terminal and navigate to the frontend:**

    ```bash
    cd ../pickleball-frontend
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Run the development server:**

    ```bash
    npm run dev
    ```

4. **Visit:**

    http://localhost:5173/


--- 

## 📁 Project Structure

```bash
pickleball/
├── pickleball-backend/     # Django + DRF
│   ├── manage.py
│   ├── api/                # Core tournament logic
│   └── requirements.txt
├── pickleball-frontend/    # React + Tailwind
│   ├── src/
│   └── package.json
```

--- 

## 📚 Acknowledgments

- This project was built as the final capstone for CS50W
- Inspired by local round-robin pickleball tournaments and league tools

---

## 📜 License

- Educational use only. Built as part of Harvard CS50W.