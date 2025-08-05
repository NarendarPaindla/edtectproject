# Step by Step Installations
```commands
1. cd backend
2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. Add the .env file in the backend folder
6. uvicorn app.main:app --reload
```

# .env

```
MONGODB_URI=
DATABASE_NAME=edtech
SECRET_KEY=b2wet435662szdcfhntyiv5c6ffdxwfer
HF_API_KEY=

```


## Folder Structure

```
edtech-adaptive-learning-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── content.py
│   │   │   ├── performance.py
│   │   │   └── feedback.py
│   │   ├── repositories/
│   │   │   ├── user_repo.py
│   │   │   ├── content_repo.py
│   │   │   ├── performance_repo.py
│   │   │   └── feedback_repo.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── courses.py
│   │   │   ├── recommendations.py
│   │   │   ├── assessments.py
│   │   │   └── feedback.py
│   │   └── ai/
│   │       ├── __init__.py
│   │       ├── adaptive_learning.py
│   │       ├── recommendation_engine.py
│   │       ├── feedback_generator.py
│   │       ├── assessment_adapter.py
│   │       └── nlp_utils/
│   │           ├── summarizer.py
│   │           ├── question_generator.py
│   │           └── embedding_service.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── …
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── StudentDashboard.jsx
│   │   │   ├── TeacherDashboard.jsx
│   │   │   └── AdminDashboard.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── auth.js
│   │   ├── theme/
│   │   │   ├── lightTheme.js
│   │   │   └── darkTheme.js
│   │   ├── App.jsx
│   │   └── index.js
│   ├── Dockerfile
│   └── package.json
├── analytics/
│   └── streamlit_app/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
├── deployment/
│   ├── render.yaml
│   └── README.md
├── tests/
│   ├── backend/
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   └── …
│   ├── ai/
│   │   ├── test_adaptive_learning.py
│   │   └── …
│   └── frontend/
│       └── …
├── .gitignore
└── README.md
```